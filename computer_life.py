# power up game
# user faces an enemy: the computer.
# computer [power up, punch, knife, gun]
# user [power up, punch, knife, gun]
# If user power ups they gain 10 energy, punch lose 1 energy and subtract 2 from opponent, knife lose 2 energy
# minus 4 from opponent, gun lose 4 energy subtract 8 from opponent

import random

instructions: str = '''
You are fighting against a computer. To win, you must get the computer's life down to zero.
If your life falls to zero YOU LOSE. 😔🥲

You and the computer will start with 15 life. 👀
Both you and the computer have fighting options to stay alive, BUT you will use life using them.
'''

fighting_menu: str = '''
***** Fighting Menu ******
punch 👊: | enemy life -2 | your life -1
knife 🔪: | enemy life -4 | your life -2
gun 🔫:   | enemy life -8 | your life -4"
'''

power_up_menu: str = '''
----- power up menu -----
successful power up ✨🚀 | your life + 10
failed power up 😞🥲😵   | your life -  7
'''


def instructions_and_menus():
    print(instructions, fighting_menu, power_up_menu)


instructions_and_menus()
input('*** HIT ENTER TO PLAY 😵🚀🔫🔪 ***')


user_energy = 15
computer_energy = 15
attack = ['punch', 'knife', 'gun']
computer_attack = ['power up', 'punch', 'knife', 'gun']
try_power_up = ['power up', 'no power up']

print(f'STARTING LIFE ❇️ = {user_energy}')
while user_energy > 0 and computer_energy > 0:

    user_input = input("\nAttack the computer or try to power up P_P/: punch 👊, knife  🔪, gun 🔫, or power up? 🚀 -->: ")
    computer_choice = random.choice(computer_attack)

    match user_input:
        case 'punch':
            print("LIFE REMAINING ❇️ = ", user_energy - 1, "Computer life remaining", computer_energy - 2)
        case 'knife':
            print("LIFE REMAINING ❇️ = ", user_energy - 1, "Computer life remaining", computer_energy - 2)
        case 'gun':
            print("LIFE REMAINING ❇️ = ", user_energy - 4, "Computer life remaining", computer_energy - 8)
        case 'power up':
            try_power_up = random.choice(try_power_up)
            if try_power_up == 'powerup':
                print("Power up successful. ✨🚀🥹 Your life remaining", user_energy + 5)
            if try_power_up == 'no power up':
                print("Power up unsuccessful. 🥲You have lost life trying 🌚:", user_energy - 3)

    #
    # if user_input == "punch":
    #     print("Your life remaining:", user_energy - 1, "Computer life remaining", computer_energy - 2)
    # elif user_input == "knife":
    #     print("Your life remaining:", user_energy - 2, "Computer life remaining", computer_energy - 4)
    # elif user_input == "gun":
    #     print("Your life remaining:", user_energy - 4, "Computer life remaining", computer_energy - 8)
    # elif user_input == "power up":
    #     try_power_up = random.choice(try_power_up)
    #     if try_power_up == 'powerup':
    #         print("Power up successful. Your life remaining", user_energy + 5)
    #     if try_power_up == 'sorry no power up':
    #         print("Power up unsuccessful. You have lost life trying:", user_energy - 3)

    match computer_choice:
        case 'power up':
            print("Computer move:", computer_choice, "LIFE REMAINING ❇️ = ", user_energy, "ENEMY LIFE ♦️️ = ", computer_energy + 5)
        case 'punch':
            print("Computer move:", computer_choice, "LIFE REMAINING ❇️ = ", user_energy - 2, "ENEMY LIFE ♦️️ = ", computer_energy - 1)
        case 'knife':
            print("Computer move:", computer_choice, "LIFE REMAINING ❇️ = ", user_energy - 4, "ENEMY LIFE ♦️️ = ", computer_energy - 2)
        case 'gun':
            print("Computer move:", computer_choice, "LIFE REMAINING ❇️ = ", user_energy - 8, "ENEMY LIFE ♦️️ = ", computer_energy - 4)


    # if computer_attack == 'power up':
    #     print("Computer move:", computer_choice, "Your life:", user_energy, "Computer life:", computer_energy + 5)
    # elif computer_attack == 'punch':
    #     print("Computer move:", computer_choice, "Your life:", user_energy - 2, "Computer life:", computer_energy - 1)
    # elif computer_attack == 'knife':
    #     print("Computer move:", computer_choice, "Your life:", user_energy - 4, "Computer life:", computer_energy - 2)
    # elif computer_attack == 'gun':
    #     print("Computer move:", computer_choice, "Your life:", user_energy - 8, "Computer life:", computer_energy - 4)




