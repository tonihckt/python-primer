#libreria dibujar lineas
import turtle

#capturamos los movimientos
window = turtle.Screen()
window.screensize(200, 200 , "black")

colors = ['red', 'blue']

#instanciamos
trtl = turtle.Turtle()
#trtl = turtle.Pen()
trtl.color("red")
trtl.pensize(30)
##trtl.speed(0.00025)


for x in range(360):
    trtl.pencolor(colors[x%2])
    #trtl.pencolor(colors[1])
    trtl.width(x/100+1)
     #Se mueve 100 pixeles hacia adelante
    #trtl.forward(100)
    trtl.forward(x)
    #Gira x grados a la derecha
    trtl.right(90) #cudrado
    #trtl.left(60) 


'''
for x in range (50,100,10):
    for trng in range(3):
        trtl.forward(x)
        trtl.left(120)
'''     

'''
#movimientos hacide delante
trtl.forward(100)
#cantidad de grados
trtl.right(90)
'''

#no se cierra la ventana hasta la orden
#turtle.mainloop()
turtle.done()
window.mainloop()