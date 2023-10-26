from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

window = Tk()

# processing icon image to Photoimage
icon = PhotoImage(file='icon.png')

window.title('Sketchpad using Tkinter')
window.geometry('1100x610')
window.configure(bg='black')
window.iconphoto(True,icon)

#color picker
chose_color = PhotoImage(file='box.png')
Label(image=chose_color,borderwidth=0,padx=9).place(x=15,y=10)

    
def new_canvas():
    draw_canvas.delete('all')
    color_picker()
    


#eraser
eraser = PhotoImage(file='er-removebg-preview.png')
Button(window,command=new_canvas, image=eraser,compound='top',borderwidth=0).place(x=40,y=530)

#color picker
colors = Canvas(window, bg='#ffffff',width=37,height=470,bd=0)
colors.place(x=43,y=41)

current_x = 0
current_y = 0
color = 'black'

def locate_pointer(pointer):
    global current_x, current_y
    
    current_x = pointer.x
    current_y = pointer.y
    

    
    
def show_color(new_color):
    global color
    
    color = new_color

def chose():
    global color
    color = askcolor()[1]
    #print(color)

#color_choser_btn = 0
color_choser_btn = Button(window,height=3,width=3,command=chose,font=('Verdena',11),bg='black',fg='white',text='pick')
color_choser_btn.place(x=45,y=450)


draw_canvas = Canvas(window, width=940, height=560,background='white',cursor='hand2')
draw_canvas.place(x=140, y=26)

line_width = 2
line_width = Scale(window,fg='#000000',bg='#40ff56',from_=1,orient='horizontal',length=400,to=20)
line_width.set(2)
line_width.place(x=150,y=530)

print(line_width.get())
    
def Addline(pointer):
    global current_x, current_y
    
    draw_canvas.create_line((current_x,current_y,pointer.x,pointer.y),width=line_width.get(),fill=color)
    current_x,current_y = pointer.x, pointer.y

def color_picker():
    id = colors.create_rectangle((10,10,30,30),fill='black')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('black'))
    
    id = colors.create_rectangle((10,40,30,60),fill='red')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('red'))
    
    id = colors.create_rectangle((10,70,30,90),fill='white')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('white'))
    
    id = colors.create_rectangle((10,100,30,120),fill='yellow')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('yellow'))
    
    id = colors.create_rectangle((10,130,30,150),fill='blue')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('blue'))
    
    id = colors.create_rectangle((10,160,30,180),fill='green')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('green'))
    
    id = colors.create_rectangle((10,190,30,210),fill='violet')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('violet'))
    
    id = colors.create_rectangle((10,220,30,240),fill='pink')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('pink'))
    
    id = colors.create_rectangle((10,250,30,270),fill='light blue')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('light blue'))
    
    id = colors.create_rectangle((10,280,30,300),fill='orange')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('orange'))
    
    id = colors.create_rectangle((10,310,30,330),fill='gray')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('gray'))
    
    id = colors.create_rectangle((10,340,30,360),fill='light green')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('light green'))
    
    id = colors.create_rectangle((10,370,30,390),fill='cyan')
    colors.tag_bind(id, '<Button-1>',lambda x: show_color('cyan'))
    
    """ id = colors.create_rectangle((10,400,30,420),fill=color)
    colors.tag_bind(id,'<Button-1>',lambda x: show_color(color)) """
    
    
color_picker()

draw_canvas.bind('<Button-1>', locate_pointer)
draw_canvas.bind('<B1-Motion>', Addline)

window.mainloop()

