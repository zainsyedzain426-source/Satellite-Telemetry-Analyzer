import csv
import matplotlib.pyplot as plt

#Function for Battery
def check_battery(battery):

    battery = int(battery)

    if battery >= 80:
        return "🟢 Healthy"

    elif battery >= 50:
        return "🟡 Warning"

    else:
        return "🔴 Critical"

#Function for temperature
def check_temperature(temperature):

    temperature = int(temperature)

    if temperature <= 30:
        return "🟢 Normal"

    elif temperature <= 40:
        return "🟡 Warm"

    else:
        return "🔴 Overheating"

#Function for check signal
def check_signal(signal):

    if signal == "Strong":
        return "🟢 Excellent"

    elif signal == "Moderate":
        return "🟡 Moderate"

    else:
        return "🔴 Weak Connection"

#Function for checking altitude
def check_altitude(altitude):

    altitude = float(altitude)

    if 395 <= altitude <= 405:
        return "🟢 Stable"

    else:
        return "🔴 Unstable"

#Function for Velocity
def check_velocity(velocity):

    velocity = float(velocity)

    if 7.75 <= velocity <= 7.90:
        return "🟢 Nominal"

    else:
        return "🔴 Abnormal"

#Anomaly detection Function
def detect_anomalies(row):

    anomalies = []

    battery = float(row["Battery"])
    temperature = float(row["Temperature"])
    altitude = float(row["Altitude"])
    velocity = float(row["Velocity"])
    signal = row["Signal"]

    if battery < 50:
        anomalies.append("Low Battery")

    if temperature > 40:
        anomalies.append("High Temperature")

    if not 395 <= altitude <= 405:
        anomalies.append("Altitude Anomaly")

    if not 7.75 <= velocity <= 7.90:
        anomalies.append("Velocity Anomaly")

    if signal == "Weak":
        anomalies.append("Weak Signal")

    return anomalies


#Function for checking Satellite status
def overall_health(battery_status,
                   temperature_status,
                   altitude_status,
                   velocity_status,
                   signal_status):

    if ("🔴" in battery_status or
        "🔴" in temperature_status or
        "🔴" in altitude_status or
        "🔴" in velocity_status or
        "🔴" in signal_status):

        return "🔴 CRITICAL"

    elif ("🟡" in battery_status or
          "🟡" in temperature_status or
          "🟡" in altitude_status or
          "🟡" in velocity_status or
          "🟡" in signal_status):

        return "🟡 WARNING"

    else:

        return "🟢 HEALTHY"

# Statistic Function
def calculate_statistics(data):

    total_records = len(data)

    batteries = []
    temperatures = []

    weak_signal_count = 0

    for row in data:
        batteries.append(float(row["Battery"]))
        temperatures.append(float(row["Temperature"]))

        if row["Signal"] == "Weak":
            weak_signal_count += 1

    average_battery = sum(batteries) / total_records
    maximum_temperature = max(temperatures)
    minimum_battery = min(batteries)

    return total_records, average_battery, maximum_temperature, minimum_battery, weak_signal_count

#Report Function
def generate_report(
    total_records,
    average_battery,
    maximum_temperature,
    minimum_battery,
    weak_signal_count,
    total_anomalies
):

    report = ""

    report += "=" * 40 + "\n"
    report += "       SATELLITE TELEMETRY REPORT\n"
    report += "=" * 40 + "\n\n"

    report += f"Records Processed     : {total_records}\n"
    report += f"Average Battery       : {average_battery:.2f} %\n"
    report += f"Minimum Battery       : {minimum_battery} %\n"
    report += f"Maximum Temperature   : {maximum_temperature} °C\n"
    report += f"Weak Signal Events    : {weak_signal_count}\n"
    report += f"Total Anomalies       : {total_anomalies}\n"

    report += "\n"
    report += "=" * 40 + "\n"

    return report

#Main Code
with open("data/telemetry.csv", "r") as file:
    reader = csv.DictReader(file)

    data = list(reader)

    times = []
    battery_levels = []
    temperatures = []
    altitudes = []
    velocities = []

    anomaly_times = []
    anomaly_temperatures = []

    total_anomalies = 0

    for row in data:
        times.append(row["Time"])
        battery_levels.append(float(row["Battery"]))
        temperatures.append(float(row["Temperature"]))
        altitudes.append(float(row["Altitude"]))
        velocities.append(float(row["Velocity"]))

    for row in data:
        print("=" * 40)

        print(f"Time        : {row['Time']}")

        battery_status = check_battery(row["Battery"])
        print(f"Battery     : {row['Battery']} %   {battery_status}")

        temperature_status = check_temperature(row["Temperature"])
        print(f"Temperature : {row['Temperature']} °C   {temperature_status}")

        altitude_status = check_altitude(row["Altitude"])
        print(f"Altitude    : {row['Altitude']} km   {altitude_status}")

        velocity_status = check_velocity(row["Velocity"])
        print(f"Velocity    : {row['Velocity']} km/s   {velocity_status}")

        signal_status = check_signal(row["Signal"])
        print(f"Signal      : {row['Signal']}   {signal_status}")

        anomalies = detect_anomalies(row)

        if anomalies:

            total_anomalies += len(anomalies)

            print("⚠️ ANOMALIES DETECTED:")

            for anomaly in anomalies:
                print(f"   - {anomaly}")

            if "High Temperature" in anomalies:
                anomaly_times.append(row["Time"])
                anomaly_temperatures.append(float(row["Temperature"]))

        else:
            print("✅ No anomalies detected")


        # Calculate overall satellite health
        health = overall_health(
            battery_status,
            temperature_status,
            altitude_status,
            velocity_status,
            signal_status
        )

        print("-" * 40)
        print(f"Overall Health : {health}")

        print("=" * 40)


# Anomaly Summary
print("\n")
print("=" * 40)
print("       ANOMALY SUMMARY")
print("=" * 40)
print(f"Total Anomalies Detected : {total_anomalies}")
print("=" * 40)

#Calculate Statistics
statistics = calculate_statistics(data)

total_records, average_battery, maximum_temperature, minimum_battery, weak_signal_count = statistics

print("\n")
print("=" * 40)
print("       MISSION STATISTICS")
print("=" * 40)

print(f"Records Processed     : {total_records}")
print(f"Average Battery       : {average_battery:.2f} %")
print(f"Maximum Temperature   : {maximum_temperature} °C")
print(f"Minimum Battery       : {minimum_battery} %")
print(f"Weak Signal Events    : {weak_signal_count}")

print("=" * 40)

#Generate Report
report = generate_report(
    total_records,
    average_battery,
    maximum_temperature,
    minimum_battery,
    weak_signal_count,
    total_anomalies
)

print(report)

#Saving Report as .txt
with open("reports/mission_report.txt", "w", encoding="utf-8") as file:
    file.write(report)

#Graph Analysis

# Battery vs Time
plt.figure(figsize=(10, 5))

plt.plot(times, battery_levels, marker="o")

plt.title("Satellite Battery Level")
plt.xlabel("Time")
plt.ylabel("Battery (%)")
plt.grid(True)

plt.savefig("images/battery_vs_time.png")


# Temperature vs Time
plt.figure(figsize=(10, 5))

plt.plot(times, temperatures, marker="o")

plt.title("Satellite Temperature vs Time")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.savefig("images/temperature_vs_time.png")


# Altitude vs Time
plt.figure(figsize=(10, 5))

plt.plot(times, altitudes, marker="o")

plt.title("Satellite Altitude vs Time")
plt.xlabel("Time")
plt.ylabel("Altitude (km)")
plt.grid(True)

plt.savefig("images/altitude_vs_time.png")


# Velocity vs Time
plt.figure(figsize=(10, 5))

plt.plot(times, velocities, marker="o")

plt.title("Satellite Velocity vs Time")
plt.xlabel("Time")
plt.ylabel("Velocity (km/s)")
plt.grid(True)

plt.savefig("images/velocity_vs_time.png")


#Relationship Analysis
#Velocity vs Altitude
plt.figure(figsize=(10, 5))

plt.plot(altitudes, velocities, marker="o")

plt.title("Satellite Altitude vs Velocity")
plt.xlabel("Altitude (km)")
plt.ylabel("Velocity (km/s)")
plt.grid(True)

plt.savefig("images/altitude_vs_velocity.png")


# Temperature Anomaly Analysis
plt.figure(figsize=(10, 5))

plt.plot(
    times,
    temperatures,
    marker="o",
    label="Temperature"
)

plt.scatter(
    anomaly_times,
    anomaly_temperatures,
    marker="x",
    s=100,
    label="Anomaly"
)

plt.title("Satellite Temperature Anomaly Detection")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")

plt.grid(True)
plt.legend()

plt.savefig("images/temperature_anomalies.png")

# Show both graphs
plt.show()



