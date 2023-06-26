from tkinter import *
from tkinter import ttk, messagebox


class Aplicacion():
    __ventana = None
    __precio_sin_iva = None
    __tipo_iva = None
    __iva = None
    __precio_con_iva = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('300x260')
        self.__ventana.title('Cálculo de IVA')

        # Estilos
        self.__ventana.configure(bg="#00ADEF")
        estilo_titulo = ttk.Style()
        estilo_titulo.configure("titulo.TLabel", foreground="white", background="#00ADEF", font=("Arial", 14, "bold"))
        estilo_boton_calcular = ttk.Style()
        estilo_boton_calcular.configure("boton_calcular.TButton", background="#00CC00", font=("Arial", 10, "bold"))
        estilo_boton_salir = ttk.Style()
        estilo_boton_salir.configure("boton_salir.TButton", background="#FF6699", font=("Arial", 10, "bold"))

        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        ttk.Label(mainframe, text="Cálculo de IVA", style="titulo.TLabel").grid(column=1, row=0, columnspan=3, pady=10)

        self.__precio_sin_iva = StringVar()
        self.__tipo_iva = StringVar()
        self.__iva = StringVar()
        self.__precio_con_iva = StringVar()

        self.precio_sin_iva_entry = ttk.Entry(mainframe, width=10, textvariable=self.__precio_sin_iva)
        self.precio_sin_iva_entry.grid(column=1, row=1, sticky=(W, E), pady=10)

        ttk.Radiobutton(mainframe, text="IVA 21%", variable=self.__tipo_iva, value="21",
                        command=self.calcular_iva).grid(column=1, row=2, sticky=W)
        ttk.Radiobutton(mainframe, text="IVA 10.5%", variable=self.__tipo_iva, value="10.5",
                        command=self.calcular_iva).grid(column=1, row=3, sticky=W)

        ttk.Label(mainframe, text="Precio sin IVA").grid(column=2, row=1, sticky=W)

        ttk.Label(mainframe, text="IVA").grid(column=1, row=4, sticky=E, pady=10)
        ttk.Label(mainframe, textvariable=self.__iva).grid(column=2, row=4, sticky=(W, E), pady=10)

        ttk.Label(mainframe, text="Precio con IVA").grid(column=1, row=5, sticky=E, pady=10)
        ttk.Label(mainframe, textvariable=self.__precio_con_iva).grid(column=2, row=5, sticky=(W, E), pady=10)

        ttk.Button(mainframe, text='Calcular', command=self.calcular_iva, style="boton_calcular.TButton") \
            .grid(column=1, row=6, sticky=W, pady=10)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy, style="boton_salir.TButton") \
            .grid(column=2, row=6, sticky=E, pady=10)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5)

        self.precio_sin_iva_entry.focus()
        self.__ventana.mainloop()

    def calcular_iva(self):
        if self.__precio_sin_iva.get() != '':
            try:
                precio_sin_iva = float(self.__precio_sin_iva.get())
                tipo_iva = float(self.__tipo_iva.get())

                iva = precio_sin_iva * tipo_iva / 100
                precio_con_iva = precio_sin_iva + iva

                self.__iva.set(f"{iva:.2f}")
                self.__precio_con_iva.set(f"{precio_con_iva:.2f}")

            except ValueError:
                messagebox.showerror(title='Error de tipo',
                                     message='Debe ingresar un valor numérico')
                self.__precio_sin_iva.set('')
                self.precio_sin_iva_entry.focus()
        else:
            self.__iva.set('')
            self.__precio_con_iva.set('')

