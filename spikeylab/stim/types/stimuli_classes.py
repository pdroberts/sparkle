import os
import wave

import scipy.io.wavfile as wv
import numpy as np

from PyQt4 import QtGui, QtCore

from spikeylab.stim.abstract_stimulus import AbstractStimulusComponent
from spikeylab.stim.types.widgets import tone_parameters, silence_parameters
from spikeylab.stim.types.widgets import vocal_parameters
from spikeylab.tools.audiotools import spectrogram, make_tone

from matplotlib.cm import get_cmap
from enthought.chaco import default_colormaps
from chaco.api import DataRange1D

generator = default_colormaps.color_map_name_dict['jet']
cmap = generator(DataRange1D())
cmap = np.array(cmap.color_bands)
cmap = cmap[:,0:3]
COLORTABLE=[]
for i in range(256): 
    row = cmap[i,:]*255
    COLORTABLE.append(QtGui.qRgb(*row))

class Tone(AbstractStimulusComponent):
    foo = None

class PureTone(Tone):
    name = "Pure Tone"
    explore = True
    protocol = True
    _frequency = 5000
    def update_fscale(self, scale):
        print '!updating tone scale'
        self._frequency_details['multiplier'] = scale

    def frequency(self):
        return self._frequency

    def setFrequency(self, freq):
        self._frequency = freq

    def showEditor(self):
        editor = tone_parameters.ToneParameterWidget()
        editor.setComponent(self)
        return editor

    def paint(self, painter, rect, palette):

        painter.fillRect(rect, palette.base())
        painter.drawText(rect.x()+5, rect.y()+12, rect.width()-5, rect.height()-12, QtCore.Qt.AlignLeft, "Pure Tone")
        painter.fillRect(rect.x()+5, rect.y()+35, rect.width()-10, 20, QtCore.Qt.black)
        painter.drawText(rect.x()+5, rect.y()+80, str(self._frequency/1000) + " kHz")

    def signal(self, fs, atten):
        tone = make_tone(self._frequency, self._intensity+atten, self._duration, self._risefall, fs)[0]
        return tone

    def stateDict(self):
        state = super(PureTone, self).stateDict()
        state['frequency'] = self._frequency

        return state

    def loadState(self, state):
        super(PureTone,self).loadState(state)
        self._frequency = state['frequency']
        print 'loaded freq', self._frequency

    def auto_details(self):
        details = super(PureTone, self).auto_details()
        details['frequency'] = {'label':self._labels[1], 'multiplier':self._scales[1], 'min':0, 'max':200000}
        return details

class FMSweep(Tone):
    name = "fmsweep"
    start_frequency = None
    stop_frequency = None

class Vocalization(AbstractStimulusComponent):
    name = "Vocalization"
    explore = True
    protocol = True
    _filename = None
    _browsedir = os.path.expanduser('~')

    def browsedir(self):
        return self._browsedir

    def setBrowseDir(self, browsedir):
        self._browsedir = browsedir

    def file(self):
        return self._filename

    def samplerate(self):
        if self._filename is not None:
            wf =  wave.open(self._filename)
            fs= wf.getframerate()
            wf.close()
            return fs

    def stateDict(self):
        state = super(Vocalization, self).stateDict()
        state['file'] = self._filename

        return state

    def setFile(self, fname):
        if fname is not None:
            self._filename = fname

            try:
                sr, wavdata = wv.read(fname)
            except:
                print u"Problem reading wav file"
                raise
            # wavdata = wavdata.astype(float)
            # nfft=512
            # Pxx, freqs, bins, im = specgram(wavdata, NFFT=nfft, Fs=sr, noverlap=int(nfft*0.9), pad_to=nfft*2)

            self._duration = float(len(wavdata))/sr


    def paint(self, painter, rect, palette):

        if self._filename is not None:
            
            spec, f, bins, fs = spectrogram(self._filename)
            spec_max = np.amax(spec)
            scaled = spec/(spec_max/255)
            scaled = np.require(scaled, np.uint8, 'C')
            data = scaled.data[::-1]

            image = QtGui.QImage(data, len(bins), len(f), QtGui.QImage.Format_Indexed8)
            image.setColorTable(COLORTABLE)
            # image = image.mirrored(True,False)
            pixmap = QtGui.QPixmap.fromImage(image)
            painter.drawPixmap(rect.x(), rect.y(), rect.width(), rect.height(), pixmap)
        else:
            painter.save()
            # draw a warning symbol
            smallrect = QtCore.QRect(rect.x()+10, rect.y()+10, rect.width()-20, rect.height()-20)
            painter.setPen(QtGui.QPen(QtCore.Qt.red, 8))
            painter.drawEllipse(smallrect)
            rad = smallrect.width()/2
            x = rad - (np.cos(np.pi/4)*rad)
            painter.drawLine(smallrect.x()+x, smallrect.y()+x, smallrect.x()+smallrect.width()-x, smallrect.y()+smallrect.height()-x)

            painter.restore()
            
    def showEditor(self):
        editor = vocal_parameters.VocalParameterWidget()
        editor.setComponent(self)
        return editor

    def signal(self, fs, atten):
        try:
            sr, wavdata = wv.read(self._filename)
        except:
            print u"Problem reading wav file"
            raise
        if fs != sr:
            print 'specified', fs, 'wav file', sr
            raise Exception("specified samplerate does not match wav stimulus")
        # normalize to calibration
        wavdata = wavdata.astype(float)
        print "DANGER vocal wav files Hard-coded calibration 100db 0.1V"
        caldB = 100
        v_at_caldB = 0.1
        max_amp = np.amax(wavdata)
        amp = (10 ** ((self._intensity+atten-caldB)/20)*v_at_caldB)
        wavdata = ((wavdata/max_amp)*amp)
        return wavdata

class Noise(AbstractStimulusComponent):
    name = "noise"

class Silence(AbstractStimulusComponent):
    name = "silence"
    protocol = True
    def paint(self, painter, rect, palette):
        mid = rect.y() + (rect.height()/2)
        painter.drawLine(rect.x()+5, mid, rect.x()+rect.width()-10, mid)

    def showEditor(self):
        editor = silence_parameters.SilenceParameterWidget()
        editor.setComponent(self)
        return editor

    def signal(self, fs, atten):
        return np.zeros((self._duration*fs,))

class Modulation(AbstractStimulusComponent):
    modulation_frequency = None

class SAM(Modulation):
    """Sinusodal Amplitude Modulation"""
    name = "sam"

class SquareWaveModulation(Modulation):
    name = "squaremod"

class SFM(AbstractStimulusComponent):
    name = "sfm"

class Ripples(AbstractStimulusComponent):
    name = "ripples"