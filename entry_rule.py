import tkinter
from tkinter import messagebox


root = tkinter.Tk()
root.title('入力規則テスト')
root.geometry('500x500')
root.resizable(0, 0)

# フレームの作成
entry_flame = tkinter.Frame(root)
button_flame = tkinter.Frame(root)
entry_flame.pack()
button_flame.pack()

def show_message():
    messagebox.showinfo('お知らせ', 'お知らせです')

def limit_character(string):
    boolena_limit = len(string) <= 5
    return boolena_limit

def least_character(string):
    if len(string) >= 5:
        button_1['state'] = 'normal'

    return True

# 文字数制限の検証関数
vc_1 = root.register(limit_character)
vc_2 = root.register(least_character)


# エントリーの作成
entory_1 = tkinter.Entry(entry_flame, width=30, validate='key', validatecommand=(vc_1, '%P')) # %Pで引数にパラメーターを渡す
entory_2 = tkinter.Entry(entry_flame, width=30, validate='key', validatecommand=(vc_2, '%P'))

entory_1.grid(row=0, column=0, padx=70, pady=10)
entory_2.grid(row=1, column=0, padx=70, pady=(0, 10))

# ボタンの作成
button_1 = tkinter.Button(button_flame, text='テスト', state='disabled', command=show_message)
button_1.grid(row=2, column=1, padx=70, ipadx=10)

root.mainloop()