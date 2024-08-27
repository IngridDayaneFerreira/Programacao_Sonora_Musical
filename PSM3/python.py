from music21 import stream, note, midi, tempo #foi inserida a biblioteca tempo para inserir o andamento
from midiutil import MIDIFile
from midi2audio import FluidSynth
from pydub import AudioSegment
from pydub.playback import play
import mido
import time #biblioteca time para controlar o início e fim da gravação

#get the midi file
midi_file_name = "./sound.mid"

#array whith notes
#notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"] 
#notes = ["C5","D5","E5","D5","C5","C5","G5","E5","G5","G5","G5","F5","F5","E5","E5","D5","D5","C5","E5"]
notes = ["C5","C5","D5","C5","F5","E5","C5","C5","D5","C5","G5","F5","C5","C5","C6","A5","F5","E5","D5"]

#Pedindo o andamento ao usuário
andamento_interativo = int(input("Insira o tempo do andamento em Bpm: "))

#creating objects
score = stream.Score()
part = stream.Part()
andamento = tempo.MetronomeMark(number = andamento_interativo) #Atribuindo o andamento inserido prlo usuário
score.append(part)
score.append(andamento) #Inserindo o andamento na partitura

#array that adds the notes to the score 
for note_name in notes:
    new_note = note.Note(note_name)
    part.append(new_note)

midi_file = midi.translate.music21ObjectToMidiFile(score) #Converts the score to a MIDIFile object
midi_file.open(midi_file_name, "wb") #open the midi file to writing
midi_file.write()
midi_file.close()


midi_file.open(midi_file_name, "rb") #open the midi file to reading

soundfont_file_piano = "./piano.sf2"
soundfont_file_MArshall = "./Strat_Marshall.sf2"
soundfont_file_Theremin = "./Theremin.sf2"
soundfont_file_Trumpet = "./WT_Trumpet.sf2"

wave_file = "./out.wav"

timbre = int(input("Qual o timbre?\nPara Piano, digite 1\nPara MArshall, digite 2\nPara Theremin, digite 3\nPara Trumpet, digite 4\n"))

# laço onde é determinado o timbre de acordo com o que o usuário escolher
# este laço também trata caso o usuário escolha uma opção inválida
if timbre > 4 or timbre < 1:
    print('Timbre inválido')
    timbre = int(input("Qual o timbre?\nPara Piano, digite 1\nPara MArshall, digite 2\nPara Theremin, digite 3\nPara Trumpet, digite 4\n"))
    
else:
    match timbre:
        case 1: soundfont_file = soundfont_file_piano
        case 2: soundfont_file = soundfont_file_MArshall
        case 3: soundfont_file = soundfont_file_Theremin
        case 4: soundfont_file = soundfont_file_Trumpet

audio_file = FluidSynth(soundfont_file).midi_to_audio(midi_file_name, wave_file)

player = int(input('Digite 1 para iniciar a reprodução!\n'))

while player != 3:
    if player == 1:
        play(audio_file)
        player = int(input('Digite 1 para reiniciar a reprodução, 2 para pausar ou 3 para encerrar!\n'))
        #precisei acrescentar a opção de reiniciar o áudio, pois não consegui implementar a funcionalidade de pausda
        if player == 2:
            #Aqui deveria ser possível pausar o áudio
            #aqui teria um corte no áudio e audio_file receberia a parte final do corte para continuar quando o usuário qusesse
        else:
            continue
    elif player < 1 or player >3:
        print('Opção inválida!')
        player = int(input('Digite 1 para reiniciar a reprodução, 2 para pausar ou 3 para encerrar!\n'))
