import tkinter as tk
from tkinter import *
from tkinter import messagebox as tmsg
import xml.etree.ElementTree as ET


class HangmanGame:
    def __init__(self):
        # 初始化时设置num和图片资源
        self.num = 1
        self.lst = [PhotoImage(
            file=f"images/hangman{i}.png") for i in range(7)]
        self.buttons = []  # 保存按钮的列表

    def show_main_window(self, word):
        # 在此处显示主界面，您可以根据您的界面设计和逻辑来实现
        # 这里只是一个简单的示例，使用Tkinter创建一个新窗口来显示选中的单词
        self.main_window = tk.Toplevel()
        self.main_window.title("Hangman Game")
        self.main_window.geometry("1000x550")

        def quit_game(root):
            # 实现退出游戏的功能
            root.destroy()

        # 解析XML菜单
        tree = ET.parse('menus.xml')
        root_menu = tk.Menu(self.main_window)

        # 创建菜单栏
        for menu_elem in tree.findall('menu'):
            menu = tk.Menu(root_menu, tearoff=0)  # 创建一个菜单
            for lien_elem in menu_elem.findall('lien'):
                label = lien_elem.find('label').text
                command = lien_elem.find('command').text
                if command == "quit_game":
                    menu.add_command(
                        label=label, command=lambda root=self.main_window: quit_game(root))  # 传递根窗口作为参数给quit_game函数
                else:
                    # 此处可以根据command指定的函数名来绑定对应的功能函数
                    menu.add_command(label=label)
            root_menu.add_cascade(
                label=menu_elem.attrib['categorie'], menu=menu)  # 将菜单添加到主菜单栏中

        # 将菜单栏添加到主窗口
        self.main_window.config(menu=root_menu)

        # 此处为输出信息的Label
        self.response_label = Label(
            self.main_window, text="", font=("comicsans", 40, "bold"))
        self.response_label.grid(row=4, columnspan=2)

        # 使用Label显示图片
        self.chances = Label(self.main_window, image=self.lst[0])
        self.chances.grid(row=0, column=0)

        # 创建字母按钮
        self.letters_frame = Frame(self.main_window, bg="blue")
        self.letters_frame.grid(row=5, column=0, columnspan=4, pady=10)

        # 创建字母按钮，并使用grid布局
        row = 0
        col = 0
        max_buttons_per_row = 13  # 每行最大按钮数量

        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            btn = Button(self.letters_frame, text=letter, font=("comicsans", 20, "bold"),
                         width=3, bg="blue", fg="white")
            btn.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(btn)  # 将按钮添加到列表中

            col += 1
            if col >= max_buttons_per_row:
                col = 0
                row += 1

        # functioning of code

        random_word = [x for x in word]
        print(random_word)

        check_word = ["-" for x in range(len(word))]

        word_label = Label(self.main_window, text=check_word,
                           font=("comicsans", 50, "bold"))
        word_label.grid(row=0, column=1)

        def hi(event=None):
            temp = check_alp.get()
            if len(temp) > 1:
                tmsg.showerror(
                    "Error", "Only single Alphabet is required", parent=self.main_window)
            elif temp == "":
                tmsg.showerror(
                    "Error", "Please provide an Alphabet", parent=self.main_window)
            else:
                if temp.capitalize() in random_word:
                    indices = [i for i, letter in enumerate(
                        random_word) if letter == temp.capitalize()]
                    for ind in indices:
                        check_word.pop(ind)
                        check_word.insert(ind, temp.capitalize())
                    word_label.configure(text=check_word)
                    self.response_label.configure(
                        text="  Right Guess   ", fg="green")
                    index = ord(temp.capitalize()) - ord('A')
                    self.buttons[index].config(bg='light green', fg='black')

                    if "-" not in check_word:
                        result = tmsg.showinfo("Congragulations",
                                               "      You win       ", parent=self.main_window)
                        if result:
                            self.main_window.destroy()  # 关闭 main_window 窗口

                else:
                    try:
                        self.response_label.configure(
                            text="Wrong Guess", fg="red")
                        index = ord(temp.capitalize()) - ord('A')
                        self.buttons[index].config(bg='grey', fg='white')
                        self.chances.configure(image=self.lst[self.num])
                        self.num += 1
                    except IndexError:
                        result = tmsg.showerror(
                            "You lose", "Sorry, chances over", parent=self.main_window)
                        if result:
                            self.main_window.destroy()  # 关闭 main_window 窗口

            alp.set("")

        Button(self.main_window, text="CHECK", command=hi,
               height=2, bg="Blue").grid(row=2)

        Label(self.main_window, text="   Type an Alphabet:", font=(
            "comicsans", 40, "bold")).grid(row=3, columnspan=2)

        # 创建Entry组件
        alp = StringVar()
        check_alp = Entry(self.main_window, bg="cyan", textvariable=alp)
        check_alp.grid(row=3, column=3)
        check_alp.bind('<Return>', hi)

        # 设置光标自动定位到Entry组件
        check_alp.focus()

        self.main_window.mainloop()
