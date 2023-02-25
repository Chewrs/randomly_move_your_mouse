import pyautogui  # to install type "pip3 install pyautogui" on your terminal
import random
import time


apk_length = float(input("Input how long do you want to AFK (min)"))  # user input
apk_time = int((apk_length * 60) / 1.43)  # change from minute to times of loop

start = time.time()  # start of timer

move = 0  # count for the move
right = 0  # count for right click

for i in range(apk_time):
    move += 1
    print("move", move)
    # random  x and the range is depend on your screen
    x = random.randint(100, 1000)
    # random y and the range is depend on your sreen
    y = random.randint(100, 1000)
    pyautogui.moveTo(x, y, 1)  # move the cursor to the point by x and y

    # random for the click 1 is click other is do nothing so it's 1/10
    # we don't have the left click because it will be annoying or making the problem.
    click = random.randint(1, 10)
    if click == 1:
        right += 1
        pyautogui.rightClick()  # auto right click
        print("click")


end = time.time()  # end of timer
# calculate time spent and convert from second to minute
afk_long = (end - start) / 60


# print the over all summary
print()
print("DONE")
print("%.2f" % afk_long, "minutes")  # print the time spent
print(
    "move = ", move, "times," "right click = ", right, "times"
)  # print how many time that move and click
