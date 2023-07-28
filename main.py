import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import xml.etree.ElementTree as ET
import subprocess


class WelcomeScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to Hangman Game")
        self.root.geometry("400x300")

        # 解析XML菜单
        tree = ET.parse('menus.xml')
        root_menu = tk.Menu(root)

        # 创建菜单栏
        for menu_elem in tree.findall('menu'):
            menu = tk.Menu(root_menu, tearoff=0)  # 创建一个菜单
            for lien_elem in menu_elem.findall('lien'):
                label = lien_elem.find('label').text
                command = lien_elem.find('command').text
                if command == "quit_game":
                    menu.add_command(
                        label=label, command=self.quit_game)  # 传递根窗口作为参数给quit_game函数
                elif command == "play_game":
                    menu.add_command(
                        label=label, command=self.play_game)
                elif command == "about":
                    menu.add_command(
                        label=label, command=self.about)
                else:
                    # 此处可以根据command指定的函数名来绑定对应的功能函数
                    menu.add_command(label=label, command=command)
            root_menu.add_cascade(
                label=menu_elem.attrib['categorie'], menu=menu)  # 将菜单添加到主菜单栏中

        # 将菜单栏添加到主窗口
        root.config(menu=root_menu)

        canvas = tk.Canvas(root, width=400, height=300)
        canvas.pack()

        # 添加“Welcome to Hangman Game”文本
        canvas.create_text(200, 100, text="Welcome to Hangman Game",
                           font=("Helvetica", 20, "bold"))

        # 添加Play按钮
        play_button = ttk.Button(root, text="Play", command=self.play_game)
        play_button.place(x=150, y=150, width=100, height=40)

        # 添加Quit按钮
        quit_button = ttk.Button(root, text="Quit", command=self.quit_game)
        quit_button.place(x=150, y=200, width=100, height=40)

    def play_game(self):
        # 启动index.py，打开游戏窗口
        subprocess.Popen(["python", "index.py"])
        self.root.destroy()  # 关闭当前窗口

    def quit_game(self):
        # 退出游戏
        self.root.destroy()

    def about(self) -> None:
        "Affichage de la boîte de dialogue 'À propos'"
        messagebox.showinfo(
            "About", "Welcome to the 'Hangman' game, It is licensed under GNU-GPL 3.0")


def main():
    root = tk.Tk()
    welcome_screen = WelcomeScreen(root)
    root.mainloop()


if __name__ == "__main__":
    main()
