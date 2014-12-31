import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr

gridSize = 150
colors = 3
iterations = 1500000
grids = {}
grid = np.random.random_integers(1-0.5, colors-0.5, size = (gridSize, gridSize))

randChoice = random.choice
randInt = random.randint

def randomNeighbour(x,y):
	x = randChoice([x - 1, x, x + 1])
	y = randChoice([y - 1, y, y + 1])
	if x == -1:
		x = gridSize-1
	if x == gridSize:
		x = 0
	if y == -1:
		y = gridSize-1
	if y == gridSize:
		y = 0
	return (x, y)

def changeCell(array):
	x = randInt(0, len(array) - 1)
	y = randInt(0, len(array) - 1)
	neighbour = randomNeighbour(x, y)
	array[x, y] = array[neighbour[0], neighbour[1]]

index = 1
for i in range(iterations):
	grids[index] = grid
	index += 1
	changeCell(grid)

fig, ax = plt.subplots()
matrix = ax.matshow(grid, cmap=plt.cm.CMRmap, vmin=0, vmax=colors)
plt.show()
