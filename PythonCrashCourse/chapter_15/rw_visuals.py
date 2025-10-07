import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values,rw.y_values, s = 15, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none')
    plt.show()


    keep_running = input("Should you keep running? y/n")
    if keep_running.lower() == 'n':
        break