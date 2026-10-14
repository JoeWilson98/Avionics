import json
import urllib.request

url_launches = "https://lldev.thespacedevs.com/2.3.0/launches/upcoming/"


response = urllib.request.Request(url_launches, headers={"User-Agent": "NASALunchTracker/1.0"})

with urllib.request.urlopen(response) as response:
    result = json.loads(response.read().decode("utf-8"))

print(f"{"SPACECRAFT"} {"LAUNCH START":>68} {"AGENCY":>16} {"ID":>52} {"MISSION":>43}")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
for data in result["results"]:
    print("{:<65.65} | {:<10} | {:<55} | {} | {}".format(data["name"], data["window_start"], data["launch_service_provider"]["name"], data["id"], data["mission"]["name"]))

