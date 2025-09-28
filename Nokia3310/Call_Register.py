class CallRegister:
    def call_register_menu(self):
        while True:
            print("1. Missed calls")
            print("2. Received calls")
            print("3. Dialled numbers")
            print("4. Erase recent call lists")
            print("5. Show call duration")
            print("6. Show call costs")
            print("7. Call cost settings")
            print("8. Prepaid credit")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Missed calls")
                case "2":
                    print("Received calls")
                case "3":
                    print("Dialled numbers")
                case "4":
                    print("Erase recent call lists")
                case "5":
                    print(self.show_call_duration())
                case "6":
                    print(self.show_call_costs())
                case "7":
                    print(self.call_cost_settings())
                case "8":
                    print("Prepaid credit")
                case "0":
                    break
                case _:
                    print("Invalid input")

    def show_call_duration(self):
        while True:
            print("1. Last call duration")
            print("2. All calls' duration")
            print("3. Received calls' duration")
            print("4. Dialled calls' duration")
            print("5. Clear timer")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Last call duration")
                case "2":
                    print("All calls' duration")
                case "3":
                    print("Received calls' duration")
                case "4":
                    print("Dialled calls' duration")
                case "5":
                    print("Clear timer")
                case "0":
                    break
                case _:
                    print("Invalid input")

    def show_call_costs(self):
        while True:
            print("1. Last call costs")
            print("2. All calls' costs")
            print("3. Clear counters")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Last call costs")
                case "2":
                    print("All calls' costs")
                case "3":
                    print("Clear counters")
                case "0":
                    break
                case _:
                    print("Invalid input")

    def call_cost_settings(self):
        while True:
            print("1. Call cost limit")
            print("2. Show costs in")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Call cost limit")
                case "2":
                    print("Show costs in")
                case "0":
                    break
                case _:
                    print("Invalid input")