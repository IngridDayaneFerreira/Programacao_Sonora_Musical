import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play

chunk = 1024 # record in chunks of 1024 samples
sample_format = pyaudio.paInt16 # 16 bits per sample
channels = 2 # mono - 1 channel / stereo - 2 channels
sample_rate = 44100 # 44100 samples per second
duration = 10 # 10 seconds of recording
filename = "output.wav"

p = pyaudio.PyAudio() 

print('Recording audio...')

# opening the file to add frames
stream = p.open(format=sample_format,
                channels=channels, 
                rate=sample_rate, 
                frames_per_buffer=chunk,
                input=True)

frames = [] # array to store captured frames

for i in range(0, int(sample_rate / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data) #adding frames on the audio

stream.stop_stream() #stoping the recording
stream.close() #closing the recording

p.terminate()

print('Audio recording finished!')

# saving the audio to the file using wave
wave_file = wave.open(filename, 'wb')
wave_file.setnchannels(channels)
wave_file.setsampwidth(p.get_sample_size(sample_format))
wave_file.setframerate(sample_rate)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print('Playing recorded original wave file...')

#playing the audio
play_file = AudioSegment.from_file(file = "output.wav", 
                                  format = "wav")

play(play_file)

print('Playing recorded wave file whith + 5dB...')

new_play_file = play_file + 5 #adding 5dB to the original audio

play(new_play_file) #playing the new audio whith 5dB more

print('Finished!')