from tkinter import*
import random
import time

root1=Tk()
root1.title('padlock')
canvas=Canvas(root1, width=500, height=250, bg='#000000')
canvas.pack()
text=Entry(width=30)
text.place(x=200,y=100)
x=False
canvas.create_text(120,110,text='Enter the password',fill='white')

L3=[]

def onclick1():
    text.insert(10987123,'1')
    
    L3.append('1')
def onclick2():
    text.insert(42612561,'2')
    
    L3.append('2')
def onclick3():
    text.insert(42834123,'3')
    
    L3.append('3')
def onclick4():
    text.insert(46519876,'4')
    
    L3.append('4')
def onclick5():
    text.insert(49721854,'5')
    
    L3.append('5')
def onclick6():
    text.insert(59767320,'6')
    
    L3.append('6')
def onclick7():
    text.insert(60000000,'7')
    
    L3.append('7')
def onclick8():
    text.insert(62000000,'8')
    
    L3.append('8')
def onclick9():
    text.insert(64000000,'9')
    
    L3.append('9')
def onclick10():
    text.insert(67000000,'0')
    L3.append('0')
def onclick11():
    global x
    x=False
   
    for i in range(len(L3)-1):
        L3[0]=L3[0]+L3[i+1]
        
    
    if L3[0]=='2001':
        x=True
        root1.destroy()
        game()

btn1=Button(text='1', fg='#255',height=2,width=4,state='normal',command=onclick1)
btn1.place(x=200,y=120)
btn1.bind()
btn2=Button(text='2', fg='#255',height=2,width=4, state='normal',command=onclick2)
btn2.place(x=240,y=120)
btn2.bind()
btn3=Button(text='3', fg='#255',height=2,width=4, state='normal',command=onclick3)
btn3.place(x=280,y=120)
btn3.bind()
btn4=Button(text='4', fg='#255',height=2,width=4, state='normal',command=onclick4)
btn4.place(x=200,y=160)
btn4.bind()
btn5=Button(text='5', fg='#255',height=2,width=4, state='normal',command=onclick5)
btn5.place(x=240,y=160)
btn5.bind()
btn6=Button(text='6', fg='#255',height=2,width=4, state='normal',command=onclick6)
btn6.place(x=280,y=160)
btn6.bind()
btn7=Button(text='7', fg='#255',height=2,width=4, state='normal',command=onclick7)
btn7.place(x=200,y=200)
btn7.bind()
btn8=Button(text='8', fg='#255',height=2,width=4, state='normal',command=onclick8)
btn8.place(x=240,y=200)
btn8.bind()
btn9=Button(text='9', fg='#255',height=2,width=4, state='normal',command=onclick9)
btn9.place(x=280,y=200)
btn9.bind()
btn10=Button(text='0', fg='#255', height=2, width=4, state='normal', command=onclick10)
btn10.place(x=320, y=120)
btn10.bind()
btn11=Button(text='Enter', fg='#255', height=2, width=4, state='normal', command=onclick11)
btn11.place(x=320, y=160)
btn11.bind()


def game():
    
    root=Tk()
    root.title('Game')
    root.resizable(0,0)
    root.wm_attributes('-topmost',1)
    canvas=Canvas(root, width=500, height=500,bd=0,highlightthickness=0,bg='#000000')
    canvas.pack()
    root.update()
    
    x=0
    y=0
    x1=50
    y1=30
    L=[]
    L1=[]
    L2=[0]
    p=0
    def onclick():
        btn.destroy()
        
        class Ball:

            def __init__(self, canvas, paddle, brick, color):
                self.canvas=canvas
                self.paddle=paddle
                self.brick=brick
                self.id=canvas.create_oval(10,10,25,25,fill=color)

                
                    
                self.canvas.move(self.id, 245, 100)
                self.x=4
                self.y=-2
                self.canvas_height=self.canvas.winfo_height()
                self.canvas_width=self.canvas.winfo_width()
                self.hit_bottom=False
                
                
            def hit_paddle(self,pos):
                paddle_pos=self.canvas.coords(self.paddle.id)
                if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
                    if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                        
                        return True
                    
                    return False

            def hit_brick(self, pos):
                    for i in range(10):
                        
                        if i==0:
                            x=0
                            y=0
                            x1=50
                            y1=30
                            brick_pos=[x, y, x1, y1]
                            if brick_pos in L1:
                                canvas.tag_raise(self.id)
                                continue
                                
                                
                            if pos[0]<=brick_pos[2] and pos[2]>=brick_pos[0]:
                                if pos[1]<=brick_pos[3] and pos[3]>=brick_pos[3]:
                                    void=canvas.create_rectangle(290,460,380,500,fill='black')
                                    canvas.tag_raise(self.id)
                                    L2[0]=L2[0]+10
                                    L.append(brick_pos)
                                    
                                    score=canvas.create_text(310, 480, text=L2, font=('Times', 30), fill='green')
                                    return True
                                    
                                    
                                return False

                        elif i!=0 and i<10:
                            x+=50
                            y=0
                            x1+=50
                            y1=30
                            brick_pos=[x, y, x1, y1]
                            if brick_pos in L1:
                                canvas.tag_raise(self.id)
                                continue
                            if pos[0]<=brick_pos[2] and pos[2]>=brick_pos[0]:
                                if pos[1]<=brick_pos[3] and pos[3]>=brick_pos[3]:
                                    void=canvas.create_rectangle(290,460,380,500,fill='black')
                                    canvas.tag_raise(self.id)
                                    L2[0]=L2[0]+10
                                    L.append(brick_pos)
                                    
                                    score=canvas.create_text(310, 480, text=L2, font=('Times', 30), fill='green')
                                    return True
                                    
                                return False         
                    
            def draw(self):
                self.canvas.move(self.id, self.x, self.y)
                pos=self.canvas.coords(self.id)
                
                if pos[1]<=0:
                    self.y=2

                if pos[0]<=0:
                    self.x=2

                if pos[3]>=self.canvas_height:
                    self.hit_bottom=True
                    
                    canvas.create_text(245, 100, text='Game Over',font=('Times',30),fill='red')
                                   
                if pos[2]>=self.canvas_width:
                    self.x=-2
            
                if self.hit_paddle(pos)==True:
                    self.y=-2

                if self.hit_brick(pos)==True:
                    self.y=2
                    
                    void=canvas.create_rectangle(*L[0], fill='black')
                    
                    L1.append(L[0])
                    L.clear()
                    
                if L2[0]==100:
                    self.hit_bottom=True
                    canvas.create_text(245, 100, text='Success',font=('Times',30),fill='red')
            
        class Paddle:

            def __init__(self, canvas, color):
                self.canvas=canvas
                self.id=canvas.create_rectangle(10, 10,90, 20,fill=color)
                
                self.canvas.move(self.id,245, 300)
                
                self.x=0
                
                self.canvas_width=self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-a>',self.turn_left)
                self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
                self.canvas.bind_all('<KeyPress-A>',self.turn_left)
                self.canvas.bind_all('<KeyPress-D>',self.turn_right)
                self.canvas.bind_all('<KeyPress-d>',self.turn_right)
                self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

            def draw(self):
                self.canvas.move(self.id,self.x,0)
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                    self.x=2
                if pos[2]>=self.canvas_width:
                    self.x=-2

            def turn_left(self,evt):
                self.x=-2

            def turn_right(self,evt):
                self.x=2

        class Brick:

            def __init__(self,canvas, color):
                
                for i in range(10):

                    if i==0:
                        x=0
                        y=0
                        x1=50
                        y1=30
                        self.canvas=canvas
                        
                        self.id=canvas.create_rectangle(x,y,x1,y1,fill=color)
                        canvas.tag_lower(self.id)
                        
                        self.x=0
                        
                        
                    elif i!=0 and i<10:
                        x+=50
                        y=0
                        x1+=50
                        y1=30
                        self.canvas=canvas
                        
                        self.id=canvas.create_rectangle(x,y,x1,y1,fill=color)
                        
                        
                        self.x=0

           
                 
                    
        brick=Brick(canvas, 'orange')        
        paddle=Paddle(canvas,'blue')
        ball=Ball(canvas,paddle,brick, 'red')
        canvas.create_text(235, 480, text='Score:', font=('Times', 30), fill='green')
        randomLIST=[]
        randomLIST1=[]
        while 1:
            
            if ball.hit_bottom==False:        
                ball.draw()
                paddle.draw()
            elif ball.hit_bottom==True:
                
                end_time=time.perf_counter()
                randomLIST.append(end_time)
                randomLIST1.append(randomLIST[0])
                randomLIST.clear()
                
                if abs(end_time-randomLIST1[0]>=3) and abs(end_time-randomLIST1[0]<=4):
                    PlaySound(None, SND_ASYNC)
                    root.destroy()
            
                
            
                
                
            
            root.update_idletasks()
            root.update()
            time.sleep(0.01)
    btn=Button(text='Play', bg='#0000ff', fg='#00ff00',width=30,height=3,state='normal', command=onclick)
    btn.place(x=140, y=200)
    root.mainloop()
root1.mainloop()
