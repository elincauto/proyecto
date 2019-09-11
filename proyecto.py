from tkinter import *
from tkinter import ttk
import configparser
import requests
import json

DEFAULTPADDING=4

class Conversor(ttk.Frame):
    def __init__(self,parent):
        ttk.Frame.__init__(self,parent,height='150',width='1536')

        config=configparser.ConfigParser()
        config.read("config.ini")
        self.API_KEY=config['COINMARKETCAP']['API_KEY']
        self.ALL_SYMBOLS_EP=config['COINMARKETCAP']['ALL_SYMBOLS_EP']

        #Variables de control
        self.strInQuantity=StringVar(value="")
        self.oldInQuantity=self.strInQuantity.get()
        self.strInQuantity.trace('w',self.validarCantidad)#falta definir validar cantidad
        self.strIncurrency=StringVar()
        self.strInQuantity=StringVar()

        #Parte de la izquierda del Frame

        self.strInCurrency=StringVar()
        self.strOutCurrency=StringVar()

        frIncurrency=ttk.Frame(self)
        frIncurrency.pack_propagate(0)
        frIncurrency.pack(side=LEFT,fill=BOTH,expand=True)

        self.inCurrencyCombo=ttk.Combobox(frIncurrency, width=25, height=5, textvariable=self.strInCurrency)
        self.inCurrencyCombo.pack(side=TOP,fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)
        self.inCurrencyCombo.bind('<<ComboboxSelected',self.convertirDivisas) #falta definir convertir divisas

        lblQ=ttk.Label(frIncurrency,text='Cantidad')
        lblQ.pack(side=TOP, fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)

        self.inQuantityentry=ttk.Entry(frIncurrency,font=('Times',22,'bold'),width=10,textvariable=self.strInQuantity)
        self.inQuantityentry.pack(side=TOP,fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)


        #Parte de la derecha del Frame

        frOutCurrency=ttk.Frame(self)
        frOutCurrency.pack_propagate(0)
        frOutCurrency.pack(side=LEFT,fill=BOTH,expand=TRUE)

        self.outCurrencyCombo=ttk.Combobox(frOutCurrency,width=25,height=5,textvariable=self.strOutCurrency)
        self.outCurrencyCombo.pack(side=TOP, fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)
        self.outCurrencyCombo.bind('<<ComboboxSelected>>',self.convertirDivisas)

        lblQ=ttk.Label(frOutCurrency,text='Cantidad')
        lblQ.pack(side=TOP,fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)

        self.outQuantityLbl=ttk.Label(frOutCurrency,font=('Times',22,'bold'),anchor=E, width=10)
        self.outQuantityLbl.pack(side=TOP,fill=X,padx=DEFAULTPADDING,pady=DEFAULTPADDING)

        frBotones=ttk.frame(self)

        #esto nos queda pendiente hacer los botones de aceptar y rechazar

    def validarCantidad(self,*args):
        try:
            v=float(self.strInQuantity.get())
            self.oldInQuantity=v
            self.convertirDivisas()

        except:
            self.strInQuantity.set(self.oldInQuantity)

    def accesoAPI(self,url,callback,**args):
        try:
            response=requests.get(url)
        except requests.exceptions.ConnectionError as e:
            print(e)
        raise APIAccesError('Error de conexión al servidor.Mire consola')

        if response.status_code==200:
            callback(response.text,**args)
        else:
            msgError='{}-{}'.format(response.status_code,url)
        raise APIAccesError(msgError)

    def convertirDivisas(self,*args):
        _from=self.strInCurrency.get()
        _to=self.strOutCurrency.get()

        if self.strInCurrency.get() and self.strOutCurrency and self.strInQuantity.get():
            self.lblErrorMessages.config(text='Conectando...')

        url=self.rate_ep.format(self.API_KEY,_from,_to)

        try:
            self.accesoAPI(url,self.showConversionRate,From=_from,To=_to)

        except:
            self.lblErrorMessages.config(text=e.cause)

    def showConversionRate(self,textdata,**args):
        data=json.loads(textdata)
        if data['succes']:
            tasa_conversion=data['price']

        self.lblErrorMessages.config(text='')

        else:
            msgError="{}-{}".format(status['error_code'],data['error_message']
        
            prnt(msgError)

            raise APIAccesError(msgError)

        valor_label=round(float(self.strInQuantity.get()/tasa_conversion*tasa_conversion2,5)
        self.outQuantityLbl.config(text=valor_label)

    






        









        



        

    












        






        
class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Crypto inversions")
        self.geometry("864x1536") #ancho x alto
        self.Conversor=Conversor(self)#quiero que ocupe toda mi pantalla y no lo estoy consiguiendo.
        self.Conversor.place(x=0,y=0)

    def start(self):
        self.mainloop()

if __name__=='__main__':
    app=MainApp()
    app.start()