class Settings:
    def settings_menu(self):
        while True:
            print("1. Call Settings")
            print("2. Phone settings")
            print("3. Security settings")
            print("4. Restore factory settings")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print(self.call_settings())
                case "2":
                    print(self.phone_settings())
                case "3":
                    print(self.security_settings())
                case "4":
                    print("Restore factory settings")
                case "0":
                    print("Exiting.....")
                    break
                case _:
                    print("Invalid input")

    def call_settings(self):
        while True:
            print("1. Automatic redial")
            print("2. Speed dialling")
            print("3. Call waiting options")
            print("4. Own number setting")
            print("5. Phone line in use")
            print("6. Automatic answer")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Automatic redial")
                case "2":
                    print("Speed dialling")
                case "3":
                    print("Call waiting options")
                case "4":
                    print("Own number setting")
                case "5":
                    print("Phone line in use")
                case "6":
                    print("Automatic answer")
                case "0":
                    print("Exiting.....")
                    break
                case _:
                    print("Invalid input")

    def phone_settings(self):
        while True:
            print("1. Language")
            print("2. Cell info display")
            print("3. Welcome note")
            print("4. Network selection")
            print("5. Lights")
            print("6. Confirm SIM service actions")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("Language")
                case "2":
                    print("Cell info display")
                case "3":
                    print("Welcome note")
                case "4":
                    print("Network selection")
                case "5":
                    print("Lights")
                case "6":
                    print("Confirm SIM service actions")
                case "0":
                    print("Exiting.....")
                    break
                case _:
                    print("Invalid input")

    def security_settings(self):
        while True:
            print("1. PIN Code request")
            print("2. Calling barring service")
            print("3. Fixed dialling")
            print("4. Closed user group")
            print("5. Phone security")
            print("6. Change access codes")
            print("0. Go back")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print("PIN code request")
                case "2":
                    print("Calling barring service")
                case "3":
                    print("Fixed dialling")
                case "4":
                    print("Closed user group")
                case "5":
                    print("Phone security")
                case "6":
                    print("Change access codes")
                case "0":
                    print("Exiting.....")
                    break
                case _:
                    print("Invalid input")


