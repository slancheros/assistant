import sounddevice as sd
from scipy.io.wavfile import write
sd.default.device = 2
fs = 44100  # Sample rate
seconds =10  # Duration of recording
print(sd.query_devices())
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file