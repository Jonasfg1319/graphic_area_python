import sys
from tkinter import Label
from tkinter import Tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk


import os

class Solution ( object ):
    cont = 0   
    graphic = ["graphic1.png","graphic2.png","graphic3.png","graphic4.png","graphic5.png","graphic6.png","graphic7.png","graphic8.png"]
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Área da água")
        #self.create_button()
        self.create_image()
        self.poll()
        self.root.mainloop()
        
               
        

    def maxArea ( self , height ):
      area = 0
      if(height != []):
         for l in range(len(height)):
           for c in range(len(height)):
             mi = min(height[l], height[c])
             area = max(area, mi * (c - l) ) 
      return area
    

    def maxAreaOnePass ( self , height ):
      area = 0
      if(height != []):
        p = 0
        u = len(height) -1
        while p < u:
            mi = min(height[p],height[u])
            area = max(area, mi * (u - p))
            if height[p] > height[u]:
                u -= 1
            else:
                p += 1
      return area

    def poll( self ):
         self.draw()
         self.root.after(650, self.poll)

    def create_button(self):
        botao_start = ttk.Button(self.root, text="Iniciar", command=self.animate)
        botao_start.pack(sid="right")

    def create_image(self):
        self.image = ImageTk.PhotoImage(Image.open((self.graphic[self.cont]))) 
        self.cicle = Label(self.root, image=self.image)
        self.cicle.image = self.image
        self.cicle.pack()     
    
    def draw(self):
          if(self.cont >= 7):
	          self.cont = 0
          self.animate()
    
    def change(self):
        print(self.scale.get())
    
    def animate(self):
        img = ImageTk.PhotoImage(Image.open(self.graphic[self.cont]))
        self.cicle.configure(image = img)
        self.cicle.image = img
        self.cicle.pack()
        self.cont+=1

    
	       
	     

    ## Main program for testing .
def main ():
     test = [ [1 ,1] ,
     [1 ,8 ,6 ,2 ,5 ,4 ,8 ,3 ,7] ,
     [4 ,3 ,2 ,1 ,4] ,
     [] ,
     [1 ,2 ,1] ,
     [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9] ]
     s = Solution()
        
     for t in test:
       r1 = s.maxArea(t)
       r2 = s.maxAreaOnePass(t)
       print ( "{} = {} = {}".format(t,r1 ,r2 ))
        
if __name__ == " __main__ ":
      sys.exit(main())

main()

s = Solution()