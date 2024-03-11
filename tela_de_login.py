# Importa os módulos necessários
from customtkinter import *
from PIL import Image

# Cria a janela principal da aplicação
app = CTk()
app.geometry("600x480")  # Define o tamanho da janela
app.resizable(0, 0)      # Torna a janela não redimensionável

# Carrega as imagens
side_img_data = Image.open("side-img.webp")
email_icon_data = Image.open("email-icon.webp")
password_icon_data = Image.open("password-icon.webp")
google_icon_data = Image.open("google-icon.webp")

# Cria instâncias CTkImage para cada imagem
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17, 17))

# Exibe a imagem de fundo lateral
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

# Cria um frame para os elementos do formulário
frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)  
frame.pack(expand=True, side="right")

# Cria rótulos e campos de entrada para os elementos do formulário
CTkLabel(master=frame, text="Bem vindo!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Faça login em sua conta", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000").pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Senha:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))

# Cria botão de login
CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Cria botão de login com Google
CTkButton(master=frame, text="Continuar com o Google", fg_color="#EEEEEE", hover_color="#EEEEEE", font=("Arial Bold", 9), text_color="#601E88", width=225, image=google_icon).pack(anchor="w", pady=(20, 0), padx=(25, 0))

# Inicia o loop de eventos principal da aplicação
app.mainloop()