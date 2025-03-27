import json
import csv

# Load JSON file
with open("alerts.json", "r") as file:
    data = json.load(file)

# Extract required fields
alerts_list = []
for alert in data:
    alerts_list.append([
        alert["number"],
        alert["created_at"],
        alert["security_advisory"]["severity"],
        alert["dependency"]["package"]["name"],
        alert["state"]
    ])

# Save to CSV
with open("security_alerts.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Created At", "Severity", "Package", "State"])
    writer.writerows(alerts_list)

print("CSV file generated: security_alerts.csv")
