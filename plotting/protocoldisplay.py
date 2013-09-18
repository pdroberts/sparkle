import sys

from enthought.etsconfig.etsconfig import ETSConfig
ETSConfig.toolkit = "qt4"
from enthought.chaco.api import GridPlotContainer
# from enthought.chaco.tools.rect_zoom import RectZoomTool

# from audiolab.plotting.chacoplots import ImagePlotter, Plotter, DataPlotWidget, ImageWidget, TraceWidget
from audiolab.plotting.custom_plots import TraceWidget, FFTWidget, SpecWidget

from PyQt4 import QtGui, QtCore

class ProtocolDisplay(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # self.fft_plot = Plotter(self, 1, rotation = -90)
        # self.fft_plot = DataPlotWidget(orientation='v')
        self.fft_plot = FFTWidget(self)
        # add a rubber band zoom to the fft plot
        # self.fft_plot.plotview.plots[0].tools.append(RectZoomTool(self.fft_plot.plotview.plots[0], drag_button="right"))
        self.spiketrace_plot = TraceWidget(self)
        # self.spiketrace_plot = DataPlotWidget(self)
        # self.signal_plot = DataPlotWidget(self)
        self.spec_plot = SpecWidget(self)

        # container = GridPlotContainer(shape=(3,2))
        # container.insert(0, self.spec_plot)
        # container.insert(2, self.signal_plot)
        # container.insert(4, self.spiketrace_plot)
        # container.insert(5, self.fft_plot)

        # self.signal_plot.setMinimumHeight(100)
        self.spec_plot.setMinimumHeight(100)
        self.spiketrace_plot.setMinimumWidth(100)
        self.spiketrace_plot.setMinimumHeight(100)
        self.fft_plot.setMinimumWidth(100)
        self.fft_plot.setMinimumHeight(100)

        # layout = QtGui.QGridLayout()
        # # layout.setSpacing(10)
        # layout.addWidget(self.spec_plot.widget, 0, 0)
        # layout.addWidget(self.signal_plot.widget, 1, 0)
        # layout.addWidget(self.spiketrace_plot.widget, 2, 0)
        # layout.addWidget(self.fft_plot.widget, 2, 1)

        splittersw = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitternw = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitterse = QtGui.QSplitter(QtCore.Qt.Horizontal)

        # splitternw.addWidget(self.spec_plot)
        # splitternw.addWidget(self.signal_plot)
        # splittersw.addWidget(splitternw)
        splittersw.addWidget(self.spec_plot)
        splittersw.addWidget(self.spiketrace_plot)
        splitterse.addWidget(splittersw)
        splitterse.addWidget(self.fft_plot)

        # set inital sizes
        # splitternw.setSizes([100])
        splittersw.setSizes([100,500])
        splitterse.setSizes([500,100])

        # link spectrogram x axis with response x axis
        # self.spec_plot.plotview.plots[0].range2d = self.spiketrace_plot.traits.trace_plot.range2d
        # print self.spec_plot.plotview.plots[0].index_range

        layout = QtGui.QHBoxLayout()
        layout.addWidget(splitterse)
        self.setLayout(layout)
        # self.setGeometry(0,0,500,500)

    def update_spec(self, *args, **kwargs):
        self.spec_plot.update_data(*args, **kwargs)

    def update_fft(self, *args, **kwargs):
        self.fft_plot.update_data(*args, **kwargs)

    def update_spiketrace(self, xdata, ydata):
        # self.spiketrace_plot.update_data(*args, **kwargs)
        self.spiketrace_plot.update_data(xdata, datakey='times', axeskey='response')
        self.spiketrace_plot.update_data(ydata, datakey='response', axeskey='response')

    def update_signal(self, xdata, ydata):
        # self.signal_plot.update_data(*args, **kwargs)
        self.spiketrace_plot.update_data(xdata, datakey='times', axeskey='stim')
        self.spiketrace_plot.update_data(ydata, datakey='signal', axeskey='stim')

    def set_xlimits(self, lims):
        self.spec_plot.set_xlim(lims)
        # self.signal_plot.set_xlim(lims)
        self.spiketrace_plot.set_xlim(lims)

    def sizeHint(self):
        return QtCore.QSize(500,300)

    # def resizeEvent(self,event):
    #     sz = event.size()
    #     self.item.setGeometry(QtCore.QRectF(0,0,sz.width(), sz.height()))

if __name__ == "__main__":
    import random, time, os
    import numpy as np
    import audiolab.tools.audiotools as audiotools
    import scipy.io.wavfile as wv
    from scipy.io import loadmat

    app = QtGui.QApplication(sys.argv)
    plot = ProtocolDisplay()
    plot.resize(800, 400)
    plot.show()

    sylpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "sample_syl.wav")
    spec, f, bins, fs = audiotools.spectrogram(sylpath)
    plot.update_spec(spec, xaxis=bins, yaxis=f)


    sr, wavdata = wv.read(sylpath)
    freqs, fft = audiotools.calc_spectrum(wavdata,sr)

    # stim_times = np.arange(0,len(wavdata),1/float(len(wavdata)))
    stim_times = np.linspace(0,float(len(wavdata))/sr, len(wavdata))


    marr = loadmat(os.path.join(os.path.abspath(os.path.dirname(__file__)),"singlesweep.mat"), squeeze_me=True)
    resp = abs(marr['sweep'])
    acq_rate = 50000

    resp_times = np.linspace(0,float(len(resp))/acq_rate, len(resp))

    print 'stim time', stim_times[-1], 'resp time', resp_times[-1]
    x = np.arange(len(wavdata))
    y = random.randint(0,10) * np.sin(x)
    # plot.update_signal(x,y)
    # plot.update_spiketrace(x,y)
    plot.update_signal(stim_times, wavdata)
    plot.update_spiketrace(resp_times,resp)
    # plot.update_spiketrace(resp_times, datakey='times', axeskey='response')
    # plot.update_spiketrace(resp, datakey='response', axeskey='response')
    for i in range(10):
        y = random.randint(0,10) * np.sin(x)
        plot.update_fft(x,y)
        time.sleep(0.2)
        QtGui.QApplication.processEvents()
    plot.update_fft(freqs,fft)

    # coerce x ranges to match
    plot.set_xlimits([0, resp_times[-1]])

    sys.exit(app.exec_())