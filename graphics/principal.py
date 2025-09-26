import customtkinter as ctk    
# ----------------------- Função da janela principal --------------------------
def main(janela_login, user_name):
    
    principal = ctk.CTkToplevel()

    janela_login.withdraw()
    principal.title("Seal Criptography")
    principal.geometry("1050x500")
    principal.resizable(False, False)
    principal.update()
    principal.grab_set()

    
    principal.grid_columnconfigure(0,weight=1)
    principal.grid_columnconfigure(1,weight=1)
    principal.grid_columnconfigure(2,weight=1)
    principal.grid_columnconfigure(3,weight=1)

    principal.grid_rowconfigure(0,weight=1)
    principal.grid_rowconfigure(1,weight=1)
    principal.grid_rowconfigure(2,weight=1)
    principal.grid_rowconfigure(3,weight=1)
    

    label_saudacao = ctk.CTkLabel(principal,
                                  text=f"Seja bem vindo {user_name}",
                                    font=("Roboto", 20))
    label_saudacao.grid(row=0, column=1,columnspan=2, pady=(10, 5))

    label_area_texto = ctk.CTkLabel(principal, text="Área de Texto", font=("Roboto", 16, "bold"))
    label_area_texto.grid(row=1, column=1, columnspan=2, pady=(10, 5))
    
    # - Frame para os Textboxes -
    textbox_frame = ctk.CTkFrame(principal, fg_color="transparent")
    textbox_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    textbox_frame.grid_columnconfigure(0, weight=1)
    textbox_frame.grid_columnconfigure(1, weight=1)
    
    # - Caixas de texto
    label_cripto_text = ctk.CTkLabel(textbox_frame, text="Mensagem de Entrada:", font=("Roboto", 16), text_color="#BDC3C7")
    label_cripto_text.grid(row=0, column=0, sticky="ew", padx=10)
    cripto_text = ctk.CTkTextbox(textbox_frame, width=350, height=150, font=("Roboto", 16), border_color="#34495E")
    cripto_text.grid(row=1, column=0, padx=10, pady=5)
    
    #Caixa de texto saida

    label_resultado_text = ctk.CTkLabel(textbox_frame, text="Resultado:", font=("Roboto", 16), text_color="#BDC3C7")
    label_resultado_text.grid(row=0, column=1, sticky="ew", padx=10)
    resultado_text = ctk.CTkTextbox(textbox_frame, width=350, height=150, font=("Roboto", 16), border_color="#34495E", state="disabled")
    resultado_text.grid(row=1, column=1, padx=10, pady=5)

    btn_frame = ctk.CTkFrame(principal, fg_color="transparent")
    btn_frame.grid(row=2, column=1, columnspan=2, pady=10)
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=0)
    btn_frame.grid_columnconfigure(2, weight=1)

    #Botões criptografar e descriptografar

    btn_encrypt = ctk.CTkButton(btn_frame, height=40, text="CRIPTOGRAFAR", fg_color="blue",hover_color="dark blue" )
    btn_encrypt.grid(row=0, column=0, padx=(0, 20))

    btn_decrypt = ctk.CTkButton(btn_frame,height=40, text="DESCRIPTOGRAFAR", fg_color="#DC2525", hover_color="#8E1616")
    btn_decrypt.grid(row=0, column=2, padx=(10, 20))


    def voltar_ao_login(): # Função para retornar o login
        principal.destroy()
        janela_login.deiconify()
        
    btn_voltar = ctk.CTkButton(principal,height=40, text="Voltar",fg_color="red", command=voltar_ao_login)
    btn_voltar.grid(row=3, column=1, columnspan=2, pady=10)
    principal.update()
    #---------------------------------------------------------------------------------------