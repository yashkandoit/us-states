import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

answer=screen.textinput(title="U.S. States Game",prompt="Guess any State")

tim=turtle.Turtle()
tim.hideturtle()
tim.penup()

data=pandas.read_csv("50_states.csv")
states=data["state"].tolist()
x=data["x"].tolist()
y=data["y"].tolist()
guessed=[]


while len(guessed)<50:
    if answer.title()=="Exit":
        break

    if answer.title() in states and answer.title() not in guessed:
        index=states.index(answer.title())
        tim.goto(x[index],y[index])
        tim.write(answer.title())
        guessed.append(answer.title())

    answer=screen.textinput(title=f"Correct States-{len(guessed)}/50",prompt="Guess any State")

to_learn=[i for i in states if i not in guessed]

data1=pandas.DataFrame(to_learn)
data1.to_csv("States to Learn.csv")


turtle.mainloop()
