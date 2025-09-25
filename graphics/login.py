from PIL import Image 
import customtkinter as ctk



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

    # ----------------------- Função da janela principal --------------------------
    def main(janela_login):
        janela_login.withdraw()

        principal = ctk.CTkToplevel(janela_login)
        principal.title("Seal Criptography")
        principal.geometry("500x200")
        principal.resizable(False, False)
        principal.update()
        principal.grab_set()

        def voltar_ao_login(): # Função para retornar o login
            principal.destroy()
            janela_login.deiconify()
        btn_voltar = ctk.CTkButton(principal, text="Voltar", command=voltar_ao_login)
        btn_voltar.pack(pady=20)
    #---------------------------------------------------------------------------------------

    #Label sistema
    label_sys = ctk.CTkLabel(app,text="SEAL --- Cryptography", font=("Roboto", 20))
    label_sys.grid(row=0, column=1,)

    # Login
    label_login = ctk.CTkLabel(app,text="LOGIN: ", font=("Roboto", 17 ))
    label_login.grid(row=1, column=0, sticky="ew")
    login_box  = ctk.CTkEntry(app, height=30, width=200, font=("arial bold", 12))
    login_box.grid(row=1, column=1,sticky="w")
    
    #Senha
    label_senha = ctk.CTkLabel(app, text="SENHA: ", font=("Roboto", 17 ))
    label_senha.grid(row=2, column=0,stick="ew")
    password  = ctk.CTkEntry(app, show="*", height=30, width=200, font=("arial bold", 12))
    password.grid(row=2, column=1, sticky="w")

    #Botão
    btn_login = ctk.CTkButton(app, text="Autenticar", height=30, width=100, fg_color="#6E8CFB",command=lambda:main(app))
    btn_login.grid(row=3, column=1,)




    return app 





