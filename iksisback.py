import tkinter
import os
from tkinter import filedialog
from tkinter import Button
#익이전용 UI 프로젝트 건드리지마시오
main = tkinter.Tk()
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
        print(files)
        # faceimage = tkinter.PhotoImage(file = files)
        

# faceimage=tkinter.PhotoImage(file = "test1.png")

# facelabel = tkinter.Label(main, image = faceimage)
# facelabel.pack()

add_file_btn = Button(main,text="사진찾기",command=add_file)
add_file_btn.pack()



#화면이 닫치지않게하는
main.mainloop()
