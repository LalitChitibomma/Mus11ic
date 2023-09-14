import shutil
import os
from music21.chord import Chord
from music21.stream import Stream as MusicStream
from music21.meter import TimeSignature
import random
from pyo import *
from time import sleep

notes = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 
         'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}

tones_flat = {0: 'C', 1: 'Db', 2: 'D', 3: 'Eb', 4: 'E', 5: 'F', 6: 'Gb', 7: 'G', 8: 'Ab', 9: 'A', 10: 'Bb', 11: 'B'}
tones_sharp = {0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F', 6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'}

intervals = {0: 'Unison', 1: 'Minor 2nd', 2: 'Major 2nd', 3: 'Minor 3rd', 4: 'Major 3rd', 5: 'Perfect 4th', 6: 'Tritone', 
             7: 'Perfect 5th', 8: 'Minor 6th', 9: 'Major 6th', 10: 'Minor 7th', 11: 'Major 7th', 12: 'Octave', 13: 'Minor 9th', 
             14: 'Major 9th', 15: 'Minor 10th', 16: 'Major 10th', 17: 'Perfect 11th', 18: 'Tritave', 19: 'Double Octave', 
             20: 'Minor 14th', 21: 'Major 14th', 22: 'Minor 15th', 23: 'Major 15th'}

intervals_abv = {0: 'U', 1: 'm2', 2: 'M2', 3: 'm3', 4: 'M3', 5: 'P4', 6: 'TT', 7: 'P5', 8: 'm6', 9: 'M6', 10: 'm7', 11: 'M7', 12: 'P8', 
                 13: 'm9', 14: 'M9', 15: 'm10', 16: 'M10', 17: 'P11', 18: 'TTv', 19: 'D8', 20: 'm14', 21: 'M14', 22: 'm15', 23: 'M15'}

circle_of_fifths = ['C', 'G', 'D', 'A', 'E', 'B', 'Fs', 'Cs', 'Gs', 'Ds', 'As', 'F']

class Note:
  def __init__(self, note, octave, tune=440) -> None:
    self.note = note
    self.octave = octave
    self.tune = tune
    self.frequency = round((tune/16) * pow(2, (octave-1) + (notes[note] + 3)/12), 2)

  def __str__(self) -> str:
    return f'{self.note}{self.octave}'
  
  def __repr__(self) -> str:
    return f'{self.note}{self.octave}'
  
  def __eq__(self, other) -> bool:
    return self is other or (self.note == other.note and self.octave == other.octave)
  
  def interval(self, other, include_name=False):
    if other.octave >= self.octave:
      interval = notes[other.note] - notes[self.note] 
    else:
      interval = notes[other.note] - notes[self.note] - 12
    
    if other.octave > self.octave:
      interval += 12

    return intervals[abs(interval)] if include_name else interval
  
  def interval_direction(self, other):
    if self.interval(other) == 0:
      return 'Same'
    elif self.interval(other) > 0:
      return 'Up'
    return 'Down'
    
  def scale(self, type='Major'):
    semitones = notes[self.note]
    octave = self.octave
    scale = []
    scale_conditions = {
        'Major': {2, 6},
        'Ionian': {2, 6},
        'Dorian': {1, 5},
        'Phrygian': {0, 4},
        'Lydian': {6, 3},
        'Mixolydian': {5, 2},
        'Aeolian': {4, 1},
        'Minor': {4, 1},
        'Locrian': {3, 0}
    }

    for i in range(8):
      if type == 'Lydian' or self.note in {'G', 'D', 'A', 'E', 'B'}:
        scale.append(Note(tones_sharp[semitones], octave, self.tune))
      else:
        scale.append(Note(tones_flat[semitones], octave, self.tune))

      if i in scale_conditions[type]:
        semitones += 1
      else:
        semitones += 2

      if semitones >= 12:
        semitones -= 12
        octave += 1
    
    return scale
  
def build_counterpoint(cantus_firmus):
  counterpoint = []
  interval = 0

  for measure, note in enumerate(cantus_firmus):
    cantus_firmus_interval = notes[note]

    if measure + 1 == len(cantus_firmus):
      interval = 0
      counterpoint.append(note)

    elif interval == 0 or interval == 7 or measure + 2 == len(cantus_firmus):
      interval = random.choice([4, 9])
      current_interval = interval + cantus_firmus_interval
      current_interval = current_interval if current_interval <= 11 else current_interval - 12
      if tones_sharp[current_interval][-1] == '#':
        current_interval -= 1
      counterpoint.append(tones_sharp[current_interval])

    else:
      interval = random.choice([0, 4, 7, 9])
      current_interval = interval + cantus_firmus_interval
      current_interval = current_interval if current_interval <= 11 else current_interval - 12
      if tones_sharp[current_interval][-1] == '#':
        current_interval -= 1
      counterpoint.append(tones_sharp[current_interval])
    
  return counterpoint

def create_midi(cantus_firmus, counterpoint, filename='my_counterpoint', dir_path=''):
  s = MusicStream()
  s.append(TimeSignature('4/4'))
  for i in range(len(counterpoint)):
    s.append(Chord(f'{cantus_firmus[i]}2 {counterpoint[i]}5', quarterLength=4))
  
  filename = f'{filename}.midi'
  s.write('midi', fp='my_counterpoint.midi')
  if dir_path == '':
    current_directory = os.getcwd()
    source = os.path.join(current_directory, filename)
    destination = os.path.join(current_directory, filename)
    shutil.move(source, destination)
  else:
    shutil.move(filename, dir_path)

def play_note(freq, duration=1, volume=0.5):
  amp = Fader(fadein=0.01, fadeout=0.1, dur=duration, mul=volume)
  amp.play()
  return SuperSaw(freq, mul=amp).out()

def play_counterpoint(Cantus_firmus, Counterpoint):
  s = Server().boot()
  s.start()

  for i in range(len(Counterpoint)):
      cf = play_note(Note(Cantus_firmus[i], 2).frequency, 3, 0.25)
      cp = play_note(Note(Counterpoint[i], 4).frequency, 3, 0.25)
      sleep(1.5)
  sleep(2)

  s.stop()
