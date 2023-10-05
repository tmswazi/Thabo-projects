#import turtle

#def main():
 #turtle.shape("turtle")
 #turtle.mode("logo")
 #num_petals = turtle.numinput('Amount Window', 'Enter the number of petals (must be an even number): ')
 #stem_length = turtle.numinput('Length Window', 'Enter the length of stem: ')
 #petal = turtle.textinput('Petal Window', 'Enter the petal type (triangle, square, or pentagon): ')
 #petal_size = turtle.numinput('Size Window', 'Enter the length of side: ')
 #stem_colour = turtle.textinput('Colour Window', 'Enter the stem colour: ')
 #petal_colour = turtle.textinput('Colour Window', 'Enter the first petal colour: ')
 #petal_colour1 = turtle.textinput('Colour Window', 'Enter the second petal colour: ')
 
 
 #angle = 0
 #colour = 1
 #if petal == 'triangle': # code to print triangle
  #for i in range(int(num_petals)): 
   #turtle.forward(stem_length)
   #turtle.left(30)
   #for i in range(3): 
    #if colour%2 != 0:
     #turtle.pencolor(petal_colour)
    #else: 
     #turtle.pencolor(petal_colour1)
    #turtle.forward(petal_size)
    #turtle.right(360/3)
   #turtle.pencolor(stem_colour)
   #turtle.home()
   #angle += (360/(num_petals)) 
   #turtle.right(angle) 
   #colour += 1
  #turtle.pencolor(petal_colour)
  #turtle.exitonclick()
  
 #elif petal == 'pentagon': # code to print pentagon
  #for i in range(int(num_petals)):  
   #turtle.forward(stem_length)
   #turtle.left(54)
   #for i in range(5): 
    #if colour%2 != 0:
     #turtle.pencolor(petal_colour)
    #else:
     #turtle.pencolor(petal_colour1)    
    #turtle.forward(petal_size)
    #turtle.right(360/5)
   #turtle.pencolor(stem_colour)
   #turtle.home()
   #angle += (360/(num_petals))
   #turtle.right(angle)
   #colour += 1
  #turtle.pencolor(petal_colour)
  #turtle.exitonclick()   
  
 #elif petal == 'square': # code to print square 
  #for i in range(int(num_petals)):   
   #turtle.forward(stem_length)
   #turtle.left(45)
   #for i in range(4): 
    #if colour%2 != 0: 
     #turtle.pencolor(petal_colour)
    #else: 
     #turtle.pencolor(petal_colour1)     
    #turtle.forward(petal_size)
    #turtle.right(360/4)
   #turtle.pencolor(stem_colour) 
   #turtle.home()
   #angle += (360/(num_petals)) 
   #turtle.right(angle)
   #colour += 1
  #turtle.pencolor(petal_colour)
  #turtle.exitonclick()
   
#main()  

import turtle

def main():
 turtle.shape("turtle")
 turtle.mode("logo")
 num_petals = turtle.numinput('Number Window', 'Enter the number of petals (must be an even number): ')
 stem_size = turtle.numinput('Size Window', 'Enter the length of stem: ')
 petal_type = turtle.textinput('Type Window', 'Enter the petal type (triangle, square, or pentagon): ')
 petal_size = turtle.numinput('Size Window', 'Enter the length of side: ')
 stem_colour = turtle.textinput('Colour Window', 'Enter the stem colour: ')
 petal_colour1 = turtle.textinput('Colour Window', 'Enter the first petal colour: ')
 petal_colour2 = turtle.textinput('Colour Window', 'Enter the second petal colour: ')
 
 angle = 360/num_petals
 angle_accumulator = 1
 colour_determinor = 1 
 turtle.right(angle)
 turtle.speed(0)
 if petal_type == 'triangle':
  for i in range(0, int(num_petals)): 
   for i in range(1): 
    turtle.forward(stem_size)
    turtle.left(30)
   for i in range(0, 3): 
    if colour_determinor%2 != 0:
     turtle.pencolor(petal_colour1)
    else: 
     turtle.pencolor(petal_colour2)
    turtle.forward(petal_size)
    turtle.right(360/3)
   turtle.pencolor(stem_colour)
   turtle.home()
   angle_accumulator += 1
   angle = angle_accumulator*(360/(num_petals)) 
   turtle.right(angle) 
   colour_determinor += 1 
  turtle.home()
  turtle.pencolor(petal_colour1)
  turtle.exitonclick()
  
 elif petal_type == 'square': 
  for i in range(0, int(num_petals)): 
   for i in range(1):  
    turtle.forward(stem_size)
    turtle.left(45)
    for i in range(0, 4): 
     if colour_determinor%2 != 0:
      turtle.pencolor(petal_colour1)
     else: 
      turtle.pencolor(petal_colour2)     
     turtle.forward(petal_size)
     turtle.right(360/4)
   turtle.pencolor(stem_colour) 
   turtle.home()
   angle_accumulator += 1 
   angle = angle_accumulator*(360/(num_petals)) 
   turtle.right(angle)
   colour_determinor += 1 
  turtle.home()
  turtle.pencolor(petal_colour1)
  turtle.exitonclick()
 
 elif petal_type == 'pentagon': 
  for i in range(0, int(num_petals)): 
   for i in range(1): 
    turtle.forward(stem_size)
    turtle.left(54)
   for i in range(0, 5): 
    if colour_determinor%2 != 0:
     turtle.pencolor(petal_colour1)
    else:
     turtle.pencolor(petal_colour2)    
    turtle.forward(petal_size)
    turtle.right(360/5)
   turtle.pencolor(stem_colour)
   turtle.home()
   angle_accumulator += 1
   angle = angle_accumulator*(360/(num_petals))
   turtle.right(angle)
   colour_determinor += 1
  turtle.home()
  turtle.pencolor(petal_colour1)
  turtle.exitonclick()  
   
main()