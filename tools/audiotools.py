import numpy as np
from scipy.integrate import simps, trapz

VERBOSE = True
DBFACTOR = 20

def calc_db(peak, caldB, cal_peak):
    try:
        pbdB = DBFACTOR * np.log10(peak/cal_peak) + caldB
    except ZeroDivisionError:
        print('attempted division by zero:')
        print('peak {}, caldb {}, calpeak {}'.format(peak, caldB, cal_peak))
        pbdB = np.nan
    return pbdB

def calc_noise(fft_vector, ix1,ix2):
    fft_slice = fft_vector[ix1:ix2]
    area = trapz(fft_slice)
    return area

def calc_spectrum(signal,rate):
    #calculate complex fft

    # pad with zeros?
    #padded_signal = np.zeros(len(signal*2))
    #padded_signal[:len(signal)] = signal
    #signal = padded_signal
    npts = len(signal)

    freq = np.arange(npts)/(npts/rate)
    freq = freq[:(npts/2)] #single sided
    #print('freq len ', len(freq))

    sp = np.fft.fft(signal)/npts
    sp = sp[:(npts/2)]
    #print('sp len ', len(sp))

    return freq, sp.real

def get_fft_peak(spectrum, freq, atfrequency=None):
    # find the peak values for spectrum
    if atfrequency is None:
        maxidx = spectrum.argmax(axis=0)
        f = freq[maxidx]
        spec_peak = np.amax(spectrum)
    else:
        f = atfrequency
        spec_peak = spectrum[freq==f]
    return spec_peak, f

def make_tone(freq,db,dur,risefall,samplerate, caldb=100, calv=0.1, adjustdb=0):
    # create portable tone generator class that allows the 
    # ability to generate tones that modifyable on-the-fly
    npts = dur * samplerate
    try:
    
        #print("duration (s) :{}".format(dur))
        # equation for db from voltage is db = 20 * log10(V2/V1))
        # 10^(db/20)
        db = db + adjustdb
        v_at_caldB = calv
        caldB = caldb
        amp = (10 ** ((db-caldB)/DBFACTOR)*v_at_caldB)

        if VERBOSE:
            print("current dB: {}, current frequency: {} kHz, AO Amp: {:.6f}".format(db, freq/1000, amp))
            print("cal dB: {}, V at cal dB: {}".format(caldB, v_at_caldB))

        rf_npts = risefall * samplerate
        #print('amp {}, freq {}, npts {}, rf_npts {}'
        # .format(amp,freq,npts,rf_npts))
    
        tone = amp * np.sin((freq*dur) * np.linspace(0, 2*np.pi, npts))
        #add rise fall
        if risefall > 0:
            tone[:rf_npts] = tone[:rf_npts] * np.linspace(0,1,rf_npts)
            tone[-rf_npts:] = tone[-rf_npts:] * np.linspace(1,0,rf_npts)
        
        timevals = np.arange(npts)/samplerate

        # in the interest of not blowing out the speakers I am going to set this to 5?
        if np.amax(abs(tone)) > 5:
            print("WARNING: OUTPUT VOLTAGE {:.2f} EXCEEDS MAXIMUM, RECALULATING".format(np.amax(abs(tone))))
            tone = tone/np.amax(abs(tone))

    except:
        print("WARNING: Unable to produce tone")
        tone = np.zeros(npts)
        timevals = np.arange(npts)/samplerate

    return tone, timevals

