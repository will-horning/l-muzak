import json, random
from collections import namedtuple
from notation import note_freqs
from pippi import dsp
from itertools import izip

NoteSpec = namedtuple('NoteSpec', ['freq', 'env', 'amp', 'duration'])

def weighted_choice(a):
    r = random.uniform(0.0, sum(p[1] for p in a))
    t = 0
    for e, w in a:
        if r <= t + w: return e
        t += w

def load_grammar(path):
    with open(path, 'r') as f:
        raw_grammar = json.loads(f.read())
        lex = {k: parse_note_spec(v) for k, v in raw_grammar['lexicon'].iteritems()}
        return raw_grammar['grammar'], lex
    raise Exception('Failed to load grammar.')

def lsystem_gen(grammar, lexicon, n_generations, start_string):
    for i in xrange(n_generations):
        start_string = "".join([weighted_choice(grammar.get(k, [[k,1]])) for k in start_string])
    for symbol in start_string:
        yield lexicon[symbol]

def parse_note_spec(ns_str):
    ns = NoteSpec(*[s.strip() for s in ns_str.strip().split(',')])
    out = []
    for pitch in ns[0].split("|"):
        out.append(dsp.tone(dsp.mstf(int(ns.duration)), note_freqs[pitch], amp=float(ns.amp)))
    return dsp.mix(out)


