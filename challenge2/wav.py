import wave
import struct
import math
import requests

array = []
for i in range(0, 5):
    r = requests.get('https://www.random.org/integers/?num=9602&min=0&max=255&col=1&base=10&format=plain&rnd=new')
    array.extend(map(int, r.text.splitlines()))

sampleRate = 16000
duration = 3.0       # seconds

# Use different frequencies for the left and right channels
rFreq = 1760.00  # A
lFreq = 523.25  # C

wavef = wave.open('sound.wav', 'w')
wavef.setnchannels(2)  # stereo
wavef.setsampwidth(2)
wavef.setframerate(sampleRate)

print duration * sampleRate
for i in range(int(duration * sampleRate)):
    wavef.writeframesraw(struct.pack('<hh', array[i], array[i]))

wavef.writeframes('')
wavef.close()
