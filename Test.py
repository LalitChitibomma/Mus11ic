import unittest
from Mus11ic import Note

def piano():
    notes = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4, 'F': 5, 'F#': 6, 
                'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11} 
    octave_1 = []
    octave_2 = []
    octave_3 = []
    octave_4 = []
    octave_5 = []
    octave_6 = []
    octave_7 = []
    
    for note in notes.keys():
        octave_1.append(Note(note, 1))
    
    for note in notes.keys():
        octave_2.append(Note(note, 2))

    for note in notes.keys():
        octave_3.append(Note(note, 3))
    
    for note in notes.keys():
        octave_4.append(Note(note, 4))
    
    for note in notes.keys():
        octave_5.append(Note(note, 5))
    
    for note in notes.keys():
        octave_6.append(Note(note, 6))
    
    for note in notes.keys():
        octave_7.append(Note(note, 7))

    return octave_1, octave_2, octave_3, octave_4, octave_5, octave_6, octave_7

class MyTestCase(unittest.TestCase):
    def test_find_interval(self):
        _, _, octave_3, octave_4, octave_5, _, _ = piano()
        C3, Cs3, Db3, D3, Ds3, Eb3, E3, F3, Fs3, Gb3, G3, Gs3, Ab3, A3, As3, Bb3, B3 = octave_3
        C4, Cs4, Db4, D4, Ds4, Eb4, E4, F4, Fs4, Gb4, G4, Gs4, Ab4, A4, As4, Bb4, B4 = octave_4
        C5, Cs5, Db5, D5, Ds5, Eb5, E5, F5, Fs5, Gb5, G5, Gs5, Ab5, A5, As5, Bb5, B5 = octave_5

        # Testing all intervals by semitone (starts on C4)
        (self.assertEqual(0, C4.interval(C4))),                                             # Unison (U)
        (self.assertEqual(1, C4.interval(Cs4)), self.assertEqual(-1, Cs4.interval(C4))),    # Minor 2nd (m2)
        (self.assertEqual(2, C4.interval(D4)), self.assertEqual(-2, D4.interval(C4))),      # Major 2nd (M2)
        (self.assertEqual(3, C4.interval(Ds4)), self.assertEqual(-3, Ds4.interval(C4))),    # Minor 3rd (m3)
        (self.assertEqual(4, C4.interval(E4)), self.assertEqual(-4, E4.interval(C4))),      # Major 3rd (M3)
        (self.assertEqual(5, C4.interval(F4)), self.assertEqual(-5, F4.interval(C4))),      # Perfect 4th (P4)
        (self.assertEqual(6, C4.interval(Fs4)), self.assertEqual(-6, Fs4.interval(C4))),    # Tritone (TT)
        (self.assertEqual(7, C4.interval(G4)), self.assertEqual(-7, G4.interval(C4))),      # Perfect 5th (P5)
        (self.assertEqual(8, C4.interval(Gs4)), self.assertEqual(-8, Gs4.interval(C4))),    # Minor 6th (m6)
        (self.assertEqual(9, C4.interval(A4)), self.assertEqual(-9, A4.interval(C4))),      # Major 6th (M6)
        (self.assertEqual(10, C4.interval(As4)), self.assertEqual(-10, As4.interval(C4))),  # Minor 7th (m7)
        (self.assertEqual(11, C4.interval(B4)), self.assertEqual(-11, B4.interval(C4))),    # Major 7th (M7)
        (self.assertEqual(12, C4.interval(C5)), self.assertEqual(-12, C5.interval(C4))),    # Octave (P8)
        (self.assertEqual(13, C4.interval(Cs5)), self.assertEqual(-13, Cs5.interval(C4))),  # Minor 9th (m9)
        (self.assertEqual(14, C4.interval(D5)), self.assertEqual(-14, D5.interval(C4))),    # Major 9th (M9)
        (self.assertEqual(15, C4.interval(Ds5)), self.assertEqual(-15, Ds5.interval(C4))),  # Minor 10th (m10)
        (self.assertEqual(16, C4.interval(E5)), self.assertEqual(-16, E5.interval(C4))),    # Major 10th (M10)
        (self.assertEqual(17, C4.interval(F5)), self.assertEqual(-17, F5.interval(C4))),    # Perfect 11th (P11)
        (self.assertEqual(18, C4.interval(Fs5)), self.assertEqual(-18, Fs5.interval(C4))),  # Tritave (P12)
        (self.assertEqual(19, C4.interval(G5)), self.assertEqual(-19, G5.interval(C4))),    # Double Octave (P13)
        (self.assertEqual(20, C4.interval(Gs5)), self.assertEqual(-20, Gs5.interval(C4))),  # Minor 14th (m14)
        (self.assertEqual(21, C4.interval(A5)), self.assertEqual(-21, A5.interval(C4))),    # Major 14th (M14)
        (self.assertEqual(22, C4.interval(As5)), self.assertEqual(-22, As5.interval(C4))),  # Minor 15th (m15)
        (self.assertEqual(23, C4.interval(B5)), self.assertEqual(-23, B5.interval(C4)))     # Major 15th (M15)

        # Testing all intervals by name (starts on C4)
        (self.assertEqual(('Unison'), C4.interval(C4, True))),                                                                     # Unison (U)
        (self.assertEqual(('Minor 2nd'), C4.interval(Cs4, True)), self.assertEqual(('Minor 2nd'), Cs4.interval(C4, True))),        # Minor 2nd (m2)
        (self.assertEqual(('Major 2nd'), C4.interval(D4, True)), self.assertEqual(('Major 2nd'), D4.interval(C4, True))),          # Major 2nd (M2)
        (self.assertEqual(('Minor 3rd'), C4.interval(Ds4, True)), self.assertEqual(('Minor 3rd'), Ds4.interval(C4, True))),        # Minor 3rd (m3)
        (self.assertEqual(('Major 3rd'), C4.interval(E4, True)), self.assertEqual(('Major 3rd'), E4.interval(C4, True))),          # Major 3rd (M3)
        (self.assertEqual(('Perfect 4th'), C4.interval(F4, True)), self.assertEqual(('Perfect 4th'), F4.interval(C4, True))),      # Perfect 4th (P4)
        (self.assertEqual(('Tritone'), C4.interval(Fs4, True)), self.assertEqual(('Tritone'), Fs4.interval(C4, True))),            # Tritone (TT)
        (self.assertEqual(('Perfect 5th'), C4.interval(G4, True)), self.assertEqual(('Perfect 5th'), G4.interval(C4, True))),      # Perfect 5th (P5)
        (self.assertEqual(('Minor 6th'), C4.interval(Gs4, True)), self.assertEqual(('Minor 6th'), Gs4.interval(C4, True))),        # Minor 6th (m6)
        (self.assertEqual(('Major 6th'), C4.interval(A4, True)), self.assertEqual(('Major 6th'), A4.interval(C4, True))),          # Major 6th (M6)
        (self.assertEqual(('Minor 7th'), C4.interval(As4, True)), self.assertEqual(('Minor 7th'), As4.interval(C4, True))),        # Minor 7th (m7)
        (self.assertEqual(('Major 7th'), C4.interval(B4, True)), self.assertEqual(('Major 7th'), B4.interval(C4, True))),          # Major 7th (M7)
        (self.assertEqual(('Octave'), C4.interval(C5, True)), self.assertEqual(('Octave'), C5.interval(C4, True))),                # Octave (P8)
        (self.assertEqual(('Minor 9th'), C4.interval(Cs5, True)), self.assertEqual(('Minor 9th'), Cs5.interval(C4, True))),        # Minor 9th (m9)
        (self.assertEqual(('Major 9th'), C4.interval(D5, True)), self.assertEqual(('Major 9th'), D5.interval(C4, True))),          # Major 9th (M9)
        (self.assertEqual(('Minor 10th'), C4.interval(Ds5, True)), self.assertEqual(('Minor 10th'), Ds5.interval(C4, True))),      # Minor 10th (m10)
        (self.assertEqual(('Major 10th'), C4.interval(E5, True)), self.assertEqual(('Major 10th'), E5.interval(C4, True))),        # Major 10th (M10)
        (self.assertEqual(('Perfect 11th'), C4.interval(F5, True)), self.assertEqual(('Perfect 11th'), F5.interval(C4, True))),    # Perfect 11th (P11)
        (self.assertEqual(('Tritave'), C4.interval(Fs5, True)), self.assertEqual(('Tritave'), Fs5.interval(C4, True))),            # Tritave (P12)
        (self.assertEqual(('Double Octave'), C4.interval(G5, True)), self.assertEqual(('Double Octave'), G5.interval(C4, True))),  # Double Octave (P13)
        (self.assertEqual(('Minor 14th'), C4.interval(Gs5, True)), self.assertEqual(('Minor 14th'), Gs5.interval(C4, True))),      # Minor 14th (m14)
        (self.assertEqual(('Major 14th'), C4.interval(A5, True)), self.assertEqual(('Major 14th'), A5.interval(C4, True))),        # Major 14th (M14)
        (self.assertEqual(('Minor 15th'), C4.interval(As5, True)), self.assertEqual(('Minor 15th'), As5.interval(C4, True))),      # Minor 15th (m15)
        (self.assertEqual(('Major 15th'), C4.interval(B5, True)), self.assertEqual(('Major 15th'), B5.interval(C4, True)))         # Major 15th (M15)

        self.assertEqual(3, A3.interval(C4))
        self.assertEqual(-3, C4.interval(A3))
        self.assertEqual(9, C4.interval(A4))
        self.assertEqual(-9, A4.interval(C4))

        self.assertEqual(10, D3.interval(C4))
        self.assertEqual(-10, C4.interval(D3))
        self.assertEqual(14, C4.interval(D5))
        self.assertEqual(-14, D5.interval(C4))

    def test_interval_direction(self):
        # Test cases for interval_direction
        _, _, _, octave_4, octave_5, _, _ = piano()
        # C1, Cs1, Db1, D1, Ds1, Eb1, E1, F1, Fs1, Gb1, G1, Gs1, Ab1, A1, As1, Bb1, B1 = octave_1
        # C2, Cs2, Db2, D2, Ds2, Eb2, E2, F2, Fs2, Gb2, G2, Gs2, Ab2, A2, As2, Bb2, B2 = octave_2
        # C3, Cs3, Db3, D3, Ds3, Eb3, E3, F3, Fs3, Gb3, G3, Gs3, Ab3, A3, As3, Bb3, B3 = octave_3
        C4, Cs4, Db4, D4, Ds4, Eb4, E4, F4, Fs4, Gb4, G4, Gs4, Ab4, A4, As4, Bb4, B4 = octave_4
        C5, Cs5, Db5, D5, Ds5, Eb5, E5, F5, Fs5, Gb5, G5, Gs5, Ab5, A5, As5, Bb5, B5 = octave_5
        # C6, Cs6, Db6, D6, Ds6, Eb6, E6, F6, Fs6, Gb6, G6, Gs6, Ab6, A6, As6, Bb6, B6 = octave_6
        # C7, Cs7, Db7, D7, Ds7, Eb7, E7, F7, Fs7, Gb7, G7, Gs7, Ab7, A7, As7, Bb7, B7 = octave_7

        # Unison
        self.assertEqual('Same', C4.interval_direction(C4))
        self.assertEqual('Same', Ds4.interval_direction(Ds4))
        self.assertEqual('Same', E4.interval_direction(E4))

        # Minor 2nd
        self.assertEqual('Up', C4.interval_direction(Cs4))
        self.assertEqual('Down', D4.interval_direction(Cs4))

        # Perfect 5th
        self.assertEqual('Up', Gs4.interval_direction(A4))
        self.assertEqual('Down', A4.interval_direction(Gs4))
    
    def test_scale(self):
        _, _, _, octave_4, octave_5, _, _ = piano()
        C4, Cs4, Db4, D4, Ds4, Eb4, E4, F4, Fs4, Gb4, G4, Gs4, Ab4, A4, As4, Bb4, B4 = octave_4
        C5, Cs5, Db5, D5, Ds5, Eb5, E5, F5, Fs5, Gb5, G5, Gs5, Ab5, A5, As5, Bb5, B5 = octave_5

        # Ionian mode (Major)
        self.assertEqual([C4, D4, E4, F4, G4, A4, B4, C5], C4.scale('Ionian'))

        # Dorian mode
        self.assertEqual([C4, D4, Eb4, F4, G4, A4, Bb4, C5], C4.scale('Dorian'))

        # Phrygian mode
        self.assertEqual([C4, Db4, Eb4, F4, G4, Ab4, Bb4, C5], C4.scale('Phrygian'))

        # Lydian mode
        self.assertEqual([C4, D4, E4, Fs4, G4, A4, B4, C5], C4.scale('Lydian'))

        # Mixolydian mode
        self.assertEqual([C4, D4, E4, F4, G4, A4, Bb4, C5], C4.scale('Mixolydian'))

        # Aeolian mode (Natural Minor)
        self.assertEqual([C4, D4, Eb4, F4, G4, Ab4, Bb4, C5], C4.scale('Aeolian'))

        # Locrian mode
        self.assertEqual([C4, Db4, Eb4, F4, Gb4, Ab4, Bb4, C5], C4.scale('Locrian'))

if __name__ == '__main__':
    unittest.main()
