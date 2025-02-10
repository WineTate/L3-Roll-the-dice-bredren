error = "put in a number more than / equal to 13"

while True:
    try:
        game_goal = int(input("What is the game goal?"))

        if game_goal < 13:
            print(error)

        print(f"Game Goal: {game_goal}")

    except ValueError:
        print(error)
