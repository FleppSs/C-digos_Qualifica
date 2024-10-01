import customtkinter as ctk
from tkinter import *
from PIL import Image, ImageTk


# Configurar modo claro/ escuro
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode

    if dark_mode:
        ctk.set_appearance_mode("dark")
        theme_button.configure(text="Modo Claro")
    else:
        ctk.set_appearance_mode("light")
        theme_button.configure(text="Modo Escuro")

    transparent_windows = [header, menu_frame, search_frame]

    for component in transparent_windows:
        component.configure(fg_color=app.cget("bg"))


# Limpar o frame
def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def load_icons():
    # Carrega os ícones diretamente da pasta "icons" (no mesmo diretório que o arquivo Python)
    icons = {
        "home": ImageTk.PhotoImage(Image.open("icons/home.png").resize((30, 30))),
        "explorar": ImageTk.PhotoImage(Image.open("icons/explorar.png").resize((30, 30))),
        "favoritos": ImageTk.PhotoImage(Image.open("icons/favorito.png").resize((30, 30))),
        "opcoes": ImageTk.PhotoImage(Image.open("icons/opcoes.png").resize((30, 30)))
    }
    return icons


# Lógica da Pesquisa
def search_action(query):
    # Lista de todas as categorias disponíveis
    all_items = explorar_praia()[1] + explorar_bares()[1]

    # Filtrar os itens
    filtered_items = [item for item in all_items if query in item["name"].lower()]
    show_content(filtered_items)


favorite_states = {}  # Armazena os estados de favoritos globalmente
all_items = []


def toggle_favorite(button, item_name):
    # Verifica o estado atual do item
    is_favorite = favorite_states.get(item_name, False)

    # Atualizar o estado no dicionário
    favorite_states[item_name] = not is_favorite

    # Mudar o ícone com base no estado atual
    icon_path = "icons/favorito_active.png" if not is_favorite else "icons/favorito.png"
    img = Image.open(icon_path).resize((20, 20))
    image = ImageTk.PhotoImage(img)

    button.configure(image=image)
    button.image = image
    print(favorite_states)  # Log de verificação


# Toggle hover do icone de Favoritar
def on_enter(button, active_icon):
    # Trocar o ícone para o ativo ao passar o mouse
    img = Image.open(active_icon).resize((25, 25))
    image = ImageTk.PhotoImage(img)
    button.configure(image=image)
    button.image = image


def on_leave(button, item_name):
    # Trocar o ícone de volta com base no estado atual
    icon_path = "icons/favorito_active.png" if favorite_states.get(item_name, False) else "icons/favorito.png"
    img = Image.open(icon_path).resize((20, 20))
    image = ImageTk.PhotoImage(img)
    button.configure(image=image)
    button.image = image


def show_content(items):
    clear_frame(main_frame)

    if not items:
        no_result_label = ctk.CTkLabel(master=main_frame, text="Nenhum resultado encontrado.",
                                       font=("Arial", 16, "bold"))
        no_result_label.pack(pady=20)
        return

    for item in items:
        frame = ctk.CTkFrame(master=main_frame, corner_radius=10)
        frame.pack(pady=10, padx=20, fill="x")

        try:
            print(f"Carregando a imagem: {item['image']}")  # Linha de depuração
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

        # Criação do botão favorito
        favorite_button = ctk.CTkButton(master=frame, text="",
                                        image=ImageTk.PhotoImage(Image.open("icons/favorito.png").resize((20, 20))),
                                        width=40, height=40, fg_color="transparent", hover=False)
        favorite_button.pack(pady=(0, 0), padx=(0, 10), anchor="e")

        # Adicionando a função para o botão favorito
        favorite_button.bind("<Button-1>",
                             lambda event, btn=favorite_button, item_name=item["name"]: toggle_favorite(btn, item_name))
        favorite_button.bind("<Enter>", lambda event, btn=favorite_button: on_enter(btn, "icons/favorito_active.png"))
        favorite_button.bind("<Leave>",
                             lambda event, btn=favorite_button, item_name=item["name"]: on_leave(btn, item_name))

        # Inicializa o estado do favorito
        initial_icon = "icons/favorito_active.png" if favorite_states.get(item["name"], False) else "icons/favorito.png"
        favorite_button.configure(image=ImageTk.PhotoImage(Image.open(initial_icon).resize((20, 20))))

        button_details = ctk.CTkButton(master=frame, text="Ver mais", command=lambda p=item: show_gallery(p),
                                       fg_color="red")
        button_details.pack(pady=(0, 10), padx=(0, 10), anchor="e")


def show_gallery(place):
    clear_frame(main_frame)

    back_button = ctk.CTkButton(master=main_frame, text="Voltar", command=show_explore_menu, fg_color="red")
    back_button.pack(pady=(10, 5), padx=(10, 0), anchor="nw")

    # Carregar a imagem principal
    try:
        img = Image.open(place["image"]).resize((400, 300))
        image = ImageTk.PhotoImage(img)

        main_image_label = ctk.CTkLabel(master=main_frame, image=image, text="")
        main_image_label.image = image  # Manter a referência da imagem
        main_image_label.pack(pady=(15, 10))
    except Exception as e:
        print(f"Erro ao carregar a imagem: {place['image']} - {e}")

    # Nome do lugar
    label_name = ctk.CTkLabel(master=main_frame, text=place["name"], font=("Arial", 18, "bold"))
    label_name.pack(pady=(10, 5))

    # Descrição do lugar
    label_description = ctk.CTkLabel(master=main_frame, text=place["description"], wraplength=400)
    label_description.pack(pady=(5, 10))

    # Galeria de imagens adicionais
    gallery_images = place.get("gallery", [])
    if gallery_images:
        gallery_canvas = Canvas(main_frame, height=150)
        gallery_canvas.pack(pady=10, fill="both", expand=True)

        scrollbar = Scrollbar(main_frame, orient="horizontal", command=gallery_canvas.xview)
        gallery_canvas.configure(xscrollcommand=scrollbar.set)
        scrollbar.pack(side="bottom", fill="x")

        gallery_container = ctk.CTkFrame(gallery_canvas)
        gallery_canvas.create_window((0, 0), window=gallery_container, anchor="nw")

        for image_path in gallery_images:
            try:
                img = Image.open(image_path).resize((120, 90))
                image = ImageTk.PhotoImage(img)
                gallery_label = ctk.CTkButton(master=gallery_container, image=image, text="",
                                              command=lambda img=image_path: update_main_image(main_image_label, img))
                gallery_label.image = image  # Manter a referência da imagem
                gallery_label.pack(side="left", padx=5)
            except Exception as e:
                print(f"Erro ao carregar a imagem da galeria: {image_path} - {e}")

        gallery_container.update_idletasks()
        gallery_canvas.config(scrollregion=gallery_canvas.bbox("all"))


# Atualizar a imagem principal na galeria
def update_main_image(main_image_label, image_path):
    try:
        img = Image.open(image_path)
        img = img.resize((400, 300))
        image = ImageTk.PhotoImage(img)
        main_image_label.configure(image=image)
        main_image_label.image = image
    except Exception as e:
        print(f"Erro ao carregar a imagem: {image_path} - {e}")


# Funções individuais de exploração
def explorar_praia():
    praias = [
        {"name": "Praia 1", "image": "images/praia1.png", "description": "Uma das mais belas praias do Brasil.",
         "gallery": ["images/praia1.png", "images/praia1_1.png"]},
        {"name": "Praia 2", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.",
         "gallery": ["images/praia2.png", "images/praia2_1.png"]},
        {"name": "Praia 3", "image": "images/praia2.png", "description": "Famosa praia no Rio de Janeiro.",
         "gallery": ["images/praia2.png", "images/praia2_1.png"]}
    ]

    global all_items
    all_items.extend(praias)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Praias", praias


def explorar_bares():
    bares = [
        {"name": "Bar 1", "image": "images/bar1.png", "description": "Ambiente agradável com música ao vivo.",
         "gallery": ["images/bar1.png", "images/bar1_1.png"]},
        {"name": "Bar 2", "image": "images/bar2.png", "description": "Excelente local para petiscos e cerveja gelada.",
         "gallery": ["images/bar2.png", "images/bar2_1.png"]},
    ]
    global all_items
    all_items.extend(bares)  # Adiciona a lista global

    # Retorna o nome do botão e os itens
    return "Bares", bares


# Menu 'Inicio'
def show_home():
    clear_frame(main_frame)
    home_label = ctk.CTkLabel(master=main_frame, text="Bem-vindo à Maricá City!", font=("Arial", 18, "bold"))
    home_label.pack(pady=20)


# Menu 'Explorar'
def show_explore_menu():
    clear_frame(main_frame)
    explore_options = [explorar_praia, explorar_bares]

    for option_func in explore_options:
        button_name, content = option_func()
        button = ctk.CTkButton(master=main_frame, text=button_name, command=lambda c=content: show_content(c),
                               fg_color="red")
        button.pack(pady=10, padx=20, side="top", anchor="w")


# Menu 'Favoritos'
def show_favorites_menu():
    clear_frame(main_frame)
    favoritos_label = ctk.CTkLabel(master=main_frame, text="Favoritos", font=("Arial", 18, "bold"))
    favoritos_label.pack(pady=20)

    # Filtrar os itens favoritos de qualquer categoria
    favorite_items = []
    for item_name, is_favorite in favorite_states.items():
        if is_favorite:
            # Aqui você deve buscar de onde o item é, por exemplo, de uma lista de praias ou bares
            # Vou usar exemplos genéricos, substitua pelos seus dados reais
            for category in [explorar_praia(), explorar_bares()]:  # Adicione outras categorias conforme necessário
                for item in category[1]:  # item seria cada item dentro da categoria
                    if item["name"] == item_name:
                        favorite_items.append(item)

    # Chamar a função show_content com os itens favoritos
    show_content(favorite_items)


# Menu 'Opções'
def show_options_menu():
    clear_frame(main_frame)
    global theme_button
    theme_button = ctk.CTkButton(master=main_frame, text="Modo Escuro", command=toggle_theme, fg_color="red")
    theme_button.pack(pady=10, padx=20)


#################### APLICATIVO ####################
app = ctk.CTk()
app.geometry("800x600")
app.title("Marica City")
app.resizable(width=False, height=False)

app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(1, weight=1)

# Nome MARICA CITY
header = ctk.CTkFrame(app, width=260, fg_color=app.cget("bg"))
header.grid(row=0, column=0, sticky="ew", padx=(10, 0), pady=(0, 10))

header_label = ctk.CTkLabel(header, text="MARICA CITY", text_color="red", font=("Arial", 20, "bold"))
header_label.grid(row=0, column=0, pady=10, padx=10)

# Botao de pesquisa
search_frame = ctk.CTkFrame(app, width=300, height=50, fg_color=app.cget("bg"))
search_frame.grid(row=0, column=1, sticky="ew", padx=(10, 0))

search_entry = ctk.CTkEntry(search_frame, width=200)
search_entry.grid(row=0, column=0, padx=(10, 0), pady=10)

search_button = ctk.CTkButton(search_frame, text="Pesquisar", command=lambda: search_action(search_entry.get().lower()),
                              fg_color="red")
search_button.grid(row=0, column=1, padx=(5, 0), pady=10)

# Frame principal
main_frame = ctk.CTkFrame(master=app)
main_frame.grid(row=1, column=1, sticky="nsew", padx=(10, 0))

menu_frame = ctk.CTkFrame(master=app, fg_color=app.cget("bg"))
menu_frame.grid(row=1, column=0, sticky="ns", pady=(0, 10))

# Botoes da esquerda / MENU
icon = load_icons()
menu_buttons = [
    {"text": "   Inicio   ", "command": show_home, "icon": icon["home"]},  # Adiciona espaços extras para alinhar
    {"text": " Explorar", "command": show_explore_menu, "icon": icon["explorar"]},
    {"text": "Favoritos", "command": show_favorites_menu, "icon": icon["favoritos"]},
    {"text": " Opções  ", "command": show_options_menu, "icon": icon["opcoes"]}
]

for index, btn in enumerate(menu_buttons):
    ctk.CTkButton(
        master=menu_frame,
        text=btn["text"],
        command=btn["command"],
        image=btn["icon"],
        compound="left",
        fg_color="red",
        width=150
    ).grid(row=index, column=0, pady=10, padx=10)

# Tema inicial
dark_mode = False
ctk.set_appearance_mode("light")

# Exibe o menu inicial
show_home()
app.mainloop()