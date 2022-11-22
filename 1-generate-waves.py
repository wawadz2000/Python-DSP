from thinkdsp import CosSignal, SinSignal, read_wave
from matplotlib import pyplot
import IPython 
import thinkdsp  
import thinkplot
import librosa as lib
import numpy as np
import matplotlib.pyplot as plot
import IPython.display as ipd

s1 = SinSignal(freq=8, amp=3, offset=0)
s2 = SinSignal(freq=4, amp=5, offset=0)
mix=s1+s2
waveMix = mix.make_wave(duration=5, start=0, framerate=2000)
mix.plot()
waveMix.make_audio()

