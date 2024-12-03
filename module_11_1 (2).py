import matplotlib.pyplot as plt
import numpy as np

# 1. Линейный график
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.title('Линейный график')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# 2. Гистограмма
data = np.random.randn(1000)
plt.hist(data, bins=30, color='skyblue', alpha=0.7)
plt.title('Гистограмма распределения')
plt.show()

# 3. Круговая диаграмма
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Круговая диаграмма')
plt.show()
