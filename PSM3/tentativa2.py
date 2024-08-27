import time
import fluidsynth
from midi2audio import FluidSynth

midi_name = "sound.mid"
fs = fluidsynth.Synth()
fs.start(driver="coreaudio" if fluidsynth.fluidsynth_cmd().startswith("fluidsynth") else None)

soundfont_file_piano = "./piano.sf2"
soundfont_file_MArshall = "./Strat_Marshall.sf2"
soundfont_file_Theremin = "./Theremin.sf2"
soundfont_file_Trumpet = "./WT_Trumpet.sf2"

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

sfid = fs.sfload(timbre)

player = fs.midi_player()
player.add(midi_name)

while player.get_status() == fluidsynth.MIDI_PLAYER_PLAYING:
    time.sleep(0.1)
player.stop()
fs.delete()