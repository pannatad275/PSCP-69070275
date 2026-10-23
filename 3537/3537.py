'''imposter'''
players = {}
while True:
    line = input().strip()
    if line == "Start":
        break
    line = line.replace("{", "").replace("}", "").replace('"', "")
    name, role = line.split(" : ")
    players[name] = role
dead_players = {}

while True:
    line = input().strip()
    if line == "End":
        break
    if line in players:
        dead_players[line] = players.pop(line)
impostor_count = 0
for role in players.values():
    if role == "Impostor":
        impostor_count = impostor_count + 1
print(str(impostor_count) + " Impostor Remains")
print("***Alive***")
alive_names = list(players.keys())
alive_names.sort()
for name in alive_names:
    print(name + " : " + players[name])
print("***Dead***")
dead_names = list(dead_players.keys())
dead_names.sort()
for name in dead_names:
    print(name + " : " + dead_players[name])
