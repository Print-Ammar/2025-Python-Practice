import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()

    fig, ax = plt.subplots()
    ax.scatter(rw.x_values,rw.y_values, s = 15)
    plt.show()


    keep_running = input("Should you keep running? y/n")
    if keep_running.lower() == 'n':
        break