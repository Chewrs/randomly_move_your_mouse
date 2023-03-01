import pyautogui  # to install type "pip3 install pyautogui" on your terminal
import random
import time
import json


def covert_input():
    input_error_check = True
    while input_error_check == True:

        input_lenght = str(input("Input how long you want to AFK (Hour,Minute)"))

        list_lenght = input_lenght.split(",")

        try:
            hour_lenght = float(list_lenght[0])
            min_lenght = float(list_lenght[1])
            input_error_check = False
        except:
            print()
            print("there an error")
            print("make sure to input only the number")
            print("and with Hour,Minute format")
            print("for example 1,30 ")
            print()

    global afk_times
    afk_times = ((hour_lenght * 3600) + (min_lenght * 60)) / 1.43


def json_setting_open_file():
    with open("setting.json", "r") as f:
        data_json = json.load(f)

        global first_x
        global second_x

        global first_y
        global second_y

        first_x = data_json["setting"]["x"][0]
        second_x = data_json["setting"]["x"][1]

        first_y = data_json["setting"]["y"][0]
        second_y = data_json["setting"]["y"][1]


def radom_point():
    global move
    global right
    global start
    global end
    start = time.perf_counter()  # start of timer
    right = 0
    move = 0
    for i in range(int(afk_times)):
        move += 1
        print("move", move)
        # random  x and the range is depend on your screen
        x = random.randint(first_x, second_x)
        # random y and the range is depend on your sreen
        y = random.randint(first_y, second_y)
        pyautogui.moveTo(x, y, 1)  # move the cursor to the point by x and y

        # random for the click 1 is click other is do nothing so it's 1/10
        # we don't have the left click because it will be annoying or making the problem.
        click = random.randint(1, 10)
        if click == 1:
            pyautogui.rightClick()  # auto right click
            print("click")
            right += 1
    print(move, right)
    end = time.perf_counter()


def covert_sec():
    # end of timer
    # calculate time spent and convert from second to minute
    afk_long = end - start
    convert_afk_long = time.strftime(
        "%H hours %M minutes %S second", time.gmtime(afk_long)
    )
    print(convert_afk_long)


def print_summry():
    # print the over all summary
    print()
    print("DONE")
    covert_sec()
    print(
        "move = ", move, "times," "right click = ", right, "times"
    )  # print how many time that move and click


covert_input()
json_setting_open_file()
radom_point()
print_summry()
