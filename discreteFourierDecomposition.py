# READ A WAVE FILE
import wave
import numpy as np
import matplotlib.pyplot as plt

fileName = "Trees c5.wav"
with wave.open(fileName, "rb") as input:
	#print(input.getcomptype()) #double check there isnt any compression
	channels = input.getnchannels()
	sampleRate = input.getframerate() # this wav sample is 44100
	nframes = input.getnframes()
	audiobytes = input.readframes(nframes)
	input.rewind() # just in case

# Convert signal to numpy array and limit signal range, proportionally
signal = np.fromstring(audiobytes, dtype=np.int16, count=nframes)
n = signal.size #/ 10
# TODO: one slider for position, another for zoom level (down to 1 single sample)
signal = signal[:n]


d = 1/float(sampleRate)
t = np.linspace(0,1,num=n, endpoint=False) # time vector

def plotSpectrum(y,Fs):
    """
    Plots a Single-Sided Amplitude Spectrum of y(t)
    """
    n = len(y) # length of the signal
    n2 = round(n/2)
    k = np.arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(0,n2)] # one side frequency range

    Y = np.fft.fft(y)/n # fft computing and normalization
    Y = Y[range(n2)]
	 
    plt.plot(frq,abs(Y),'r') # plotting the spectrum
    plt.ylim([0,22000])
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|Y(freq)|')


plt.subplot(2,1,1)
#np.savetxt("Trees c2.txt", signal)
plt.plot(t,signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
ax=plt.subplot(2,1,2)
plotSpectrum(signal, sampleRate)
ax.set_xscale("log")
#ax.set_yscale("log") # This is definitely more aesthetically appealing...

plt.show()