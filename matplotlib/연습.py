import matplotlib.pyplot as plt

plt.style.available

x = list(range(1, 101))
squares = [i ** 2 for i in x]

fig, ax = plt.subplots()
scatter = ax.scatter(x, squares, c=squares, cmap=plt.cm.Blues)

ax.set_title('square')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.colorbar(scatter)

ax.ticklabel_format(style='plain')
plt.show()


