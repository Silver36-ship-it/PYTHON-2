class Messages:
    def show_menu(self):
        while True:
            print("""
                1. Write Message
                2. Inbox
                3. Outbox
                4. Picture Message
                5. Templates
                6. Smileys
                7. Message settings
                8. Info service
                9. Voice mailbox number
                10. Service command editor
                """)
            user_input = input("Select an option: ")
            match user_input:
                case "1":
                    print("Write Message")
                case "2":
                    print("Inbox")
                case "3":
                    print("Outbox")
                case "4":
                    print("Picture Message")
                case "5":
                    print("Templates")
                case "6":
                    print("Smileys")
                case "7":
                    print(self.message_settings())
                case "8":
                    print("Info service")
                case "9":
                    print("Voice mailbox number")
                case "10":
                    print("Service command editor")
                case _:
                    print("Invalid option")
    def message_settings(self):
        while True:
            print("1. Set")
            print("2. Common")
            print("0. Go back")
            user_input = input("Select an option: ")
            match user_input:
                case "1":
                    print(self.set_menu())
                case "2":
                    print(self.common_menu())
                case "0":
                    break
                case _:
                    print("Invalid option")
    def set_menu(self):
        while True:
            print("1. Message centre number")
            print("2. Messages sent as")
            print("3. Message validity")
            user_input = input("Select an option: ")
            match user_input:
                    case "1":
                        print("Message centre number")
                    case "2":
                        print("Messages sent as")
                    case "3":
                        print("Message validity")
                    case "0":
                        break
                    case _:
                        print("Invalid option")
    def common_menu(self):
        while True:
            print("1. Delivery reports")
            print("2. Reply via same centre")
            print("3. Character support")
            user_input3 = input("Select an option: ")
            match user_input3:
                case "1":
                        print("Delivery reports")
                case "2":
                        print("Reply via same centre")
                case "3":
                        print("Character support")
                case "0":
                    break
                case _:
                    print("Invalid option")

