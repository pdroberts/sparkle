import os, time
import threading

from PyQt4 import QtCore, QtGui

from tcform import Ui_TuningCurve
from audiolab.calibration.calibration import ToneCurve
from audiolab.tools.qthreading import GenericThread, WorkerSignals

RED = QtGui.QPalette()
RED.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
GREEN = QtGui.QPalette()
GREEN.setColor(QtGui.QPalette.Foreground,QtCore.Qt.green)


class TuningCurve(QtGui.QWidget):
    def __init__(self, outchans, inchans, live_lock, saveinfo, parent=None):
        # auto generated code intialization
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_TuningCurve()
        self.ui.setupUi(self)

        # assume one channel each for now
        self.aochan = outchans
        self.aichan = inchans
        self.live_lock = live_lock

        self.ui.start_btn.clicked.connect(self.run_curve)
        self.ui.stop_btn.clicked.connect(self.abort_curve)

        self.ui.running_label.setPalette(RED)
        self.apply_calibration = False
        self.display = None

        self.savefolder = saveinfo[0]
        self.savename = saveinfo[1]
        self.saveformat = saveinfo[2]

        self.signals = WorkerSignals()
        self.signals.spectrum_analyzed.connect(self.display_response)

    def run_curve(self):
        print "run curve"

        if self.live_lock.tryLock():
            # will need to replace this with user defined filepath
            if self.apply_calibration:
                calibration_vector = np.load(os.path.join(caldata_filename()))
                calibration_freqs = np.load(os.path.join(calfreq_filename()))

            self.ui.start_btn.setEnabled(False)

            self.fscale = 1000
            self.tscale = 0.001

            self.ngenerated = 0
            self.nacquired = 0
            self.halt = False

            try:
                #scale_factor = 1000
                f_start = self.ui.freq_start_spnbx.value()*self.fscale
                f_stop = self.ui.freq_stop_spnbx.value()*self.fscale
                f_step = self.ui.freq_step_spnbx.value()*self.fscale
                db_start = self.ui.db_start_spnbx.value()
                db_stop = self.ui.db_stop_spnbx.value()
                db_step = self.ui.db_step_spnbx.value()
                dur = self.ui.dur_spnbx_2.value()*self.tscale
                rft = self.ui.risefall_spnbx_2.value()*self.tscale
                reprate = self.ui.reprate_spnbx.value()
                sr = self.ui.sr_spnbx_2.value()*self.fscale
                nreps = self.ui.nreps_spnbx.value()

                if f_start < f_stop:
                    freqs = range(f_start, f_stop+1, f_step)
                else:
                    freqs = range(f_start, f_stop-1, -f_step)
                if db_start < db_stop:
                    intensities = range(db_start, db_stop+1, db_step)
                else:
                    intensities = range(db_start, db_stop-1, -db_step)

                # calculate ms interval from reprate
                interval = (1/reprate)*1000
                self.sr = sr
                self.interval = interval

                # set up display
                if self.display == None or not(self.display.active):
                    self.spawn_display()
                    #self.display.show()

                if not os.path.isdir(self.savefolder):
                    os.makedirs(self.savefolder)

                fname = os.path.join(self.savefolder,self.savename+'.hdf5')
                self.tonecurve = ToneCurve(dur, sr, rft, nreps, freqs, 
                                            intensities, 
                                           filename=fname)

                if self.apply_calibration:
                    self.tonecurve.set_calibration(calibration_vector, calibration_freqs)

                self.tonecurve.assign_signal(self.signals.spectrum_analyzed)
                self.calval = self.tonecurve.arm(self.aochan, self.aichan)
                self.ngenerated +=1

                self.ui.running_label.setText(u"RUNNING")
                self.ui.running_label.setPalette(GREEN)

                # save these lists for easier plotting later
                self.freqs = freqs
                self.intensities = intensities

                # save the start time and set last tick to expired, so first
                # acquisition loop iteration executes immediately
                self.start_time = time.time()
                self.last_tick = self.start_time - (interval/1000)
                self.acq_thread = threading.Thread(target=self.curve_worker)
                self.acq_thread.start()                    

            except:
                self.live_lock.unlock()
                print u"handle curve set-up exception"
                self.ui.start_btn.setEnabled(True)
                raise
        else:
            print u"Operation already in progress"


    def curve_worker(self):
        print('do work')
        pass
        
    def abort_curve(self):
        print "abort!"

    def spawn_display(self):
        print "display"

    def display_response(self):
        pass