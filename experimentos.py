# https://stackoverflow.com/questions/9348264/does-tkinter-have-a-table-widget
# https://github.com/clarenceangel/tkinterstuff

# from tkinter import *

# root = Tk()

# height = 5
# width = 5
# # for i in range(height): #Rows
# #     for j in range(width): #Columns
# #         b = Entry(root, text="")
# #         b.grid(row=i, column=j)

# # # # mainloop()

# from tkinter import *

# def checkered(canvas, line_distance):
#    # vertical lines at an interval of "line_distance" pixel
#    for x in range(line_distance,canvas_width,line_distance):
#       canvas.create_line(x, 0, x, canvas_height, fill="#476042")
#    # horizontal lines at an interval of "line_distance" pixel
#    for y in range(line_distance,canvas_height,line_distance):
#       canvas.create_line(0, y, canvas_width, y, fill="#476042")


# master = Tk()
# canvas_width = 800
# canvas_height = 500
# w = Canvas(master, 
#            width=canvas_width,
#            height=canvas_height)
# w.pack()

# checkered(w,100)

# mainloop()

# from tkinter import *

def checkered(canvas, line_distancex,line_distancey):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distancex,canvas_width,line_distancex):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distancey,canvas_height,line_distancey):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


master = Tk()
canvas_width = 800
canvas_height = 500
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()

checkered(w,100,60)

mainloop()

