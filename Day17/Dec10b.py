import matplotlib.pyplot as plt
import numpy as np
"""
x = [1,2,3,4,5,6,7,8,9]
y = [1,3,5,2,4,6,8,7,3]
plt.plot(x,y)   #tidak langsung tampil kalau di VSCode
plt.show()
"""
#Untuk Save
x = np.array(range(1,10))
y = x ** 2
z = x ** 3
plt.plot(x, x, x, y, x, z)
plt.title("Testing 3")
plt.xlabel("Nilai X")
plt.ylabel("Nilai X/Y/Z")
plt.grid(True)
plt.legend(["Linier", "Kuadrat", "Pangkat 3"])
plt.savefig("myChart.png")
plt.show()