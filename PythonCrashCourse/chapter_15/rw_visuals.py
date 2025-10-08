import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    fig, ax = plt.subplots(figsize = (15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values,rw.y_values, linewidth = 3)

    ax.plot(0, 0, color='green',)
    ax.plot(rw.x_values[-1], rw.y_values[-1], color='blue')

    
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()


    keep_running = input("Should you keep running? y/n")
    if keep_running.lower() == 'n':
        break  