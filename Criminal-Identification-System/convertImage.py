import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image
path = PIL.Image.open("1.png")
grayscale_image = path.convert("L")
grayscale_array = np.asarray(grayscale_image)

plt.imshow(grayscale_array, cmap="gray")
