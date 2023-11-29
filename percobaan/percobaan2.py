import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 10])
ypoints = np.array([3, 10, 5])

plt.figure(figsize=(5, 5))

# Plot dengan label sumbu, judul, warna, dan gaya garis
plt.plot(xpoints, ypoints, color='yellow', marker='o', label='Blue stars')

# Batasan sumbu X dan Y
plt.xlim([0, 15])
plt.ylim([0, 15])

# Menambahkan label sumbu
plt.xlabel('DDD')
plt.ylabel('YYY')

# Menambahkan judul
plt.title('Data Penjualan PT.Kipli Jaya')

# Menambahkan legenda
plt.legend()

# Menampilkan plot
plt.show()
