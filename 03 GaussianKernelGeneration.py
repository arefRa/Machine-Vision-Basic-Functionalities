import numpy as np
import math
import matplotlib.pyplot as plt

def get_gauss_kernel(size=3, sigma=1):
    center=size//2
    kernel=np.zeros((size,size))
    for i in range(size):
       for j in range(size):
          diff = np.sqrt((i-center)**2+(j-center)**2)
          kernel[i,j] = np.exp(-(diff**2)/(2*sigma**2))
    return kernel

kernel_size = 5
sigma = 1

kernel = get_gauss_kernel(kernel_size, sigma)
np.set_printoptions(formatter={'float_kind':"{:.2f}".format})

print(kernel)
kernel = np.floor(kernel*255)
kernel = np.int_(kernel)

print(kernel)

# 'viridis', 'plasma', 'inferno', 'magma', 'cividis'
# 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 
# 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
# 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'
# 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
#'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
# 'hot', 'afmhot', 'gist_heat', 'copper'
# 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
# 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'

plt.imshow(kernel, cmap=plt.get_cmap("hot"))
plt.show()