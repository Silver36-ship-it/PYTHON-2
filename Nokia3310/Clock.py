class Clock:
    def clock_menu(self):
        while True:
            print("1. Alarm clock")
            print("2. Clock settings")
            print("3. Date settings")
            print("4. Stopwatch")
            print("5. Countdown timer")
            print("6. Auto update of date and time")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Alarm clock")
                case "2":
                    print("Clock settings")
                case "3":
                    print("Date settings")
                case "4":
                    print("Stopwatch")
                case "5":
                    print("Countdown timer")
                case "6":
                    print("Auto update of date and time")
                case "0":
                    print("Exiting....")
                    break
                case _:
                    print("Invalid input")