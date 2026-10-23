def dice_game():
    score = 0
    while true:
        choice = input("enter 'r' to roll or 'q' to quit ")
        if choice == 'q':
            print(f"game over. final score:")
            elif choice == 'r':
                if roll = random.randint(1,7)
                    if roll == 7:
                    score += 10
                    print(f"you rolled a {roll}! you win 10 points.")
                    else:
                        score -= 5
                        print(f"you rolled a {roll}. you lose 5 points.")
                        print(f"current score: {score}")
                        else:
                            print("invalid input.")