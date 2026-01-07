
for num in range(1,11):
    if num == 7:
        print("遇到7，跳出循环")
        break
    elif num > 5:
        print(f"{num}大于5")
        num += 1
    else:
        print(f"{num}小于等于5")
        num += 1


print("=====================================")

import random
target = random.randint(1,20)
while True:
    guess = int(input("请输入你猜的数字："))
    if guess > target:
        print("猜大了")
    elif guess < target:
        print("猜小了")
    else:
        print("恭喜猜对了！")
        break
