import sys
import os 
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(project_root)
import customtkinter as ctk
from graphics.principal import main
from criptografia import criptografia_simetrica
from criptografia import descriptografia_simetrica

def app():


    ctk.set_appearance_mode("Dark")

    app = ctk.CTk()
    app.title("Seal Criptography")
    app.geometry("500x200")
    app.resizable(False, False)
    
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=0)
    app.grid_columnconfigure(2, weight=1)
    
    
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)
    app.grid_rowconfigure(2, weight=1)
    app.grid_rowconfigure(3, weight=1)

    


    #Label sistema
    label_sys = ctk.CTkLabel(app,text="SEAL --- Cryptography", font=("Roboto", 20))
    label_sys.grid(row=0, column=1,)

    # Login
    label_login = ctk.CTkLabel(app,text="IDENTIFICAÇÃO: ", font=("Roboto", 17 ))
    label_login.grid(row=1, column=0, sticky="ew")
    login_box  = ctk.CTkEntry(app, height=30, width=200, font=("arial bold", 15))
    login_box.grid(row=1, column=1,sticky="w")
    
    #Valida login
    def valida_login():
        user_name = login_box.get()
        if user_name.strip() == "": #Verifica se o campo login box está vazio ou śó com espaços em branco
            mensagem_erro.configure(text="Campo identificação é obrigatorio.", text_color="red")
        else:
            mensagem_erro.configure(text="")
            main(app,user_name)

    #Botão
    btn_login = ctk.CTkButton(app,height=40, text="Autenticar",font=("Roboto", 14, "bold"), width=100, fg_color="#1230AE",hover_color="#091057",command=valida_login)
    btn_login.grid(row=2, column=1,)

    #Mensagem de erro
    mensagem_erro = ctk.CTkLabel(app, text="", font=("Roboto", 16),text_color="red")
    mensagem_erro.grid(row=4, column=1, pady=(0, 10))

    



    return app 


inicializacao = app()
inicializacao.mainloop()






