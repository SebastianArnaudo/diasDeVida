import tkinter as tk
from tkinter import Frame
from tkinter import messagebox
from datetime import datetime
from calculos import diasVividos

def main():

    

    """def diasVividos(dia,mes,anio):
        
        anio=anio
        mes=mes
        dia=dia
            
        def esBisiesto (anio):

            anio=int(anio)
        
            if not anio % 4 and (anio % 100 or  not anio % 400): 
                return True

        def diasDelMes (mes,anio):
                
            mes = int (mes)
                


            if mes == 2:
                    
                if esBisiesto (anio):
                    return 29
                else:
                    return 28

        

        def anio1 (dia,mes,anio):
            
                            
            dia = int(dia)
                    

            ene = 31;  mar = 31; abri = 30; may = 31; jun = 30; 
            jul = 31; ago = 31; sep = 30; octu = 31; nov = 30; dic = 31

            if  diasDelMes(mes,anio) == 29:
                feb = 29
            else:
                feb = 28

                    
            diasVividosA1 = ene + feb + mar + abri + may + jun + jul + ago + sep + octu + nov + dic

            match mes:
                case 1:diasVividosA1 = diasVividosA1 - dia
                case 2: diasVividosA1 = diasVividosA1 - ene - dia
                case 3: diasVividosA1 = diasVividosA1 - ene - feb - dia
                case 4: diasVividosA1 = diasVividosA1 - ene - feb - mar - dia
                case 5: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - dia
                case 6: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - dia
                case 7: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - dia
                case 8: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - dia
                case 9: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - dia
                case 10: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - sep - dia
                case 11: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - sep - octu - dia
                case 12: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - sep - octu - nov - dia

            diasVividosA1= str(diasVividosA1)
            return diasVividosA1

        


        mensaje= "Usted vivio " + anio1(dia,mes,anio) + " dias de su año de nacimiento" 
        return mensaje """

    ventana = tk.Tk()
    ventana.title("Dias de vida")
    ventana.geometry("450x450")

    def anios():

        string=eFechaNacimiento.get()
        listaA1=string.replace("-","/")
        barrasl1=listaA1.count("/")



        
        if barrasl1 == 2:
            listaA1=listaA1.split("/")
            diasVividosA1=diasVividos(int(listaA1[0]),int(listaA1[1]),int(listaA1[2]))
            
            
            try:
                diasVividosA1=diasVividos(int(listaA1[0]),int(listaA1[1]),int(listaA1[2]))
                

            except:
                messagebox.showinfo("Aviso","Formato de fecha de nacimiento incorrecto")
        else:
            messagebox.showinfo("Aviso","Formato de fecha de nacimiento incorrecto")
        
    
        
        lDiasA1["text"]= diasVividosA1

            
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