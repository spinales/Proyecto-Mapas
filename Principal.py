import tkinter as tk
from tkinter import ttk
import requests
import json


def ConsumingAPI():
    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = """
    [out:json];
    area["ISO3166-1"="DO"][admin_level=2];
    (
    way["highway"](area);
    );
    out center;
    """
    response = requests.get(overpass_url, 
    params={'data': overpass_query})
    data = response.json()
    with open('data.json','w') as file:
        json.dump(data, file, indent=4)



def Descargar():
    win=tk.Toplevel()
    win.geometry('100x100')
    win.resizable(width=False,height=False)
    win.configure(background='white')
    boton2 = tk.Button(win,text="Download",bg="dodger blue",fg="white")
    boton2.pack(padx=10,pady=20)



def Principal(): 
    ventana = tk.Tk()
    ventana.title("OSM Converter")
    ventana.geometry('200x150')
    ventana.resizable(width=False,height=False)
    ventana.iconbitmap('icono.ico')
    ventana.configure(background='white')
    etiqueta = tk.Label(ventana,text="Choose a country",bg='white')
    etiqueta.pack(padx=20,pady=5)
    combo = ttk.Combobox(ventana, state="readonly")
    combo["values"]=["Republica Dominicana"]
    combo.pack(padx=20,pady=5)
    boton = tk.Button(ventana,text="Send",bg="dodger blue",fg="white",width="20",command=ConsumingAPI)
    boton.pack(padx=20,pady=10)
    ventana.mainloop()

   
    
Principal()
