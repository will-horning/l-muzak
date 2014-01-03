from collections import namedtuple
from notation import note_freqs
from pippi import dsp

OUTPATH = 'out'

NoteSpec = namedtuple('NoteSpec', ['freq', 'env', 'amp', 'duration'])

def create_sequence(note_specs):
    print note_specs
    print type(note_specs[0].duration)
    return "".join([dsp.env(dsp.tone(dsp.stf(ns.duration), ns.freq, amp=ns.amp), ns.env) for ns in note_specs])

nss = []
nss.append(NoteSpec(note_freqs['A4'], 'sine', 0.3, 1))
nss.append(NoteSpec(note_freqs['B4'], 'sine', 0.3, 1))
nss.append(NoteSpec(note_freqs['C4'], 'sine', 0.3, 1))
nss.append(NoteSpec(note_freqs['D4'], 'sine', 0.3, 1))

dsp.write(create_sequence(nss), OUTPATH)
