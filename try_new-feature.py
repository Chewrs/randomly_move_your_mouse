import time


input_lenght = str(input("Input how long you want to AFK (Hour,Minute)"))


def covert_input(input_lenght):
    print(input_lenght)
    try:
        list_lenght = input_lenght.split(",")
    except:
        print("input with Hour,Minute format")
        print("for example 1,30 ")
    print(list_lenght)
    try:
        hour_lenght = float(list_lenght[0])
        min_lenght = float(list_lenght[1])
    except:
        print("there an error")
        print()
        print("make sure to input only the number")
        print("and with Hour,Minute format")

        print("for example 1,30 ")
        return
    global apk_lenght
    apk_lenght = ((hour_lenght * 3600) + (min_lenght * 60)) / 1.43
    print(apk_lenght)
    for i in range(int(apk_lenght)):
        print("hello", i)
    print(apk_lenght)


covert_input(input_lenght)
for i in range(int(apk_lenght)):
    print(i)


def covert_sec():
    afk_long = 120
    convert_afk_long = time.strftime(
        "%H hours %M minutes %S second", time.gmtime(afk_long)
    )
    print(convert_afk_long)
