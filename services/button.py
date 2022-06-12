class Button():
	def __init__(self, pos, textInput, font, baseColor, hoverColor):
		self.x = pos[0]
		self.y = pos[1]
		self.font = font
		self.baseColor, self.hoverColor = baseColor, hoverColor
		self.textInput = textInput
		self.text = self.font.render(self.textInput, True, self.baseColor)
		self.textRect = self.text.get_rect(center=(self.x, self.y))

	def update(self, screen):
		screen.blit(self.text, (self.x, self.y))

	def changeColor(self, newColor):
		self.text = self.font.render(self.textInput, True, newColor)