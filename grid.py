import tkinter
from tkinter import ttk

ws=tkinter.Tk()
ws.ttle("Grid Test")

cv=tkinter.Canvas(ws,width=50, height=50,bg="gray")
ws.grid_propagate(0)
cv.grid(column=0,row=0)

ws.geometry("165x165")

cv1=tkinter.Canvas(ws,width=50,height=50,bg="light gray")
cv1.grid(row=1, column=1)

cv2=tkinter.Canvas(ws,width=50,height=50,bg="lightblue")
cv2.grid(column=2,row=2)

cv3=tkinter.Canvas(ws,width=50,height=50,bg="red")
cv3.grid(row=0,column=2,rowspan=2)
cv3.config(height=100)

cv4=tkinter.Canvas(ws,width=50,height=50,bg="lightgreen")
cv4.grid(row=2,column=0,columnspan=2)
cv4.config(width=100)

