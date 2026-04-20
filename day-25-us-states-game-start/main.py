import turtle
import pandas as pd
correct_guesses = []

states_df = pd.read_csv("./50_states.csv")
states_list = states_df.state.to_list()

main_screen = turtle.Screen()
main_screen.title("U.S. States Game")
image = "./blank_states_img.gif"
main_screen.bgpic(image)
input_screen = turtle.Screen()
while len(correct_guesses) < 50:
    # 1. Convert the guess to Title case
    answer_state = input_screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                          prompt="What's another state's name").title()
    if answer_state == "Exit":
        break
    # 2. Check if the guess is among the 50 states
    for state in states_list:
        # print(state)
        # print(lower_state)
        if answer_state == state:
            # 3. Write the correct guess onto the map
            index_location = (states_list.index(state))
            row = states_df.loc[index_location]
            x_coord = row.x
            y_coord = row.y
            state = turtle.Turtle()
            state.hideturtle()
            state.penup()
            state.goto(x=x_coord, y=y_coord)
            state.write(answer_state)
            # 5. Record the correct guesses in a list
            correct_guesses.append(row.state)
    # 4. Use a loop to allow the user to keep guessing

with open("./states_to_learn.csv", "w") as remaining_states:
    if len(correct_guesses) == 50:
        remaining_states.write("Good job! You know all the states!")
    else:
        for state in states_list:
            if state not in correct_guesses:
                remaining_states.write(f"{state}\n")



