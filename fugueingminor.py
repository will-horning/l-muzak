from main import LSystem
from pyo import *
from notation import note_freqs

class FugueInGMinor(LSystem):
	def __init__(self):
		self.lex = {'A': self.A, 'B': self.B, 'C': self.C, 'D': self.D}
		self.grammar = {'A': [['A B', 0.5], ['A C', 0.5]],
						'B': [['A', 0.75], ['B D', 0.25]]}

	def base_tone2(self, duration, note_name):
		f = note_freqs[note_name]
		t = CosTable([(0,0), (100,1), (1000,.25), (8191,0)])
		a = Osc(table=t, freq=1/duration, mul=.25)
		env = Adsr(attack=duration/10.0, decay=duration/5.0, sustain=0.8, release=0.2, dur=duration, mul=a)
		sin = Sine(freq=[f,f], mul=env).out()
		env.play()
		time.sleep(duration)
		env.stop()
		sin.stop()
		time.sleep(0.1)

	def A(self):
		self.base_tone2(1, 'G3')
		self.base_tone2(0.5, 'D3')
		self.base_tone2(0.5, 'G3')

	def B(self):
		self.base_tone2(1, 'A4')
		self.base_tone2(0.5, 'D3')
		self.base_tone2(0.5, 'A3')

	def C(self):
		self.base_tone2(1, 'Bb4')
		self.base_tone2(0.5, 'A4')
		self.base_tone2(0.5, 'G3')	

	def D(self):
		self.base_tone2(0.5, 'A4')
		self.base_tone2(0.5, 'D3')		
		self.base_tone2(0.5, 'D4')
		self.base_tone2(0.5, 'C4')