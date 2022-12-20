import matplotlib.pyplot as plt

# Values
x = [1,2,3]
y = [2,4,1]

plt.plot(x, y)

plt.xlabel('x - axis')
plt.ylabel('y - axis')

plt.title('My first graph!') 

plt.show()
plt.savefig('my_plot_journey_line.png')