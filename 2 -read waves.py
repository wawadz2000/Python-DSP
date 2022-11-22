import librosa
import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display
import librosa
import IPython 
import thinkdsp  
import thinkplot
import soundfile as sf


wave_x, sample_rate = librosa.load('sunday.wav')
ipd.Audio(wave_x, rate=sample_rate)
plt.figure(figsize=(15, 4), facecolor=(.9, .9, .9))
librosa.display.waveshow(wave_x, sr=sample_rate, color='red')
sf.write('created.wav', wave_x, samplerate=1000)
