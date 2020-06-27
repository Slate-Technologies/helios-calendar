import calendar
import os

while True:
    try:
        os.system("clear")
    except OSError:
        os.system("cls")

    print(" ____________                    _                                                   _")
    print("|  __________|                  | |                                                 | |")
    print("| |                    _____    | |                                                 | |        ______")
    print("| |                   |___  |   | |       ____________    _____________             | |       |____  |    _")
    print("| |               ________| |   | |      |  ________  |  |  _________  |    ________| |    ________| |   | |______")
    print("| |              |  ______  |   | |      | |________| |  | |         | |   |  ______  |   |  ______  |   |  ______|")
    print("| |              | |      | |   | |      |  __________|  | |         | |   | |      | |   | |      | |   | |")
    print("| |__________    | |______| |   | |__    | |__________   | |         | |   | |______| |   | |______| |   | |")
    print("|____________|   |__________|   |____|   |____________|  |_|         |_|   |__________|   |__________|   |_|")

    yy = int(input("Please enter the year you wish to view: \n"))
    mm = int(input("Please enter the month (in digits) you wish to view: \n"))

    print(calendar.month(yy, mm))

    opt = int(input("Do you want to view another calendar? \n1. Yes \n2. No \n"))

    if opt==1:
        continue

exit()
