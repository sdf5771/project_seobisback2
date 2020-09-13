import tkinter as tk
from tkinter import Button
from tkinter import dialog

main = tk.Tk()
main.geometry("640x800")
main.title("FLFC")
main.mainloop

def add_file():
        files = tk.filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("PNG 파일","*.png"),("모든 파일", "*.*")))
        print(files)
       
add_file_btn = Button(main,text="사진찾기",command=add_file)
add_file_btn.pack()