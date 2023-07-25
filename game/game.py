import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg


class HangmanGame:
    def __init__(self):
        # 初始化时设置num和图片资源
        self.num = 1
        self.lst = [PhotoImage(
            file=f"images/hangman{i}.png") for i in range(7)]

    def show_main_window(self, word):
        # 在此处显示主界面，您可以根据您的界面设计和逻辑来实现
        # 这里只是一个简单的示例，使用Tkinter创建一个新窗口来显示选中的单词
        self.main_window = tk.Toplevel()
        self.main_window.title("Hangman Game")
        self.main_window.geometry("1000x550")

        # 此处为输出信息的Label
        self.response_label = Label(
            self.main_window, text="", font=("comicsans", 40, "bold"))
        self.response_label.grid(row=4, columnspan=2)

        # 使用Label显示图片
        self.chances = Label(self.main_window, image=self.lst[0])
        self.chances.grid(row=0, column=0)

        # functioning of code

        random_word = [x for x in word]
        print(random_word)

        check_word = ["-" for x in range(len(word))]

        # choice for user
        sample = []
        for i in random_word:
            sample.append(i)

        word_label = Label(self.main_window, text=check_word,
                           font=("comicsans", 50, "bold"))
        word_label.grid(row=0, column=1)

        def hi():
            temp = check_alp.get()
            if len(temp) > 1:
                tmsg.showerror(
                    "Error", "Only single Alphabet is required", parent=self.main_window)
            elif temp == "":
                tmsg.showerror(
                    "Error", "Please provide an Alphabet", parent=self.main_window)
            else:
                if temp.capitalize() in random_word:
                    ind = random_word.index(temp.capitalize())
                    check_word.pop(ind)
                    check_word.insert(ind, temp.capitalize())
                    word_label.configure(text=check_word)
                    self.response_label.configure(
                        text="  Right Guess   ", fg="green")
                    if "-" not in check_word:
                        result = tmsg.showinfo("Congragulations",
                                               "      You win       ", parent=self.main_window)
                        if result:
                            self.main_window.destroy()  # 关闭 main_window 窗口

                else:
                    try:
                        self.response_label.configure(
                            text="Wrong Guess", fg="red")
                        self.chances.configure(image=self.lst[self.num])
                        self.num += 1
                    except IndexError:
                        result = tmsg.showerror(
                            "You lose", "Sorry, chances over", parent=self.main_window)
                        if result:
                            self.main_window.destroy()  # 关闭 main_window 窗口

            alp.set("")

        Button(self.main_window, text="CHECK", command=hi,
               height=2, bg="yellow").grid(row=2)

        Label(self.main_window, text="   Type an Alphabet:", font=(
            "comicsans", 40, "bold")).grid(row=3, columnspan=2)

        alp = StringVar()
        check_alp = Entry(self.main_window, bg="cyan", textvariable=alp)
        check_alp.grid(row=3, column=3)

        self.main_window.mainloop()
