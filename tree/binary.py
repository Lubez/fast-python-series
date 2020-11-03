#!/usr/bin/env python3

import pygame

width = 700
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("Binary Tree")

BLACK = (0, 0, 0) # 0-255
GRAY = (150, 150, 150)

class Node():
	def __init__(self, x, y, radius, color, left, right):
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color 
		self.left = left
		self.right = right

	def getLoc(self):
		return (self.x, self.y)

	def getColor(self):
		return self.color

	def getRadius(self):
		return self.radius

	def getLeft(self):
		return self.left

	def getRight(self):
		return self.right

	def setLeft(self, left):
		self.left = left

	def setRight(self, right):
		self.right = right

def create_nodes(width, levels):
	nodes = []
	finalTot = 2 ** (levels - 1)
	diameter = (width // finalTot) / 2
	radius = diameter // 2
	for lvl in range(levels):
		totlvl = 2 ** lvl
		start = (width // totlvl) / 2
		for node in range(totlvl):
				nodes.append(Node(start + ((width // totlvl) * node), (width // levels) * lvl + (width // levels / 2), radius, BLACK, None, None))

	for i in range(len(nodes)):
		if 2 * i + 1 < len(nodes) and nodes[2 * i + 1]:
			nodes[i].setLeft(nodes[2 * i + 1])
		if 2 * i + 2 < len(nodes) and nodes[2 * i + 2]:
			nodes[i].setRight(nodes[2 * i + 2])

	return nodes

def draw_circles(win, width, levels, nodes):
	for node in nodes:
		pygame.draw.circle(win, node.getColor(), node.getLoc(), node.getRadius())

def draw_lines(win, nodes):
	for node in nodes:
		if node.getLeft() != None and node.getRight() != None:
			pygame.draw.line(win, BLACK, node.getLoc(), node.getLeft().getLoc(), 5)
			pygame.draw.line(win, BLACK, node.getLoc(), node.getRight().getLoc(), 5)

def draw(win, width, levels, nodes):
	draw_lines(win, nodes)
	draw_circles(win, width, levels, nodes)
	pygame.display.update()

def main(win, width):
	pygame.init()
	win.fill(GRAY)
	pygame.display.update()
	levels = 5
	nodes = create_nodes(width, levels)
	while True:
		draw(win, width, levels, nodes)

main(win, width)
