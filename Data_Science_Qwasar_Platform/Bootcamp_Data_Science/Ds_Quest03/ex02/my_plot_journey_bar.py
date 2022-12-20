import matplotlib.pyplot as plt

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]
# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

plt.bar(left, height, tick_label = tick_label, width = 0.8, color = ['red', 'green'])

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My bar chart!')

plt.show()
plt.savefig('my_plot_journey_bar.png')