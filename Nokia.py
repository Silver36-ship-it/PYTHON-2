reading = """
 WELCOME 
     TO
       YOUR 
          NOKIA
              MENU 
                 MAP
   List of menu functions
   1->> Phone book
   2->> Messages
   3->> Chat
   4->> Call register
   5->> Tones
   6->> Settings
   7->> Call divert
   8->> Games
   9->> Calculator
   10->> Reminder
   11->> Clock
   12->> Profiles
   13->> SIM services
       
       """ 
print(reading)
menuInput = int(input("Enter any option : "))
match menuInput :
	case 1: 
            phoneBook = """
            1-> Search
            2-> Service Nos.
            3-> Add name
            4-> Erase
            5-> Edit
            6-> Assign tone
            7-> Send business card
            8-> Options
            9-> Speed dials
            10-> Voice tags
            11-> Go back to Previous Menu                  
            """ 
            print(phoneBook)
            phone_book = int(input("Go for an option: "))
            match phone_book :    
                  case 1: print("Search")
                  case 2: print("Service Nos")
                  case 3: print("Add name")
                  case 4: print("Erase")
                  case 5: print("Edit")
                  case 6: print("Assign tone")
                  case 7: print("Send business card")
                  case 9: print("Speed dials")
                  case 8 : 
                           print("""
                           1-> Type of view
                           2-> Memory status
                           3-> Previous
                           """)
              
                           viewMemory1 = int(input("Enter option: "))
                           match viewMemory1 :
                               case 1 : print("Type of view")
                               case 2 : print("Memory status")
                               case 3 : print(phoneBook)
                               case _: print("Invalid input")  
                  case 10: print("Voice tags")
                  case 11: print(reading)
                  case _: print("Invalid input")
	case 2:
		messages = """
		1-> Write messages
		2-> Inbox
		3-> Outbox
		4-> Picture messages
		5-> Templates
		6-> Smileys
		7-> Message settings
		8-> Info service
		9-> Voice mailbox number
		10-> Service command editor
		 """
		print(messages)
		message_insight = int(input('Enter option: '))
		match message_insight:
			case 1: print('Write messages')
			case 2: print('Inbox')
			case 3: print('Outbox')
			case 4: print('Picture messages')
			case 5: print('Templates')
			case 6: print('Smileys')
			case 7: 
				print("""
				1-> Set
				2-> Common
		        """)
				setInput = int(input('Enter option: '))
				match setInput :
						case 1: 
							print("""
							1-> Message centre number
							2-> Messages sent as
							3-> Message validity
							""") 
							setInput2 = int(input('Enter option: '))
							match setInput2 :
								case 1 : print('Message centre number')
								case 2 : print('Message sent as')
								case 3 : print('Message validity')
								case _: print("Invalid input")
						case 2: 
							print("""
							1-> Delivery reports
							2-> Reply via same centre
							3-> Character support
							""")
							commonInput = int(input('Enter an option: '))
							match commonInput:
								case 1 : print("Delivery reports")
								case 2 : print("Reply via same centre")
								case 3 : print("Character support")
								case _: print("Invalid input")
						case _: print("Invalid input")
			case 8 : print('Info service')
			case 9 : print('Voice mailbox number')
			case 10 : print('Service command editor')
			case _: print("Invalid input")
	case 3:
		print("chat")
	case 4:
		callRegister = """
		1-> Missed calls
		2-> Received calls
		3-> Dialled numbers
		4-> Erase recent call lists
		5-> Show call duration
		6-> Show call costs
		7-> Call cost settings
		8-> Prepaid credit
		"""
		print(callRegister)
		callInput = int(input('Enter an option: '))
		match callInput :
			case 1: print('Missed calls')
			case 2: print('Received calls')
			case 3: print('Dialled numbers')
			case 4: print('Erase recent call lists')
			case 5:
				print("""
					Show call duration
				1-> Last call duration
				2-> All calls' duration
				3-> Received calls' duration
				4-> Dialled calls' duration
				5-> Clear timers
				""")
				callDuration = int(input('Enter an option: '))
				match callDuration :
					case 1: print('Last call duration')
					case 2: print("All calls' duration")
					case 3: print("Received calls' duration")
					case 4: print("Dialled calls' duration")
					case 5: print('Clear timers')
					case _: print("Invalid input")
			case 6:
				print("""
					Show call costs
				1-> Last call cost
				2-> All calls' cost
				3-> Clear counters
				""")
				showCall = int(input('Enter option: '))
				match showCall :
					case 1: print('Last call cost')
					case 2: print("All calls' cost")
					case 3: print('Clear counters')
					case _: print("Invalid input")
			case 7:
				print("""
					Call cost settings
				1-> Call cost limit
				2-> Show costs in
				""")
				callCost = int(input('Enter option: '))
				match callCost :
					case 1: print('Call cost limit')
					case 2: print('Show costs in')
					case _: print("Invalid input")
			case 8:
				print("Prepaid credit")
			case _: print("Invalid input")
	case 5:
		tones = """
			Tones
		1-> Ringing tone
		2-> Ringing volume
		3-> Incoming call alert
		4-> Composer
		5-> Message alert tone
		6-> Message alert tone
		7-> Keypad tones
		8-> Warning and game tones
		9-> Screen saver
		"""
		print(tones)
		tonesInput = int(input("Enter an option: "))
		match tonesInput :
			case 1: print('Ringing tone')
			case 2: print('Ringing volume')
			case 3: print('Incoming call alert')
			case 4: print('Composer')
			case 5: print('Message alert tone')
			case 6: print('Keypad tones')
			case 7: print('Warning and game tones')
			case 8: print('Vibrating alert')
			case 9: print('Screen saver')
			case _: print("Invalid input")
		
	case 6:
		settings = """
		1-> Call settings
		2-> Phone settings
		3-> Security settings
		4-> Restore factory settings
		"""
		print(settings)
		settingsInput = int(input("Enter an option: "))
		match settingsInput :
			case 1 : 
				print("""
					Call settings
				1-> Automatic redial
				2-> Speed dialling
				3-> Call waiting options
				4-> Own number sending
				5-> Phone line in use
				6-> Automatic answer
				""")
				callSettings = int(input('Enter an option: '))
				match callSettings :
					case 1 : print("Automatic redial")
					case 2 : print("Speed dialling")
					case 3 : print("Call waiting options")
					case 4 : print("Own number sending")
					case 5 : print("Phone line in use")
					case 6 : print("Automatic answer")
					case _: print("Invalid input")
			case 2 : 
				print("""
					Phone settings
				1-> Language
				2-> Cell info display
				3-> Welcome note
				4-> Network selection
				5-> Lights
				6-> Confirm SIM service actions
				""")
				phoneSettings = int(input("Enter an option: "))
				match phoneSettings :
					case 1 : print("Language")
					case 2 : print("Cell info display")
					case 3 : print("Welcome note")
					case 4 : print("Network selection")
					case 5 : print("Lights")
					case 6 : print("Confirm SIM service actions")
					case _: print("Invalid input")
			case 3 : 
				print("""
					Security settings
				1-> PIN code request
				2-> Cell barring service
				3-> Fixed dialling
				4-> Closed user group
				5-> Phone security
				6-> Change access codes
				""")
				securityInput = int(input("Enter an option: "))
				match securityInput :
					case 1 : print('PIN code request')
					case 2 : print('Cell barring service')
					case 3 : print('Fixed dialling')
					case 4 : print('Closed user group')
					case 5 : print('Phone security')
					case 6 : print('Change access codes')
					case _: print("Invalid input")
			case 4 : print("Restore factory settings")
			case _: print("Invalid input")
	case 7:
		print('Call divert')
	case 8:
		print('Games')
	case 9:
		print('Calculator')
	case 10:
		print('Reminders')
	case 11:
		clock = """
		1-> Alarm clock
		2-> Clock settings
		3-> Date setting
		4-> Stopwatch
		5-> Countdown timer
		6-> Auto update of date and time
		"""
		print(clock)
		clockInput = int(input('Enter an option: '))
		match clockInput :
				case 1: print('Alarm clock')
				case 2: print('Clock settings')
				case 3: print('Date setting')
				case 4: print('Stopwatch')
				case 5: print('Countdown timer')
				case 6: print('Auto update of date and time')
				case _: print('Invalid input')
	case 12:
		print('Profiles')
	case 13:
		print('SIM services')
	case _: print('Invalid input')
	
				
				
				
				


					
		



		                
		 
                   

                            