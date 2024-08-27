from music21 import stream, note, midi
from midiutil import MIDIFile
from midi2audio import FluidSynth

notes = ["c4","D4","E4","F4","G4","A4","B4"]

score = stream.Score()
part = stream.Part()
score.append(part)

for note_name in notes:
    new_note = note.Note(note_name)

midi_file = midi.translate.music21ObjectToMidiFile(score)
midi_file.open("example_track.mid","wb")
midi_file.write()
midi_file.close()

soundfront = "piano,sf2"
fs = fluidsynth.Synth()

#carrega o timbre
fs.sfload(soundfront_file)

#carrega o arquivo midi
fs.smfload(midi_file_name)
