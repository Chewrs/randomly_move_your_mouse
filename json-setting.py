import json
import pyautogui
import random


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

        print(first_x)  # for debug
        print(second_x)  # for debug
        print(first_y)  # for debug
        print(second_y)  # for debug


def radom_point():
    for i in range(1, 11):
        print("move", i)
        # random  x and the range is depend on your screen
        x = random.randint(first_x, second_x)
        # random y and the range is depend on your sreen
        y = random.randint(first_y, second_y)
        pyautogui.moveTo(x, y, 1)  # move the cursor to the point by x and y


json_setting_open_file()
radom_point()
