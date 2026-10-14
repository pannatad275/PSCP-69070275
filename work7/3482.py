'''demon'''
def main():
    '''slayer'''
    demon_weakness = {
        'Spider Demon': 1,
        'Arrow Demon': 1,
        'Swamp Demon': 2,
        'Hand Demon': 2,
        'Mugen Train': 2,
        'Drum Demon': 3,
        'Upper Moon': 3
    }

    demon_queue = [
        'Spider Demon', 'Swamp Demon', 'Arrow Demon', 
        'Hand Demon', 'Drum Demon', 'Mugen Train', 'Upper Moon'
    ]

    kills = 0
    total_attacks = 0
    wrong_attempts = 0

    while kills < 5 and demon_queue:
        current_demon = demon_queue[0]
        attack = int(input())
        total_attacks += 1

        if attack == demon_weakness[current_demon]:
            print(current_demon)
            print("kill")
            kills += 1
            demon_queue.pop(0)
            wrong_attempts = 0
        else:
            wrong_attempts += 1
            if wrong_attempts == 2:
                print(current_demon)
                print("back")
                demon_queue.append(demon_queue.pop(0))
                wrong_attempts = 0

    print(total_attacks)
main()
