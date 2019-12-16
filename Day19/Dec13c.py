import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

fig = plt.figure()
p = plt.subplot(111, projection= "3d")
data = range(11)
x = np.array(data)

p.plot_wireframe(x, x, x.reshape(1,-1))

p.set_xlabel("sumbu X")
p.set_ylabel("sumbu Y")
p.set_zlabel("sumbu Z")

plt.show()