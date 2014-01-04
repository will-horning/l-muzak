import json
from collections import namedtuple
from notation import note_freqs
from pippi import dsp

OUTPATH = 'out'
NoteSpec = namedtuple('NoteSpec', ['freq', 'env', 'amp', 'duration'])

"""
A: [[A, B], [A, B, A]]
"""

def load_grammar(path):
    g = {}
    with open(path, 'r') as f:
        raw_grammar = json.loads(f.read())
        for k, v in raw_grammar.iteritems():
            g[parse_note_spec(k)] = [parse_note_spec(s) for s in v]
    return g

def lsystem_gen(grammar, n_generations, start_string):
    seq = start_string
    for i in range(n_generations):
        next = []
        for k in seq: 
            try: next += grammar[k]
            except KeyError: next += [k]
        seq = next
    for ns in seq:
        if '|' in ns.freq:
            notes = [dsp.env(dsp.tone(dsp.mstf(ns.duration), note_freqs[f], amp=ns.amp), ns.env) for f in ns.freq.split('|')]
            yield dsp.mix(notes)
        else:
            yield dsp.env(dsp.tone(dsp.mstf(ns.duration), note_freqs[ns.freq], amp=ns.amp), ns.env)

def parse_note_spec(ns_str):
    rawvals = [s.strip() for s in ns_str.strip().split(',')]
    return NoteSpec(rawvals[0], rawvals[1], float(rawvals[2]), int(rawvals[3]))

def create_sequence(note_specs):
    return "".join([dsp.env(dsp.tone(dsp.stf(ns.duration), ns.freq, amp=ns.amp), ns.env) for ns in note_specs])

