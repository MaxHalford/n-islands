import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as clr
import matplotlib.animation as animation
import random

gridSize = 100
colors = 4

randChoice = random.choice
randInt = random.randint
grid = np.random.random_integers(0.5, colors - 0.5, size = (gridSize, gridSize))

def randomNeighbour(x,y):
	x = randChoice([x, max(0,x-1), min(gridSize - 1, x + 1)])
	y = randChoice([y, max(0,y-1), min(gridSize - 1, y + 1)])
	return (x, y)

def changeCell(array):
	x = randInt(0, len(array) - 1)
	y = randInt(0, len(array) - 1)
	neighbour = randomNeighbour(x, y)
	array[x, y] = array[neighbour[0], neighbour[1]]
	return array

def update(data):
    mat.set_data(data)
    return mat

def dataGen():
    while True:
        yield changeCell(grid)

fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, dataGen, interval = 1, save_count = 50)

plt.show()
