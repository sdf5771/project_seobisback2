
import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import Button
from tkinter import Label
from PIL import ImageTk, Image

main = tk.Tk()
#화면 제목 작업표시줄
main.title("FLCL")
#화면크기
main.geometry("640x480")
#화면크기 고정 앞에부터 x(너비),y(높이)
# main.resizable(False,False)

#파일추가
def add_file():
        files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",\
        filetypes=(("jpeg 파일","*.jpeg"),("모든 파일", "*.*")))
        return files


result = add_file()
image_test2=Image.open(result[0])
img2 = ImageTk.PhotoImage(image_test2)
image_Label2=Label(main,image=img2)
image_Label2.pack()
# a= "/Users/kzsc5464/Documents/GitHub/project_seobisback2/test1.jpeg"
# b= result_path
# c=b.items()
# image_test=Image.open(c)
# img = ImageTk.PhotoImage(image_test)
# image_Label1=Label(main,image=img)
# image_Label1.pack()
add_file_btn = Button(main,text="사진찾기",command=add_file)
add_file_btn.pack()




#화면이 닫치지않게하는
main.mainloop()
