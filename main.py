import pyaudio
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq, ifft
import time

# Parameters for audio input
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open audio stream
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK_SIZE)

# Create a frequency array
freq_array = np.fft.fftfreq(CHUNK_SIZE, 1/RATE)

# Main loop
try:
    while True:
        start_time = time.time() * 1000
        end_time = start_time + 1000
        # Read audio data from the microphone
        audio_data = np.frombuffer(stream.read(CHUNK_SIZE), dtype=np.int16)
        #audio_data = audio_data[1]
        # Calculate the FFT of the audio data
        #N = len(audio_data)
        yf = fft(audio_data)
        
        xf = ifft(yf)
        
        #xf = fftfreq(xf[0], 1 / RATE)

        # return dominant frequnecy
        idx = np.abs(yf)
        #freq = xf[idx]
        processed_frequency = np.linalg.norm(max(yf))
        #print the dominant frequency
        print(processed_frequency, end='\r')
        time.sleep(0.1)


except KeyboardInterrupt:
    pass

# Clean up
stream.stop_stream()
stream.close()
p.terminate()

