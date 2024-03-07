import json

with open("C:\\Users\\77016\\Downloads\\sample-data (1).json", 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data.get('imdata', []):
    interface = item.get('l1PhysIf', {}).get('attributes', {})
    print("{:<50} {:<15} {:<10} {:<10}".format(interface.get("dn", ""), interface.get("descr", ""), interface.get("speed", ""), interface.get("mtu", "")))