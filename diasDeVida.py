import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
from datetime import datetime
from calculos import diasVividos

def main():

    

    

    ventana = tk.Tk()
    ventana.title("Dias de vida")
    ventana.geometry("450x450")

    def anios():

        string=eFechaNacimiento.get()
        listaA1=string.replace("-","/")
        barrasl1=listaA1.count("/")


        d = datetime.now()
        year = d.year
        
        if barrasl1 == 2:
            listaA1=listaA1.split("/")
            
            try:
                if (int(listaA1[0]) > 29 and int(listaA1[1]) == 2) or (int(listaA1[0])) > 31 or (int (listaA1[1])) > 12 or (int (listaA1[2])) > year:
                    messagebox.showerror("Aviso","Fecha invalida")
                else:
                    diasVividosA1=diasVividos(int(listaA1[0]),int(listaA1[1]),int(listaA1[2]))
                    lDiasA1["text"]= diasVividosA1
            except:
                messagebox.showinfo("Aviso","Formato de fecha de nacimiento incorrecto")
        else:
            messagebox.showinfo("Aviso","Formato de fecha de nacimiento incorrecto")
        
    
        
        

            
    lFechaNacimiento= tk.Label(text="Ingrese su fecha de nacimiento\n En formato DD/MM/AAAA")
    lFechaNacimiento.place(x=140, y=10)

    eFechaNacimiento= tk.Entry()
    eFechaNacimiento.place(x=160, y=50)

    bCalculo= tk.Button(text= "Calcular", command=anios)
    bCalculo.place(x=185,y=100)

    lDiasA1= tk.Label(text="")
    lDiasA1.place(x=80,y=150)

    tk.mainloop()

if __name__ == "__main__":
    main()