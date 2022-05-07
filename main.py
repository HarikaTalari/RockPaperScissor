from tkinter import *
from PIL import Image, ImageTk
from random import randint


class RockPaperScissors:
    def __init__(self):
        rock_paper_canvas = Canvas(window, width=400, height=400, bg='#b0d0b9')
        rock_paper_canvas.pack(fill="both", expand=True)
        global rock_image,scissor_image,paper_image
        global player, computer, computer_score, player_score

        player = 0
        computer = 0
        player_score = Label(rock_paper_canvas, text="Your Score: " + str(player), font=('Arial', 25, 'bold'),
                             bg='#b0d0b9')
        player_score.place(x=550, y=10)
        computer_score = Label(rock_paper_canvas, text="Computer Score: " + str(computer), font=('Arial', 25, 'bold'),
                               bg='#b0d0b9')
        computer_score.place(x=520, y=330)
        self.acknowledge = Label(rock_paper_canvas, text=" ", font=('Arial', 25, 'bold'),
                                 bg='#b0d0b9')
        self.acknowledge.place(x=750, y=500)
        self.open_page(rock_paper_canvas)

    def open_page(self, rock_paper_canvas):

        global rock_image
        global scissor_image
        global paper_image

        rock_image = ImageTk.PhotoImage(Image.open("rock.png"))
        rock_button = Button(rock_paper_canvas, image=rock_image, borderwidth=0, bg='#b0d0b9', height=240, width=180
                             , command=lambda: self.rock(rock_paper_canvas, paper_button, scissor_button, options,
                                                         computer_choice))
        rock_button.place(x=250, y=80)
        paper_image = PhotoImage(file='paper.png')
        paper_button = Button(rock_paper_canvas, image=paper_image, borderwidth=0, height=240, width=180, bg='#b0d0b9'
                              , command=lambda: self.paper(rock_paper_canvas, rock_button, scissor_button, options,
                                                           computer_choice))
        paper_button.place(x=600, y=80)
        scissor_image = PhotoImage(file='scissor.png')
        scissor_button = Button(rock_paper_canvas, image=scissor_image, borderwidth=0, height=240, width=180,
                                bg='#b0d0b9',
                                command=lambda: self.scissor(rock_paper_canvas, rock_button, paper_button, options,
                                                             computer_choice)
                                )
        scissor_button.place(x=950, y=80)
        options = [rock_button, paper_button, scissor_button]
        computer_choice = options[randint(0, 2)]

    def rock(self, rock_paper_canvas, paper_button, scissor_button, options, computer_choice):
        paper_button.destroy()
        scissor_button.destroy()
        if computer_choice == options[0]:
            global computer_rock_image
            computer_rock_image = ImageTk.PhotoImage(Image.open("rock.png"))
            rock_button = Button(rock_paper_canvas, image=computer_rock_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Oops! It's a Tie")
            self.open_page(rock_paper_canvas)

        elif computer_choice == options[1]:
            global computer_paper_image, computer, computer_score
            computer_paper_image = ImageTk.PhotoImage(Image.open("paper.png"))
            rock_button = Button(rock_paper_canvas, image=computer_paper_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text='You lose')

            self.computer_score_update(rock_paper_canvas)

        elif computer_choice == options[2]:
            global computer_scissor_image, player_score, player
            computer_scissor_image = ImageTk.PhotoImage(Image.open("scissor.png"))
            rock_button = Button(rock_paper_canvas, image=computer_scissor_image, borderwidth=0,
                                 highlightcolor='#b0d0b9', height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Hurrah! You Won")
            self.player_score_update(rock_paper_canvas)

    def paper(self, rock_paper_canvas, rock_button, scissor_button, options, computer_choice):
        rock_button.destroy()
        scissor_button.destroy()
        if computer_choice == options[0]:
            global computer_rock_image, player, player_score
            computer_rock_image = ImageTk.PhotoImage(Image.open("rock.png"))
            rock_button = Button(rock_paper_canvas, image=computer_rock_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Hurrah! You Won")
            self.player_score_update(rock_paper_canvas)
        elif computer_choice == options[1]:
            global computer_paper_image
            computer_paper_image = ImageTk.PhotoImage(Image.open("paper.png"))
            rock_button = Button(rock_paper_canvas, image=computer_paper_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Oops! It's a Tie")
            self.open_page(rock_paper_canvas)
        elif computer_choice == options[2]:
            global computer_scissor_image, computer, computer_score
            computer_scissor_image = ImageTk.PhotoImage(Image.open("scissor.png"))
            rock_button = Button(rock_paper_canvas, image=computer_scissor_image, borderwidth=0,
                                 highlightcolor='#b0d0b9', height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text='You lose')
            self.computer_score_update(rock_paper_canvas)

    def scissor(self, rock_paper_canvas, rock_button, paper_button, options, computer_choice):
        rock_button.destroy()
        paper_button.destroy()
        if computer_choice == options[0]:
            global computer_rock_image, computer_score, computer
            computer_rock_image = ImageTk.PhotoImage(Image.open("rock.png"))
            rock_button = Button(rock_paper_canvas, image=computer_rock_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text='You lose')
            self.computer_score_update(rock_paper_canvas)
        elif computer_choice == options[1]:
            global computer_paper_image, player, player_score
            computer_paper_image = ImageTk.PhotoImage(Image.open("paper.png"))
            rock_button = Button(rock_paper_canvas, image=computer_paper_image, borderwidth=0, highlightcolor='#b0d0b9',
                                 height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Hurrah! You Won")
            self.player_score_update(rock_paper_canvas)
        elif computer_choice == options[2]:
            global computer_scissor_image
            computer_scissor_image = ImageTk.PhotoImage(Image.open("scissor.png"))
            rock_button = Button(rock_paper_canvas, image=computer_scissor_image, borderwidth=0,
                                 highlightcolor='#b0d0b9', height=240, width=180, bg='#b0d0b9')
            rock_button.place(x=500, y=420)
            self.acknowledge.config(text="Oops! It's a Tie")
            self.open_page(rock_paper_canvas)

    def computer_score_update(self, rock_paper_canvas):
        global computer, computer_score, player

        computer += 1
        computer_score.config(text='Computer Score: ' + str(computer))
        if computer == 3:
            rock_paper_canvas.destroy()
            result_canvas = Canvas(window, width=400, height=400, bg='#b0d0b9')
            result_canvas.pack(fill="both", expand=True)
            result_label = Label(result_canvas, text='You lose', font=('Arial', 50, 'bold'), bg='#b0d0b9', fg='red')
            result_label.place(x=520, y=150)
            ratio = Label(result_canvas, text=str(player) + ' ' + ':' + ' ' + '3', font=('Arial', 50, 'bold'),
                          bg='#b0d0b9', fg='red')
            ratio.place(x=600, y=250)
            play_again_button = Button(result_canvas, text='Play again', font=('Arial', 25, 'bold'), bg='#4a934a',
                                       fg='white', command=lambda: self.game_over(result_canvas))
            play_again_button.place(x=520, y=450)
            exit_button = Button(result_canvas, text='Exit', font=('Arial', 25, 'bold'), bg='red', fg='white',
                                 command=self.exit_game)
            exit_button.place(x=740, y=450)
        self.open_page(rock_paper_canvas)

    def player_score_update(self, rock_paper_canvas):
        global player, player_score
        player += 1
        player_score.config(text='Your Score: ' + str(player))
        if player == 3:
            rock_paper_canvas.destroy()
            result_canvas = Canvas(window, width=400, height=400, bg='#b0d0b9')
            result_canvas.pack(fill="both", expand=True)
            result_label = Label(result_canvas, text='You Won ', font=('Arial', 50, 'bold'), bg='#b0d0b9', fg='green')
            result_label.place(x=520, y=150)
            ratio = Label(result_canvas, text='3' + ' ' + ':' + ' ' + str(computer), font=('Arial', 50, 'bold'),
                          fg='green',
                          bg='#b0d0b9')
            ratio.place(x=600, y=250)
            play_again_button = Button(result_canvas, text='Play again', font=('Arial', 25, 'bold'), bg='#4a934a',
                                       fg='white', command=lambda: self.game_over(result_canvas))
            play_again_button.place(x=520, y=450)
            exit_button = Button(result_canvas, text='Exit', font=('Arial', 25, 'bold'), bg='red', fg='white',
                                 command=self.exit_game)
            exit_button.place(x=740, y=450)
        self.open_page(rock_paper_canvas)

    def exit_game(self):
        window.destroy()

    def game_over(self, result_canvas):
        result_canvas.destroy()
        RockPaperScissors()


if __name__ == "__main__":
    window = Tk()
    window.state("zoomed")
    window.title("Rock Paper Scissor")
    window.resizable(False, False)

    global rock_image, scissor_image, paper_image
    global computer_rock_image, computer_paper_image, computer_scissor_image
    global player, computer, computer_score, player_score
    RockPaperScissors()
    window.mainloop()
