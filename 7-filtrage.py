import IPython 
import numpy as np
import matplotlib.pyplot as plot
import IPython.display as ipd
import numpy as np
from scipy import signal, misc

S1 = np.array([1,-1,1,-1,1,-1,1,-1,1], dtype=np.float32)
S2 = np.array([1/2,1/2], dtype=np.float32)
conv=signal.convolve(S1, S2, 'full')
corr=signal.correlate(S1, S2, mode='full')
print(corr)
plot.plot(corr)
