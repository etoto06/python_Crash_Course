import matplotlib.pyplot as plt
import random

# x = list(range(100))
# y = list(range(100,200))

x= [random.randint(0,100) for _ in range(100) ]
y= [random.randint(100,200) for _ in range(100)]

print(x)

a_walks = [5,-5]
b_walks = [5,-5]

a_data,b_data = [],[]
a,b = 0,0
a_data.append(a)
b_data.append(b)

fig, ax = plt.subplots()
ax.plot(x,y)
plt.show()


