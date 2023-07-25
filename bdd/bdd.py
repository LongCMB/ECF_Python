import sqlite3

# 连接到数据库或创建一个新数据库
conn = sqlite3.connect('bdd/hangman.db')

# 创建一个游标对象来执行SQL命令
cursor = conn.cursor()

# 创建Themes表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Themes (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

# 创建Words表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Words (
        id INTEGER PRIMARY KEY,
        word TEXT NOT NULL,
        theme_id INTEGER NOT NULL,
        FOREIGN KEY (theme_id) REFERENCES Themes (id)
    )
''')

# 示例主题和单词列表
themes_data = [('Developer',), ('Designer',),
               ('Front-end',), ('Back-end',), ('Others',)]
words_data = [
    ('python', 1), ('javascript', 1), ('html', 1), ('css', 1), ('django', 1),
    ('sketch', 2), ('photoshop', 2), ('maquettage',
                                      2), ('figma', 2), ('wireframe', 2),
    ('html', 3), ('css', 3), ('sass', 3), ('bootstrap', 3), ('javascript', 3),
    ('database', 4), ('table', 4), ('sqlite', 4), ('mysql', 4), ('phpmyadmin', 4),
    ('chatgpt', 5), ('ai', 5), ('afpa', 5), ('david', 5), ('cda', 5)
]

# 插入示例数据到Themes表
cursor.executemany('INSERT INTO Themes (name) VALUES (?)', themes_data)

# 插入示例数据到Words表
cursor.executemany(
    'INSERT INTO Words (word, theme_id) VALUES (?, ?)', words_data)

# 提交更改并关闭数据库连接
conn.commit()
conn.close()
