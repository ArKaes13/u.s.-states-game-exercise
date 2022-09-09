from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title('U.S. States Game')
screen.bgpic('blank_states_img.gif')
screen.setup(725, 491)
screen.tracer(0)

states_data = pandas.read_csv('50_states.csv')

text = Turtle()
text.penup()
text.hideturtle()

correct_guesses = []
while len(correct_guesses) < len(states_data):
    states_index = -1
    answer_state = screen.textinput(title=f'{len(correct_guesses)}/{len(states_data)} States Correct',
                                    prompt="Name the missing States").title()

    if answer_state == 'Exit':
        states_to_learn = [state for state in states_data.state if state not in correct_guesses]
        df = pandas.DataFrame(states_to_learn)
        df.to_csv('states_to_learn.csv')
        break

    for state in states_data.state:
        states_index += 1
        if answer_state == state and answer_state not in correct_guesses:
            correct_guesses.append(state)
            text.goto(states_data.x[states_index], states_data.y[states_index])
            text.write(f'{state}', align='center', font=('Arial', 8, 'normal'))
