import tkinter
from matplotlib import pyplot as  plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from customtkinter import CTk,CTkFrame,CTkEntry,CTkLabel,CTkButton
from tkinter import PhotoImage
import numpy as np
import math
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style


# Declaracion de colores

c_negro='#010101'
root=CTk()
root.geometry('480x800+350+100')
root.minsize(480,500)
root.maxsize(480,1300)
root.config(bg='white')

#Declaracion de imagenes a utilizar como favicon y botones

Logo= PhotoImage(file='images/shapes.png')
root.call('wm','iconphoto',root._w,Logo)

#Declaracion del frame
frame= CTkFrame(root,fg_color='white')
frame.grid(column=0,row=0,sticky='nsew',padx=50,pady=50)

#COnfiguracion de columnas del root

root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

# Definicion y ubicacion de los labels y bottones

label=CTkLabel(frame,text="Bienvenido a GRotation.A continuacion se presenta el\n software  de ilustracion de operadores rotacionales. ",text_color='black',width=300,height=75,anchor=tkinter.CENTER,font=('Open Sans',15))
label.grid(column=0,row=0,sticky='nsew')

label2=CTkLabel(frame,text="A.Ingrese el valor del angúlo de rotación en Degrees",text_color='black',width=300,height=50,anchor='w',font=('Open Sans',15),padx=25)
label2.grid(column=0,row=1,sticky='nsew')

angle=CTkEntry(frame,placeholder_text='Ingrese el valor de angulo',border_color='#bfff00',fg_color='white',width=350,height=50,text_color='black')
angle.grid(columnspan=2,row=2,padx=20,pady=10)

#Definicion funcion de comando de boton

def capture_angulo():
 variation=float(angle.get())
 Rotation(variation)


boton1=CTkButton(master=frame,text="Calcular frame B rotado",text_color='black',width=100,height=50,fg_color='#bfff00',anchor='CENTER',command=capture_angulo)
boton1.grid(column=0,row=3)

#Inicio Subprograma captura de la figura

def Rotation(anguloz):


#Captura y toma de datos por parte del usuario

    Rotation_grade=float(anguloz)

    # Descripcion y  Plotting del frame {A}
    # Unitarian Axes Xa,Ya,Za

    XA = [1,0,0]
    YA = [0,1,0]
    ZA = [0,0,1]

    PA=np.array([[1,0,0],[0,1,0],[0,0,1]])


    # Creating the Origin vector, setting plot limits and projection of plott.

    Origin=[0,0,0]
    fig=plt.figure(figsize=(5,4),facecolor='white')
    ax=plt.axes(projection='3d')
    ax.set_xlim([0,1])
    ax.set_ylim([0,1])
    ax.set_zlim([0,1])
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_zlabel("Eje Z")
    style.use('grayscale')
    plt.title('Rotation about Z axe by'+str(Rotation_grade)+' Degrees')
    ax.view_init(azim=30,elev=35)


    #Description of the Function plotVector with the parameter Vectors position

    # Plotting the vector to describe frame {A}

    def plot_vector (vect_position,color):
      ax.quiver(Origin[0],Origin[1],Origin[2],vect_position[0],vect_position[1],vect_position[2],color=color)

    plot_vector(XA,'b')
    plot_vector(YA,'b')
    plot_vector(ZA,'black')

    # Plotting to describe Frame{B} transformed after the rotation about Z with a vector alpha
    def convert_degtorad(number):
     return (math.pi*number)/180

   # describing the rotation Matrix in terms of the rotation angle.

    rot_matrix_z=np.array([[math.cos(convert_degtorad(Rotation_grade)),-1*math.sin(convert_degtorad(Rotation_grade)),0],[math.sin(convert_degtorad(Rotation_grade)),math.cos(convert_degtorad(Rotation_grade)),0],[0,0,1]])
    print(rot_matrix_z)

    # Evaluating the position Matrix B

    PB=PA@rot_matrix_z

    XB=[PB[0,0],PB[1,0],PB[2,0]]
    YB=[PB[0,1],PB[1,1],PB[2,1]]
    ZB=[PB[2,0],PB[2,1],PB[2,2]]

    # Plotting the new rotated axes
    plot_vector(XB,'r')
    plot_vector(YB,'r')
    plot_vector(ZB,'black')

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0,row=4,pady=35)


# capturar la variable del texto y almacenarla en una variable variation
root.mainloop()

