import matplotlib.pyplot as plt

ages = [2, 5, 70, 40, 30, 45, 50, 45, 43, 40, 44, 60, 7, 13, 57, 18, 90, 77, 32, 21, 20, 40]

range = (0, 100)
bins = 10

plt.hist(ages, bins, range, color = 'green', rwidth = 0.8)

plt.xlabel('age')
plt.ylabel('No. of people')
plt.title('My histogram')

plt.show()
plt.savefig('my_plot_journey_histogram.png')