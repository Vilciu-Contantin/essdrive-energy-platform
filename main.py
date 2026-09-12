import requests


def get_energy_data():
    url = "http://IP_ECHIPAMENT/?page=getdata&devid=HARDWARE_ID&devpass=API_KEY"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()


data = get_energy_data()

# Device information
device_id = data["devid"]
timestamp = data["time"]
relay_status = data["pout"]


# Phase 1
voltage_1 = float(data["data"]["V1"]["value"])
current_1 = float(data["data"]["A1"]["value"])
active_power_1 = float(data["data"]["W1"]["value"])
reverse_power_1 = float(data["data"]["rW1"]["value"])
energy_1 = float(data["data"]["Wh1"]["value"])
reverse_energy_1 = float(data["data"]["rWh1"]["value"])
power_factor_1 = float(data["data"]["PF1"]["value"])


# Phase 2
voltage_2 = float(data["data"]["V2"]["value"])
current_2 = float(data["data"]["A2"]["value"])
active_power_2 = float(data["data"]["W2"]["value"])
reverse_power_2 = float(data["data"]["rW2"]["value"])
energy_2 = float(data["data"]["Wh2"]["value"])
reverse_energy_2 = float(data["data"]["rWh2"]["value"])
power_factor_2 = float(data["data"]["PF2"]["value"])


# Phase 3
voltage_3 = float(data["data"]["V3"]["value"])
current_3 = float(data["data"]["A3"]["value"])
active_power_3 = float(data["data"]["W3"]["value"])
reverse_power_3 = float(data["data"]["rW3"]["value"])
energy_3 = float(data["data"]["Wh3"]["value"])
reverse_energy_3 = float(data["data"]["rWh3"]["value"])
power_factor_3 = float(data["data"]["PF3"]["value"])


# Temperature
temperature = float(data["data"]["T"]["value"])


# Total active power
total_active_power = (
    active_power_1
    + active_power_2
    + active_power_3
)


# Total reverse active power
total_reverse_power = (
    reverse_power_1
    + reverse_power_2
    + reverse_power_3
)


# Total cumulative energy
total_energy = (
    energy_1
    + energy_2
    + energy_3
)


# Total cumulative reverse energy
total_reverse_energy = (
    reverse_energy_1
    + reverse_energy_2
    + reverse_energy_3
)

total_reverse_energy = (
    reverse_energy_1
    + reverse_energy_2
    + reverse_energy_3
)

# Energie importată din rețea
grid_import = total_energy

# Energie exportată în rețea
grid_export = total_reverse_energy

net_energy = grid_export - grid_import

print(f"Net Energy : {net_energy} kWh")
print(f"Grid Import: {grid_import} kWh")
print(f"Grid Export: {grid_export} kWh")
print(f"Device ID: {device_id}")
print(f"Timestamp: {timestamp}")
print(f"Relay Status: {relay_status}")

print(f"Voltage: {voltage_1}, {voltage_2}, {voltage_3} V")
print(f"Current: {current_1}, {current_2}, {current_3} A")

print(f"Active Power: {active_power_1}, {active_power_2}, {active_power_3} W")
print(f"Reverse Power: {reverse_power_1}, {reverse_power_2}, {reverse_power_3} W")

print(f"Energy: {energy_1}, {energy_2}, {energy_3} kWh")
print(f"Reverse Energy: {reverse_energy_1}, {reverse_energy_2}, {reverse_energy_3} kWh")

print(f"Power Factor: {power_factor_1}, {power_factor_2}, {power_factor_3}")
print(f"Temperature: {temperature}")

print(f"Total Active Power: {total_active_power} W")
print(f"Total Reverse Power: {total_reverse_power} W")
print(f"Total Energy: {total_energy} kWh")
print(f"Total Reverse Energy: {total_reverse_energy} kWh")

print(data)

    
