import random

roll = input("Do you want to roll the dice? [y/n] ")
dice = ["[-----]\n[     ]\n[  0  ]\n[     ]\n[-----]",
        "[-----]\n[ 0   ]\n[     ]\n[   0 ]\n[-----]",
        "[-----]\n[ 0   ]\n[  0  ]\n[   0 ]\n[-----]",
        "[-----]\n[ 0 0 ]\n[     ]\n[ 0 0 ]\n[-----]",
        "[-----]\n[ 0 0 ]\n[  0  ]\n[ 0 0 ]\n[-----]",
        "[-----]\n[ 0 0 ]\n[ 0 0 ]\n[ 0 0 ]\n[-----]"]
while roll == "y":
    num = random.randint(1,6)
    print(dice[num-1])
    roll = input("Do you want to roll again? [y/n] ")
print("Thanks for using my dice!")
quit()
    