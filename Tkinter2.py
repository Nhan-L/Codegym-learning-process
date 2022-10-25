import tkinter as tk

cuaso = tk.Tk()
cuaso.geometry()

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

# tạo label
lbpack = tk.Label( cuaso, text="label pack", bg="red" )
lbpack.place(relx= 0.5, y=0, anchor=tk.NE)

lbpack1 = tk.Label( cuaso, text="label pack", bg="blue" )
lbpack1.place(relx= 0.5, y=0)

lbpack2 = tk.Label( cuaso, text="label pack", bg="yellow" )
lbpack2.place(relx= 0.5, y=0, anchor=tk.N)



# lbpack.place(relx=0.5, rely=0.8)

# tính độ dài của thằng cha ( cuaso)
# tính độ dài của label 
# /2 - độ dài label /2



cuaso.mainloop()
