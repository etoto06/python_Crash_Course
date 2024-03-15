import matplotlib.pyplot as plt
import random
#aexs 는 그래프를 그릴 수 있는 영역을 나타낸 개체
import matplotlib.pyplot as plt

x = list(range(1,101))
squares = [i**2 for i in x]

fig, ax = plt.subplots()

ax.plot(x, squares)
ax.set_title('squares')
ax.set_xlabel('X',fontsize=20)

ax.tick_params(labelsize=14)

plt.show()

# # 빈 Axes가 없는 빈 Figure 생성
# fig = plt.figure()

# # 하나의 Axes가 있는 Figure 생성
# fig, ax = plt.subplots()

# # 2x2 그리드 형태의 Axes가 있는 Figure 생성
# fig, axs = plt.subplots(2, 2)

# # 왼쪽에 하나의 Axes가 있고, 오른쪽에 두 개의 Axes가 있는 Figure 생성
# fig, axs = plt.subplot_mosaic([['left', 'right-top'],
#                                ['left', 'right_bottom']])

# # 그림을 화면에 표시
# plt.show()

# data =[random.randint(0,100) for _ in range(1000)]
# ax.hist(data)
# print(data)




# x = [1, 2, 3, 4]
# y = list(zip([1, 4, 2, 3], [2, 3, 4, 6]))
# ax.plot(x, y)  # Plot some data on the axes.
# plt.savefig('plot.png')
# plt.show()