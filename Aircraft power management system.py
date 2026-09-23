import numpy as np
import datetime
import time

def power_management(available_power, systems):
    if available_power < 3400:
        for system, data in systems.items():
            if data["priority"] == 3:
                reduce_power = data["power"] * 0.8
                print("{} now in reduced power : Running at {} W".format(system, reduce_power))



systems = {
"Avionics" : {"power" : 500, "priority" : 1},
"Radar" : {"power" : 1200, "priority" : 2},
"Communications" : {"power": 300, "priority" : 1},
"Lighting": {"power" : 200, "priority" : 3},
"Navigation": {"power" : 400, "priority" : 2},
"Environmental Control": {"power" : 800, "priority" : 2},

}


power = np.array([system["power"]for system in systems.values()])
priority = np.array([system["priority"]for system in systems.values()])
required_power = np.sum(power)

print("Required Power: {} W".format(required_power))

percentages = []
for num in power:
    percentage = num / required_power * 100
    percentages.append(percentage)

print("\nSystem                          Power           Percentage")
print("-------------------------------------------------------------")
for (system, power), percentage in zip(systems.items(), percentages):
    print("{:<25}       {:>5.2f}W         {:>0.2f}%".format(system, power["power"], percentage))

power_usage = np.random.normal(3400,30,24)

while True:
    for current_power in power_usage:
        if current_power > 4500:
            status_power = "CRITICAL"
            current_deficit = required_power - current_power
        elif current_power > 4000:
            status_power = "WARNING"
            current_deficit = required_power - current_power
        else:
            status_power = "Normal"
            current_deficit = required_power - current_power


        print("\nCurrent power usage: {:.2f} W | Status: {}".format(current_power, status_power))
        print("Current power deficit: {:.2f} W".format(current_deficit))
        if current_deficit > 0:
            power_management(current_power, systems)

        time.sleep(10)
