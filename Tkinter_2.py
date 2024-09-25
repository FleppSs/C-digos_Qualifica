import customtkinter
def buttom_callback():
    print("Apertou")
app = customtkinter.CTk()
app.title("Meu aplicativo")
app.geometry("500x350")
buttom = customtkinter.CTkButton(app, text="aperte", command=buttom_callback)
buttom.grid(row=0, column=0, padx=20, pady=20)
app.grid_columnconfigure(0, weight=1)
buttom.grid(row=0, column=0, padx=20, pady=2, sticky="ew")
checkbox_1 = customtkinter.CTkCheckBox(app, text="Marcação 1", text_color="red")
checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_2 = customtkinter.CTkCheckBox(app, text="Marcação 2", text_color="green")
checkbox_2.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="w")
checkbox_3 = customtkinter.CTkCheckBox(app, text="Marcação 3", text_color="Blue")
checkbox_3.grid(row=3, column=0, padx=20, pady=(0, 20), sticky="w")

app.mainloop()