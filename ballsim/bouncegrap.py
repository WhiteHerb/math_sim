import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ax=plt.axes()

print('''
공이 튀어오르는 각 횟수당 높이를 수열을 통해 구하고 그래프로 나타내 줍니다
''')

ballhight = float(input("처음 공의 높이 지정>>> "))
ballbounce = float(input("튀어오르는 높이 지정>> "))
bouncelate = float(ballbounce/ballhight)
ballhights = []

for i in range(80) :
    ballhights.append(ballhight)
    ballhight = ballhight - (1-bouncelate)*ballhight


b = []
for i in range(len(ballhights)):
    b.append(i)


ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(1))
plt.text(b[-1],ballhights[-1],ballhights[-1])
plt.plot(b,ballhights,c='red')
plt.scatter(b,ballhights)

# plt.xlim(0,1000)
plt.show()