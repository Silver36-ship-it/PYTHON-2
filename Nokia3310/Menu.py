from Nokia3310.Call_Register import CallRegister
from Nokia3310.Settings import Settings
from Nokia3310.Tones import Tones
from Nokia3310.Clock import Clock
from Nokia3310.Messages import Messages
from Nokia3310.PhoneBook import PhoneBook

class Menu:
    def __init__(self):
        self.phoneBook = PhoneBook()
        self.messages = Messages()
        self.chat = "Chat"
        self.call_register = CallRegister()
        self.tones = Tones()
        self.settings = Settings()
        self.call_divert = "call_divert"
        self.games = "Games"
        self.calculator = "Calculator"
        self.reminder = "Reminder"
        self.clock = Clock()
        self.profiles = "Profiles"
        self.sim_services = "Sim Services"

    def main(self):
        while True:
            print("1. Phonebook")
            print("2. Messages")
            print("3. Chat")
            print("4. Call Register")
            print("5. Tones")
            print("6. Settings")
            print("7. Call divert")
            print("8. Games")
            print("9. Calculator")
            print("10. Reminder")
            print("11. Clock")
            print("12. Profiles")
            print("13. SIM Services")
            print("0. Exit")
            user_input = input("Enter an option: ")
            match user_input:
                case "1":
                    print(self.phoneBook.phoneBook_menu())
                case "2":
                    print(self.messages.show_menu())
                case "3":
                    print(self.chat)
                case "4":
                    print(self.call_register.call_register_menu())
                case "5":
                    print(self.tones.tones_menu())
                case "6":
                    print(self.settings.settings_menu())
                case "7":
                    print(self.call_divert)
                case "8":
                    print(self.games)
                case "9":
                    print(self.calculator)
                case "10":
                    print(self.reminder)
                case "11":
                    print(self.clock.clock_menu())
                case "12":
                    print(self.profiles)
                case "13":
                    print(self.sim_services)
                case "0":
                    print("Thank you for using Nokia331. Bye!")
                    break
                case _:
                    print("Invalid input. Please try again.")
if __name__ == "__main__":
    menu = Menu()
    menu.main()