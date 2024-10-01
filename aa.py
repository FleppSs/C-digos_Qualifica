import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk


# Configurar modo claro/escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        ctk.set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

    components_to_update = [header, menu_frame, search_frame]

    for component in components_to_update:
        component.configure(fg_color=app.cget("bg"))


# Lógica da Pesquisa
def search_action(query):
    results = search_items(query)  # Obter os resultados da pesquisa
    show_content(results)  # Mostrar os resultados no content_frame


# Função para buscar em todas as categorias
def search_items(query):
    # Lista de todas as categorias disponíveis
    all_items = explorar_praia()[1] + explorar_bares()[1]

    # Filtrar os itens que contêm o termo pesquisado no nome
    filtered_items = [item for item in all_items if query in item["name"].lower()]
    return filtered_items


# Limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


# Exibir o conteúdo de uma categoria ou resultado de pesquisa
def show_content(items):
    clear_frame(content_frame)

    if not items:
        no_result_label = ctk.CTkLabel(master=content_frame, text="Nenhum resultado encontrado.", font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = ctk.CTkFrame(master=content_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
            img = Image.open(item["image"])
            img = img.resize((120, 90))
            image = ImageTk.PhotoImage(img)
            label_image = ctk.CTkLabel(master=frame, image=image, text="")
            label_image.image = image
            label_image.pack(side="left", padx=10)
        except Exception as e:
            print(f"Erro ao carregar a imagem: {item['image']} - {e}")

        label_name = ctk.CTkLabel(master=frame, text=item["name"], font=("Arial", 16))
        label_name.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        label_description = ctk.CTkLabel(master=frame, text=item["description"], wraplength=400)
        label_description.pack(anchor="w", pady=(10, 0), padx=(10, 0))

        button_details = ctk.CTkButton(master=frame, text="Ver mais", fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")


# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia do Francês", "image": "images/praia1.png",
         "description": "Uma das mais belas praias do Brasil."},
        {"name": "Praia de Copacabana", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro."},
    ]
    return "Praias", praias


def explorar_bares():
    bares = [
        {"name": "Bar do Zé", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo."},
        {"name": "Botequim do João", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada."},
    ]
    return "Bares", bares


# Menu 'Inicio'
def show_home():
    clear_frame(content_frame)
    home_label = ctk.CTkLabel(master=content_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)


# Menu 'Explorar'
def show_explore_menu():
    clear_frame(content_frame)
    explore_options = [explorar_praia, explorar_bares]

    for option_func in explore_options:
        button_name, content = option_func()
        button = ctk.CTkButton(master=content_frame, text=button_name, command=lambda c=content: show_content(c), fg_color="red")
        button.pack(pady=10, padx=20, side="top", anchor="w")


# Menu 'Opções'
def show_options_menu():
    clear_frame(content_frame)
    global theme_button
    theme_button = ctk.CTkButton(master=content_frame, text="Modo Claro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)


#################### APLICATIVO ####################
app = ctk.CTk()
app.geometry("800x600")
app.title("Marica City")
app.resizable(width=False, height=False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

header = ctk.CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = ctk.CTkLabel(header, text="MARICA CITY", text_color="red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10)

search_frame = ctk.CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = ctk.CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = ctk.CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()), fg_color="red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

# Adicionando o Canvas para o conteúdo principal com Scrollbar
content_canvas = Canvas(app)
content_canvas.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

scrollbar = Scrollbar(app, orient="vertical", command=content_canvas.yview)
scrollbar.grid(row=1, column=2, sticky="ns")

content_canvas.configure(yscrollcommand=scrollbar.set)
content_canvas.bind('<Configure>', lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all")))

content_frame = ctk.CTkFrame(content_canvas)
content_canvas.create_window((0, 0), window=content_frame, anchor="nw")

menu_frame = ctk.CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

menu_buttons = [
    {"text": "Inicio", "command": show_home},
    {"text": "Explorar", "command": show_explore_menu},
    {"text": "Opções", "command": show_options_menu},
]

for index, btn in enumerate(menu_buttons):
    ctk.CTkButton(master=menu_frame, text=btn["text"], command=btn["command"], fg_color="red").grid(row=index, column=0, pady=10, padx=10)

dark_mode = False

show_home()
app.mainloop()
