from datetime import datetime

class AvionicsSystem:
    def __init__(self, name, power, status):
        self.name = ""
        self.power = True
        self.status = ""

        self.name = name
        self.power = power
        self.status = status



    def system_display(self):
        print("************* ONLINE SYSTEMS *************")
        for system in online_systems:
            print(system)
        print("*******************************************")
        print("************* OFFLINE SYSTEMS *************")
        for system in offline_systems:
            print(system)
        print("*******************************************")




def system_status(systems):
    online_systems.clear()
    offline_systems.clear()
    for system in systems:
        if system.status == "Online":
            online_systems.append(system.name)
        if system.status == "Offline" or system.power == False:
            offline_systems.append(system.name)




radar = AvionicsSystem("Radar", False, "Offline")
navigation = AvionicsSystem("Navigation", False, "Offline")
flight_controls = AvionicsSystem("Flight Controls", False, "Offline")
communications = AvionicsSystem("Communications", False, "Offline")

systems = [radar, navigation, flight_controls, communications]
online_systems = []
offline_systems = []

system_status(systems)
radar.system_display()


while True:
    menu_choice = input("""
1. Power On 
2. Power Off 
3. Display systems

Please enter the number of what you would like to select: """)
    if menu_choice == "1":
        while True:
            power_on_menu = input("""
    1.Radar
    2.Navigation
    3.Flight Controls
    4.Communications
    5.Quit
    
    Please enter the number of what you would like to power on: """)
            if power_on_menu == "1":
                radar.power = True
                radar.status = "Online"
            if power_on_menu == "2":
                navigation.power = True
                navigation.status = "Online"
            if power_on_menu == "3":
                flight_controls.power = True
                flight_controls.status = "Online"
            if power_on_menu == "4":
                communications.power = True
                communications.status = "Online"
            if power_on_menu == "5":
                break


    if menu_choice == "2":
        while True:
            power_off_menu = input("""
            1.Radar
            2.Navigation
            3.Flight Controls
            4.Communications
    
            Please enter the number of what you would like to power on: """)
            if power_off_menu == "1":
                radar.power = False
                radar.status = "Offline"
            if power_off_menu == "2":
                navigation.power = False
                navigation.status = "Offline"
            if power_off_menu == "3":
                flight_controls.power = False
                flight_controls.status = "Offline"
            if power_off_menu == "4":
                communications.power = False
                communications.status = "Offline"
            if power_off_menu == "5":
                break

    if menu_choice == "3":
        system_status(systems)
        radar.system_display()
