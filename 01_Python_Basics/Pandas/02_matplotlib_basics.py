"""import matplotlib.pyplot as plt

# 1. Line Chart
#--------------

x = [10, 20, 30, 40]
y = [20, 25, 35, 55]

plt.plot(x, y)
plt.title("Line Chart")
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")
plt.show()

# 2. Bar Chart
#-------------
x1 = ['Thur', 'Fri', 'Sat', 'Sun']
y1 = [170, 120, 250, 190]

plt.bar(x1, y1)
plt.title("Bar Chart")
plt.xlabel("Day")
plt.ylabel("Total Bill")
plt.show()

# 3. Histogram
#-------------
x = [7, 8, 9, 10, 10, 12, 12, 12, 13, 14, 14, 15, 16, 16, 17, 18, 18, 19, 20, 20,
     21, 22, 23, 24, 25, 25, 26, 28, 30, 32, 35, 36, 38, 40, 42, 44, 48, 50]

plt.hist(x, bins=10, color='steelblue')
plt.title("Histogram")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
#----------------
x = [10, 15, 20, 25, 30]
y = [12, 18, 25, 28, 35]

plt.scatter(x, y)

plt.title("Scatter Plot")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()

# 5. Pie Chart
#-------------
cars = ['AUDI', 'BMW', 'FORD','TESLA', 'JAGUAR',]
data = [23, 10, 35, 15, 12]

plt.pie(data, labels=cars, autopct='%1.1f%%')
plt.title(" Pie Chart")
plt.show()

# 6. Box Plot
#------------
data = [ [10, 12, 14, 15, 18, 20, 22],
         [8, 9, 11, 13, 17, 19, 21],
         [14, 16, 18, 20, 23, 25, 27] ]

plt.boxplot(data)
plt.xlabel("Groups")
plt.ylabel("Values")
plt.title("Box Plot")
plt.show()

# 7. Heatmap
#-----------
import numpy as np

np.random.seed(0)
data = np.random.rand(10, 10)

plt.imshow(data, cmap='viridis', interpolation='nearest')

plt.colorbar()
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Heatmap')
plt.show()"""