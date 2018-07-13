from tkinter import *
import random
import time

root=Tk()

counter =0
counter_1=0
root.title("Pong")
root.resizable(0,0)
root.wm_attributes("-topmost",1) 

#canvas:
canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0,bg='yellow')
canvas.create_line(0,250,500,250,fill='red')
oval=canvas.create_oval(40,40,175,175,fill='green')
canvas.move(oval,135,150)
canvas.pack()
root.update()

#Ball class
class Ball:

    
   def __init__(self,canvas,paddle,paddle1,color):
        self.canvas=canvas
        self.paddle=paddle
        self.paddle1=paddle1
        
        self.id=canvas.create_oval(20,20,45,45,fill=color)
        self.canvas.move(self.id,300,250)
        post=[-3,-2,-1,0,1,2,3]
        random.shuffle(post)
        self.x=post[0]
        self.y=-3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        
        
   def hit_paddle(self,pos):
      paddle_pos=self.canvas.coords(self.paddle.id)
      if pos[2]>=paddle_pos[0]and pos[0]<=paddle_pos[2]:
         if pos[3]>=paddle_pos[1]and pos[3]<=paddle_pos[3]:
            return True
         return False
      
   def hit_paddle1(self,pos):
      paddle1_pos=self.canvas.coords(self.paddle1.id)
      if pos[2]>=paddle1_pos[0]and pos[2]<=paddle1_pos[2]:
         if pos[1]>=paddle1_pos[1]and pos[1]<=paddle1_pos[3]:
            return True
         return False
                                             
   def draw(self):
      self.canvas.move(self.id,self.x,self.y)
      pos=self.canvas.coords(self.id)
      if pos[1]<=0:
         self.y=3
         self.score_counter(False)
      if pos[3]>=self.canvas_height:
         self.y=-3
         self.score_counter(True)
      if pos[0]<=0:
         self.x=3
      if pos[2]>=self.canvas_width:
         self.x=-3
      if self.hit_paddle(pos)==True:
         self.y=-3
      if self.hit_paddle1(pos)==True:
         self.y=3
   def score_counter(self,val):
      global counter
      global counter_1
      if val==True:
         a=self.canvas.create_text(100,200,text=counter,font=('Times',23),fill='black')
         canvas.itemconfig(a,fill='yellow')
         counter+=1
         a=self.canvas.create_text(100,200,text=counter,font=('Times',23),fill='black')
      if val==False:
         b=self.canvas.create_text(100,300,text=counter_1,font=('Times',23),fill='black')
         canvas.itemconfig(b,fill='yellow')
         counter_1+=1
         b=self.canvas.create_text(100,300,text=counter_1,font=('Times',23),fill='black')
         
      
    
        

# paddle class
class Paddle:

    
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,20,fill=color)
        self.canvas.move(self.id,200,480)
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
        self.x=0
        
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
             self.x=0
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2

        
# class paddle 2:


class Paddle1:
   def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(100,20,0,0,fill=color)
        self.canvas.move(self.id,200,0)
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('a',self.turn_left)
        self.canvas.bind_all('d',self.turn_right)
        self.x=0
        
   def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0
        if pos[2]>=self.canvas_width:
             self.x=0
   def turn_left(self,evt):
        self.x=-2
        
   def turn_right(self,evt):
        self.x=2
        
paddle=Paddle(canvas,'blue')
paddle1=Paddle1(canvas,'black')

ball=Ball(canvas,paddle,paddle1,'red')


while 1:
   ball.draw()
   paddle.draw()
   paddle1.draw()
   if counter==10:
      ball.y=0
      ball.y=0
      paddle.x=0
      paddle.x=0
      canvas.create_text(100,200,text='Black player win!!',fill='red',font=('Times',45))
   root.update_idletasks()
   root.update()
   time.sleep(0.01)
   
      

root.mainloop()
