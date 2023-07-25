import tkinter as tk
from tkinter import ttk
import sqlite3
import random
import xml.etree.ElementTree as ET
from game.game import HangmanGame


def start_game(theme_id):
    # 根据用户选择的主题ID，从数据库中获取该主题的所有词汇
    conn = sqlite3.connect('bdd/hangman.db')
    cursor = conn.cursor()
    cursor.execute('SELECT word FROM Words WHERE theme_id = ?', (theme_id,))
    words_list = cursor.fetchall()
    conn.close()

    # 随机选择一个词汇
    if words_list:
        word = random.choice(words_list)[0].upper()
        game = HangmanGame()  # 创建HangmanGame的实例
        game.show_main_window(word)


def quit_game(root):
    # 实现退出游戏的功能
    root.destroy()


def main():
    root = tk.Tk()
    root.title("Hangman Game")
    root.geometry("400x300")

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
                    label=label, command=lambda root=root: quit_game(root))  # 传递根窗口作为参数给quit_game函数
            else:
                # 此处可以根据command指定的函数名来绑定对应的功能函数
                menu.add_command(label=label)
        root_menu.add_cascade(
            label=menu_elem.attrib['categorie'], menu=menu)  # 将菜单添加到主菜单栏中

    # 将菜单栏添加到主窗口
    root.config(menu=root_menu)

    # 创建ttk.Style对象
    style = ttk.Style()

    # 设置主题颜色为蓝色
    style.theme_use('default')
    style.configure('TButton', foreground='black',
                    background='#458BFF', font=('Helvetica', 12))

    label = tk.Label(root, text="Please choose a theme: ",
                     font=('Helvetica', 14, 'bold'))
    label.pack()

    # 获取所有主题列表
    conn = sqlite3.connect('bdd/hangman.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Themes')
    themes_list = cursor.fetchall()
    conn.close()

    # 显示所有主题的按钮
    for theme_id, theme_name in themes_list:
        button = ttk.Button(root, text=theme_name,
                            command=lambda t=theme_id: start_game(t))
        button.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
