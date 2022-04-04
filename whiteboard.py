from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root=Tk()
root.title("White Board")
root.geometry("1050x570+150+50")
root.configure(bg="#FF5733")
root.resizable(True,True)

current_x=0
current_y=0
color='black'

def locate_xy(work):
	global current_x,current_y
	current_x=work.x
	current_y=work.y

def addLine(work):
	global current_x,current_y
	canvas.create_line((current_x,current_y,work.x,work.y),width=2,fill=color)
	current_x,current_y=work.x,work.y

def show_color(new_color):
	global color
	color=new_color

def new_canvas():
	canvas.delete('all')
	display_pallete()
	

#icon
image_icon=PhotoImage(file="board.png")
root.iconphoto(False,image_icon)

color_box=PhotoImage(file="color section.png")
Label(root,image=color_box,bg="#FF5733").place(x=10,y=20)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,bg="#FF5733",command=new_canvas).place(x=31,y=435)


colors=Canvas(root,bg="#ffffff",width=37,height=350,bd=2)
colors.place(x=28,y=70)

def display_pallete():
	id=colors.create_rectangle((10,10,30,30),fill='black')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('black'))

	id=colors.create_rectangle((10,40,30,60),fill='gray')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('gray'))

	id=colors.create_rectangle((10,70,30,90),fill='brown4')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('brown4'))

	id=colors.create_rectangle((10,100,30,120),fill='red')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('red'))

	id=colors.create_rectangle((10,130,30,150),fill='yellow')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('yellow'))

	id=colors.create_rectangle((10,160,30,180),fill='green')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('green'))

	id=colors.create_rectangle((10,190,30,210),fill='pink')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('pink'))

	id=colors.create_rectangle((10,220,30,240),fill='orange')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('orange'))

	id=colors.create_rectangle((10,250,30,270),fill='blue')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('blue'))

	id=colors.create_rectangle((10,280,30,300),fill='cyan')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('cyan'))

	id=colors.create_rectangle((10,310,30,330),fill='crimson')
	colors.tag_bind(id,'<Button-1>',lambda x:show_color('crimson'))

	

display_pallete()


canvas=Canvas(root,bg="#ffffff",width=5000,height=760,background="white",cursor="hand2",bd=2)
canvas.place(x=100,y=-10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>',addLine)


##############Slider for thickness##################

#current_value=tk.DoubleVar()

#def get_current_value():
#	return '{: .2f}'.format(current_value.get())

#def slider_changed(event):
#	value_label.configure(text=get_current_value())

#slider=ttk.Scale(root,from_=0,to=50,orient='horizontal',command=slider_changed,variable=current_value)
#slider.place(x=3,y=530)

#value label
#value_label=ttk.Label(root,text=get_current_value())
#value_label.place(x=27,y=500)


root.mainloop()