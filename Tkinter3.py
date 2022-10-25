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


redbutton = tk.Button(cuaso, text="Red", fg="red")
redbutton.pack( side = tk.LEFT)

greenbutton = tk.Button(cuaso, text="green", fg="green")
greenbutton.pack( side = tk.LEFT)

bluebutton = tk.Button(cuaso, text="Blue", fg="blue", bg="PINK")
bluebutton.pack( side = tk.LEFT, expand=True, fill= tk.BOTH)

blackbutton = tk.Button(cuaso, text="Black", fg="black")
blackbutton.pack( side = tk.BOTTOM)



cuaso.mainloop()
