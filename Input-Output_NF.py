import time


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

    global apk_lenght
    apk_lenght = ((hour_lenght * 3600) + (min_lenght * 60)) / 1.43
    print(apk_lenght)
    for i in range(int(apk_lenght)):
        print("hello", i)
    print(apk_lenght)


covert_input()


for i in range(int(apk_lenght)):
    print(i)
print(apk_lenght)


def covert_sec():
    afk_long = 120
    convert_afk_long = time.strftime(
        "%H hours %M minutes %S second", time.gmtime(afk_long)
    )
    print(convert_afk_long)


covert_sec()
