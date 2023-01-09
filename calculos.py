from datetime import datetime


    
def diasVividos(dia,mes,anio):

    d = datetime.now()
    diaA= d.day
    mesA= d.month
    anioA= d.year

    diaN= dia
    mesN= mes
    anioN= anio

    def esBisiesto(anioA):
        anioA= int(anioA)

        if not anioA % 4 and (anioA % 100 or not anioA % 400):
            return True

    def diasDelMes(mesA,anioA):
        mesA= int(mesA)

        if mesA == 2:
            if esBisiesto(anioA):
                return 29
            else:
                return 28

    def esBisiestoN(anioN):
        anioN= int(anioN)

        if not anioN % 4 and (anioN % 100 or not anioN % 400):
            return True

    def diasDelMesN(mesN,anioN):
        mesN= int(mesN)

        if mesN == 2:
            if esBisiestoN(anioN):
                return 29
            else:
                return 28


    

    def calcularDJ(diaA,mesA,anioA):
           
        dia= diaA
        mes= mesA
        anio= anioA

        


            
        def calcularDiaJuliano(dia,mes,anio):

            diaJuliano = 0

            dia= int(dia)

                
            ene = 31;  mar = 31; abri = 30; may = 31; jun = 30; 
            jul = 31; ago = 31; sep = 30; octu = 31; nov = 30;

            if  diasDelMes(mes,anio) == 29:
                feb = 29
            else:
                feb = 28

            match mes: 
                case 1: diaJuliano += dia
                case 2: diaJuliano += ene + dia
                case 3: diaJuliano += ene + feb + dia
                case 4: diaJuliano += ene + feb + mar + dia
                case 5: diaJuliano += ene + feb + mar + abri + dia
                case 6: diaJuliano += ene + feb + mar + abri + may + dia
                case 7: diaJuliano += ene + feb + mar + abri + may + jun + dia
                case 8: diaJuliano += ene + feb + mar + abri + may + jun + jul + dia
                case 9: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + dia
                case 10: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + dia
                case 11: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + octu + dia
                case 12: diaJuliano += ene + feb + mar + abri + may + jun + jul + ago + sep + octu + nov + dia

            diaJuliano = int(diaJuliano)
            

            return diaJuliano

       
        
        mensaje = calcularDiaJuliano(dia,mes,anio)

        return mensaje
    
    
       


    def calcularDiasNacimiento(diaN,mesN,anioN):
        
        def anio1(diaN,mesN,anioN):
           
            diaN = (diaN)

            ene= 31; mar=31; abri=30; may=31; jun=30;
            jul=31; ago=31; sep=30; octu=31; nov=30; dic=31

            if diasDelMesN(mesN,anioN)==29:
                feb=29
            else:
                feb=28
            
            diasVividosA1= ene + feb + mar + abri + may + jun + jul + ago + sep + octu + nov + dic

            match mesN:
                case 1: diasVividosA1 = diasVividosA1 - diaN
                case 2: diasVividosA1 = diasVividosA1 - ene - diaN
                case 3: diasVividosA1 = diasVividosA1 - ene - feb - diaN
                case 4: diasVividosA1 = diasVividosA1 - ene - feb - mar - diaN
                case 5: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - diaN
                case 6: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - diaN
                case 7: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - diaN
                case 9: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - diaN
                case 10: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - diaN
                case 11: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - sep - diaN
                case 12: diasVividosA1 = diasVividosA1 - ene - feb - mar - abri - may - jun - jul - ago - sep - octu - nov - diaN

            diasVividosA1 = int(diasVividosA1)
            
            mensaje = diasVividosA1
            return mensaje
        
        return anio1(diaN, mesN, anioN)

    

    def edad(diaA,mesA,anioA, diaN, mesN,anioN):

        diaN=int(diaN); diaA=int(diaA)
        mesN=int(mesN); mesA=int(mesA)
        anioN=int(anioN); anioA=int(anioA)

        edad= 0
    
        if mesN == mesA and diaN > diaA:
            edad = anioA - anioN - 1
        elif mesN > mesA:
            edad = anioA - anioN - 1
        else:
            edad = anioA - anioN
        
        edad= int(edad)

        return edad
    
    def aniosBisiestos(anioN,anioA):
        anio=anioN
        aniosBiciestos=0

        anio=int(anio)
        anioA=int(anioA)

        while anio != anioA:
            anio += 1
            if not anio % 4 and (anio % 100 or  not anio % 400): 
                aniosBiciestos += 1
                anio += 1
        
        aniosBiciestos= int(aniosBiciestos)
        return aniosBiciestos

        
    

    diasVida=(edad(diaA,mesA,anioA,diaN,mesN,anioN) * 365) - calcularDiasNacimiento(diaN,mesN,anioN) - calcularDJ(diaA,mesA,anioA) + aniosBisiestos(anioN,anioA)
    diasVida=str(diasVida)

    aniosVividos=edad(diaA,mesA,anioA,diaN,mesN,anioN)
    aniosVividos=str(aniosVividos)

    diasVidaA1=calcularDiasNacimiento(diaN,mesN,anioN)
    diasVidaA1=str(diasVidaA1)

    diasVidaAA=calcularDJ(diaA,mesA,anioA)
    diasVidaAA=str(diasVidaAA)

    diasBisiestos=aniosBisiestos(anioN,anioA)
    diasBisiestos=str(diasBisiestos)

    mensaje = "Usted tiene " + aniosVividos + " años.\nHabiendo vivido " + diasVidaA1 + " dias el año de su nacimiento.\n Y " + diasVidaAA + " dias del año actual.\n Habiendo atravezado "+ diasBisiestos +" años bisiestos.\n Usted vivio " + diasVida + " dias"

    return mensaje

    
   
    