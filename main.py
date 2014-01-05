import json, random
from notation import note_freqs
from itertools import izip
from pyo import *

class LSystem():
    def __init__(self):
        self.lex = {"A": self.A, "B": self.B, "C": self.C}
        self.grammar = {"A": [["A B", 0.5], ["A C", 0.5]], "B" : [["B", 1.0]]}

    def play(self, n_generations, start_string):
        s = Server().boot()
        s.start()
        for i in xrange(n_generations):
            start_string = " ".join([self.w_choice(self.grammar.get(k, [[k,1.0]])) for k in start_string.split()])
        print start_string
        for symbol in start_string.split():
            self.lex[symbol]()

        time.sleep(0.5)
        s.stop()
        time.sleep(0.2)
        s.shutdown()

    def w_choice(self, a):
        r = random.uniform(0.0, sum(p[1] for p in a))
        t = 0
        for e, w in a:
            if r <= t + w: return e
            t += w

    def A(self):
        t = CosTable([(0,0), (100,1), (1000,.25), (8191,0)])
        a = Osc(table=t, freq=1, mul=.25)
        b = SineLoop(freq=[note_freqs['A4'],note_freqs['A4']], feedback=0.05, mul=a).out()
        time.sleep(1.0)
        b.stop()
        time.sleep(0.1)

    def B(self):    
        t = CosTable([(0,0), (50,1), (1000,.25), (8191,0)])
        a = Osc(table=t, freq=0.5, mul=.25)
        b = SineLoop(freq=[note_freqs['Bb4'],note_freqs['Bb4']], feedback=0.05, mul=a).out()
        time.sleep(2.0)
        b.stop()
        time.sleep(0.1)

    def C(self):
        t = CosTable([(0,0), (100,1), (1000,.25), (8191,0)])
        a = Osc(table=t, freq=2, mul=.25)
        b = SineLoop(freq=[note_freqs['C4'],note_freqs['C4']], feedback=0.05, mul=a).out()
        time.sleep(0.5)
        b.stop()
        time.sleep(0.1)


