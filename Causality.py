from pygame import *
from State import *
from cmath import *

class Causality(State):

	def setup(self):
		self.c = -5
		self.dc = .01
		self.roc_color = (255, 0, 255)
		self.not_roc_color = (255, 255, 255)
		self.text_color = (0, 0, 0)
		self.pole1_color = (0, 255, 255)
		self.pole2_color = (255, 255, 0)
		self.axies_color = (0, 0, 0)
		self.unit_circle_color = (0, 0, 0)
	
	def draw_pole(self, color, pole):
		x = int(400 + 100*pole.real)
		y = int(300 + 100*pole.imag)
		draw.line(screen, color, (x - 7, y - 7), (x + 7, y + 7), 3)
		draw.line(screen, color, (x - 7, y + 7), (x + 7, y - 7), 3)

	def draw_causal(self, radius):
		screen.fill(self.roc_color)
		draw.circle(screen, self.not_roc_color, origin, int(100*radius), 0)
		screen.blit(myfont.render("Causal", 1, self.text_color), (0, 0))

	def draw_anticausal(self, radius):
		screen.fill(self.not_roc_color)
		draw.circle(screen, self.roc_color, origin, int(100*radius), 0)
		screen.blit(myfont.render("Anticausal", 1, self.text_color), (0, 0))

	def draw_noncausal(self, radius1, radius2):
		screen.fill(self.not_roc_color)
		draw.circle(screen, self.roc_color, origin, int(100*radius1), 0)
		draw.circle(screen, self.not_roc_color, origin, int(100*radius2), 0)
		screen.blit(myfont.render("Noncausal", 1, self.text_color), (0, 0))

	def draw_axies(self):
		draw.line(screen, self.axies_color, (0, 300), (800, 300))
		draw.line(screen, self.axies_color, (400, 0), (400, 600))

	def draw_unit_circle(self):
		draw.circle(screen, self.unit_circle_color, origin, 100, 1)

	def mag(self, complex_num):
		return polar(complex_num)[0]

	def draw_c(self):
		screen.blit(myfont.render(str(self.c), 1, self.text_color), (0, 30))

	def draw(self):
		pole1 = (1 + sqrt(1 - 4*self.c))/2
		pole2 = (1 - sqrt(1 - 4*self.c))/2
		#detirmine causality based on the magnitudes of the poles
		if self.mag(pole1) < 1 and self.mag(pole2) < 1:
			self.draw_causal(max(self.mag(pole1), self.mag(pole2)))
		elif self.mag(pole1) > 1 and self.mag(pole2) > 1:
			self.draw_anticausal(min(self.mag(pole1), self.mag(pole2)))
		else:
			self.draw_noncausal(max(self.mag(pole1), self.mag(pole2)), min(self.mag(pole1), self.mag(pole2)))
		self.draw_c()
		self.draw_axies()
		self.draw_unit_circle()
		self.draw_pole(self.pole1_color, pole1)
		self.draw_pole(self.pole2_color, pole2)
		display.update()

	def update(self):
		self.c += self.dc
		if self.c > 2:
			self.c = -3

if __name__ == '__main__':
	init()
	myfont = font.SysFont("monospace", 30)
	screen = display.set_mode((800, 600))
	origin = (400, 300)
	new_game = Causality(screen)