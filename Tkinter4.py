import tkinter as tk

window = tk.Tk()
en_password = tk.Entry(window, show='*')
en_password.pack()

def showhide_password():
    # if else để kiểm tra
    if chbx_showhide_val.get() == 1:
        en_password.config(show="*")
    else:
        en_password.config(show="")

chbx_showhide_val = tk.IntVar() # tạo biến int
chbx_showhide = tk.Checkbutton(
    window, text="ẩn/ hiện mật khẩu",
    command= showhide_password,
    variable= chbx_showhide_val, onvalue=1, offvalue=0
)
chbx_showhide.pack()
# tìm cách tắt
# bắt được cái event click vào nút


window.mainloop()
