import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import thinkplot
import soundfile as sf
import random
from thinkdsp import CosSignal, SinSignal, read_wave
import thinkdsp  


STD_n= 0.1
wave, sample_rate = librosa.load('sunday.wav')
noise=np.random.normal(0, STD_n, wave.shape[0])
signal_noise = wave+noise
plt.figure(figsize=(15, 4), facecolor=(.9, .9, .9))
librosa.display.waveshow(signal_noise, sr=sample_rate, color='red')
#sf.write('noise.wav', signal_noise, samplerate=sample_rate)



###################################
#s1=SinSignal(freq=2, amp=0.5, offset=0)
#s2=SinSignal(freq=240, amp=1, offset=0)
#s3=SinSignal(freq=480, amp=1, offset=0)
#signal=s1+s2+s3
#wave=signal.make_wave(duration=0.5, start=0, framerate=8850)
#wave.plot()
#noiseSin=thinkdsp.UncorrelatedGaussianNoise()
#wavenoise=noiseSin.make_wave(duration=0.5, start=0, framerate=8850)
#wavenoise.plot()

