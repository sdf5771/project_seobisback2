
from tkinter import filedialog
from tkinter import Button
from tkinter import Label
from tkinter import *

main = Tk()
#화면 제목 작업표시줄
main.title("FLCL")
#화면크기
main.geometry("640x480")
#화면크기 고정 앞에부터 x(너비),y(높이)
main.resizable(False,False)

#파일추가

def add_file():
        files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("PNG 파일","*.png"),("모든 파일", "*.*")))
        add_path = Label(main,text=files)
        add_path.pack()

       
add_file_btn = Button(main,text="사진찾기",command=add_file)
add_file_btn.pack()
add_path = Label(main,text="유후")
add_path.pack()



#화면이 닫치지않게하는
main.mainloop()
