from pydub import AudioSegment
from pydub.playback import play

print('Mixing teste.wav and melody.wav...')
audio1 = AudioSegment.from_wav("output.wav")
audio2 = AudioSegment.from_wav("out.wav")

# panorama: -1 esquerda, 0 center, 1 direita
audio1 = audio1.pan(-0.8) #mais a esquerda
audio1 = audio1 + 3 # volume mais 3dB

audio2 = audio2.pan(0.8) #mais a direita
audio2 = audio2 + 5 # volume mais 5dB

mixed_audio = audio1.overlay(audio2)

print('Playing mixed audio...')
play(mixed_audio)

print('Saving mixed file')

mixed_audio.export("mix.wav", format="wav")