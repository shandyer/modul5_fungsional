import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([2, 9, 4, 8])

# Membuat plot untuk tiga garis dengan corak garis yang berbeda
plt.plot(y1, label='Garis 1', linestyle='-', color='#00ffcc')  
plt.plot(y2, label='Garis 2', linestyle='--', color='#d6a3ff')
plt.plot(y3, label='Garis 3', linestyle='-.', marker='o', color='cyan')  

# Menambahkan judul dan label sumbu
plt.title('Plot Tiga Garis')
plt.xlabel('Nilai x')
plt.ylabel('Nilai y')

# Menambahkan keterangan (legend)
plt.legend()

# Menampilkan plot
plt.show()
