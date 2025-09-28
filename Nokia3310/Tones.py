class Tones:
    def tones_menu(self):
        while True:
            print("1. Ringing tone")
            print("2. Ringing volume")
            print("3. Incoming call alert")
            print("4. Composer")
            print("5. Message alert tone")
            print("6. Keypad tone")
            print("7. Warning and game tone")
            print("8. Vibrating alert")
            print("9. Screen saver")
            print("0. Exit")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Ringing tone")
                case "2":
                    print("Ringing volume")
                case "3":
                    print("Incoming call alert")
                case "4":
                    print("Composer")
                case "5":
                    print("Message alert tone")
                case "6":
                    print("Keypad tone")
                case "7":
                    print("Warning and game tone")
                case "8":
                    print("Vibrating alert")
                case "9":
                    print("Screen saver")
                case "0":
                    print("Exiting.....")
                    break
                case _:
                    print("Invalid input")
