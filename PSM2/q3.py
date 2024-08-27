from music21 import stream, note, midi
from midiutil import MIDIFile
from midi2audio import FluidSynth
from pydub import AudioSegment
from pydub.playback import play

#get the midi file
midi_file_name = "./sound.mid"

#array whith notes
#notes = ["C4", "D4", "E4", "F4", "G4", "A4", "B4"] 
#notes = ["C5","D5","E5","D5","C5","C5","G5","E5","G5","G5","G5","F5","F5","E5","E5","D5","D5","C5","E5"]
notes = ["C5","C5","D5","C5","F5","E5","C5","C5","D5","C5","G5","F5","C5","C5","C6","A5","F5","E5","D5"]

#creating objects
score = stream.Score()
part = stream.Part()
score.append(part)

#array that adds the notes to the score 
for note_name in notes:
    new_note = note.Note(note_name)
    part.append(new_note)

midi_file = midi.translate.music21ObjectToMidiFile(score) #Converts the score to a MIDIFile object
midi_file.open(midi_file_name, "wb") #open the midi file to writing
midi_file.write()
midi_file.close()


midi_file.open(midi_file_name, "rb") #open the midi file to reading

soundfont_file = "./piano.sf2"
# soundfont_file = "./Strat_Marshall.sf2"
# soundfont_file = "./Theremin.sf2"
# soundfont_file = "./WT_Trumpet.sf2"

wave_file = "./out.wav"

FluidSynth(soundfont_file).midi_to_audio(midi_file_name, wave_file)