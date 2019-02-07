from sklearn.datasets import load_digits
mnist = load_digits()
print(mnist.data.shape)

import matplotlib.pyplot as plt
plt.gray()
plt.matshow(mnist.images[0])
plt.show()
print(mnist.images[0])

print(mnist.data[0])
print(mnist.target)