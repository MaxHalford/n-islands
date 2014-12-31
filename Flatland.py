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
	x = randChoice([x, max(0,x-1), min(gridSize - 1, x + 1)])
	y = randChoice([y, max(0,y-1), min(gridSize - 1, y + 1)])
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
