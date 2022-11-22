import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import thinkplot
import soundfile as sf
import random
wave1, sample_rate1 = librosa.load('bass.wav', mono=True, duration=5)
wave2, sample_rate2 = librosa.load('drums.wav', mono=True, duration=5)
wave3, sample_rate3 = librosa.load('guitar.wav', mono=True, duration=5)
mix =(2*wave1+2*wave2+0.7*wave3)/3
rate=(sample_rate1+sample_rate2+sample_rate3)/3
sf.write('mix2.wav', mix, samplerate=int(rate))
