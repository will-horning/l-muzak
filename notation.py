import math
from pippi import dsp
from collections import deque

def nth_note_freq(n):
    return 440 * 2**((n - 40) / 12)

note_freqs = {}
base_note_names = deque(['A', 'Bb', 'B', 'C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab'])
octave = 0
for i in xrange(1, 89):
    if base_note_names[0] == 'C': octave += 1
    note_name = base_note_names[0] + str(octave)    
    note_freqs[note_name] = 440.0 * math.pow(math.pow(2, 1/12.0), i - 49)
    base_note_names.rotate(-1)

