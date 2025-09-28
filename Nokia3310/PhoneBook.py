class PhoneBook:
    def phoneBook_menu(self):
        while True:
            print("1. Search")
            print("2. Service Nos")
            print("3. Add Name")
            print("4. Erase")
            print("5. Edit")
            print("6. Assign Tone")
            print("7. Send Business Card")
            print("8. Options")
            print("9. Speed Dials")
            print("10.Voice Tags")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Search")
                case "2":
                    print("Service Nos")
                case "3":
                    print("Add Name")
                case "4":
                    print("Erase")
                case "5":
                    print("Edit")
                case "6":
                    print("Assign Tone")
                case "7":
                    print("Send Business Card")
                case "8":
                    print(self.options_menu())
                case "9":
                    print("Speed Dials")
                case "10":
                    print("Voice Tags")
                case "0":
                    break
                case _:
                    print("Invalid option")
    def options_menu(self):
        while True:
            print("1. Type of view")
            print("2. Memory status")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Type of view")
                case "2":
                    print("Memory status")
                case "0":
                    break
                case _:
                    print("Invalid option")