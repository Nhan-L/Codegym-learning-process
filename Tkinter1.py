# https://www.pythontutorial.net/tkinter/tkinter-label/
# tạo cửa sổ
from turtle import window_width
import tkinter as tk
cuaso = tk.Tk()
cuaso.title("Đây là chương trình đầu tiên của tôi")
screen_width = cuaso.winfo_screenwidth()
screen_height = cuaso.winfo_screenheight()

win_width = 500
win_height = 300

cuaso.geometry("{}x{}+{}+{}".format(
    win_width,
    win_height,
    screen_width//2 - (win_width//2), 
    screen_height//2 - (win_height//2))
)

lbl_alert = tk.Label(
    cuaso, 
    text="Nhập thông tin",
)
lbl_alert.pack()

lbl_user = tk.Label(
    cuaso, 
    text="UserName",
)
lbl_user.pack()

en_user = tk.Entry()
en_user.pack()

lbl_password = tk.Label(
    cuaso, 
    text="Password",
)
lbl_password.pack()

en_password = tk.Entry()
en_password.pack()

btn_login = tk.Button(
    cuaso, text="Đăng nhập"
)
btn_login.pack()



cuaso.mainloop()


