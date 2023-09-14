from Mus11ic import Note, build_counterpoint, create_midi, play_note, play_counterpoint
from pyo import *
from time import sleep

Cantus_firmus = "G D A E G C F E A D C"
Cantus_firmus = Cantus_firmus.split()
Counterpoint = build_counterpoint(Cantus_firmus)
create_midi(Cantus_firmus, Counterpoint, dir_path='/Users/Chiti/Downloads/Counterpoint/Blah')
print(Counterpoint)
play_counterpoint(Cantus_firmus, Counterpoint)

scale_1 = Note('F', 3).scale()
scale_2 = Note('A', 3).scale('Phrygian')
scale_3 = Note('C', 3).scale('Mixolydian')
scale_4 = Note('E', 3).scale('Locrian')

# Initialize Pyo audio server
s = Server().boot()
s.start()

# Plays 6-2-5-1 Progression
for i in [3, 6, 2, 5, 1]:
    osc_1 = play_note(scale_1[i].frequency, 3, 0.25)
    osc_2 = play_note(scale_2[i].frequency, 3, 0.25)
    osc_3 = play_note(scale_3[i].frequency, 3, 0.25)
    osc_4 = play_note(scale_4[i].frequency, 3, 0.25)
    if i == 1:
        sleep(1.5)
    sleep(0.5)

s.stop()
