import customtkinter as ctk 
from Crypto.Random import get_random_bytes
from datetime import datetime
from criptografia import criptografia_simetrica
from criptografia import descriptografia_simetrica


# ----------------------- Função da janela principal --------------------------


def main(janela_login, user_name):
    
    principal = ctk.CTkToplevel()

    janela_login.withdraw()
    principal.title("Seal Criptography")
    principal.geometry("1050x500")
    principal.resizable(False, False)
    principal.update()
    principal.grab_set()

    #grid principal da tela
    principal.grid_columnconfigure(0,weight=1)
    principal.grid_columnconfigure(1,weight=1)
    principal.grid_columnconfigure(2,weight=1)
    principal.grid_columnconfigure(3,weight=1)
    principal.grid_rowconfigure(0,weight=1)
    principal.grid_rowconfigure(1,weight=1)
    principal.grid_rowconfigure(2,weight=1)
    principal.grid_rowconfigure(3,weight=1)


    # Gerando chave simetrica:

    chave_sessao = get_random_bytes(32)



    #função Criptografia

    def criptografar_mensagem():
  
        conteudo_limpo = cripto_text.get("1.0", "end-1c").strip() #Obtem conteudo da caixa de texto e remove espaços em branco
    
    
        if not conteudo_limpo: #Verifica se a variavel conteudo limpo esta com uma string vazia
            resultado_text.configure(state="normal")
            resultado_text.delete("1.0", "end")
            resultado_text.insert("1.0", "Digite uma mensagem para criptografar.")#Retorna a mensagem caso estaja vazia
            resultado_text.configure(state="disabled")
        
        
            cripto_text.configure(state="normal")# Ativa o campo de entrada para nova digitação
            return
    
        cripto_text.delete("1.0", "end-1c")#Limpa o campo de entrada e o desativa
        

    
        mensagem_original = cripto_text.get("1.0", "end-1c") # Recaptura a mensagem
        mensagem_criptografada = criptografia_simetrica(conteudo_limpo,chave_sessao)

  
        resultado_text.configure(state="normal") #Exibe o resultado
        resultado_text.delete("1.0", "end")
        resultado_text.insert("1.0", mensagem_criptografada)
        
    

    #---------------------------  Função Para Chamar  descriptografia --------------------#
    def descriptografar_mensagem():
        
        conteudo_cripto = cripto_text.get("1.0", "end-1c").strip()
        
        if not conteudo_cripto:
            resultado_text.configure(state="normal")
            resultado_text.delete("1.0", "end")
            resultado_text.insert("1.0", "Não há mensagem para descriptografar.")
            resultado_text.configure(state="normal")
            return
            
        try:
            # Passa a chave para a função Descriptografia Simetrica
            mensagem_descriptografada = descriptografia_simetrica(conteudo_cripto, chave_sessao)
            
            resultado_text.configure(state="normal")
            resultado_text.delete("1.0", "end")
            resultado_text.insert("1.0", mensagem_descriptografada)
           

        except ValueError as e:
            resultado_text.configure(state="normal")
            resultado_text.delete("1.0", "end")
            resultado_text.insert("1.0", f"Erro na descriptografia: {e}")
        
    dia_atual = datetime.now()
    data_atual_formatada = dia_atual.strftime("%d-%m-%Y")
    label_saudacao = ctk.CTkLabel(principal,
                                  text=f"Seja bem vindo {user_name}\n Data de Acesso: {data_atual_formatada}",
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
    label_cripto_text = ctk.CTkLabel(textbox_frame, 
                                    text="Mensagem de Entrada:",
                                    font=("Roboto", 16),
                                    text_color="#BDC3C7")
    label_cripto_text.grid(row=0, column=0, sticky="ew", padx=10)
    cripto_text = ctk.CTkTextbox(textbox_frame, 
                                 width=350, 
                                 height=150, 
                                 font=("Roboto", 16), 
                                 border_color="#34495E")
    cripto_text.grid(row=1, column=0, padx=10, pady=5)
    
    #Caixa de texto saida

    label_resultado_text = ctk.CTkLabel(textbox_frame, 
                                        text="Resultado:", 
                                        font=("Roboto", 16), 
                                        text_color="#BDC3C7")
    label_resultado_text.grid(row=0, column=1, sticky="ew", padx=10)
    resultado_text = ctk.CTkTextbox(textbox_frame, 
                                    width=350, 
                                    height=150, 
                                    font=("Roboto", 16), 
                                    border_color="#34495E", 
                                    state="disabled")
    resultado_text.grid(row=1, column=1, padx=10, pady=5)

    #Frame para alinhar os botões
    btn_frame = ctk.CTkFrame(principal, fg_color="transparent")
    btn_frame.grid(row=2, column=1, columnspan=2, pady=10)
    btn_frame.grid_columnconfigure(0, weight=1)
    btn_frame.grid_columnconfigure(1, weight=0)
    btn_frame.grid_columnconfigure(2, weight=1)

    #Botões criptografar e descriptografar

    btn_encrypt = ctk.CTkButton(btn_frame, height=40, text="CRIPTOGRAFAR", fg_color="blue",hover_color="dark blue", command=criptografar_mensagem )
    btn_encrypt.grid(row=0, column=0, padx=(0, 20))

    btn_decrypt = ctk.CTkButton(btn_frame,height=40, text="DESCRIPTOGRAFAR", fg_color="#DC2525", hover_color="#8E1616", command=descriptografar_mensagem)
    btn_decrypt.grid(row=0, column=2, padx=(10, 20))


    def voltar_ao_login(): # Função para retornar o login
        principal.destroy()
        janela_login.deiconify()
        
    btn_voltar = ctk.CTkButton(principal,height=40, text="Voltar",fg_color="red", command=voltar_ao_login)
    btn_voltar.grid(row=3, column=1, columnspan=2, pady=10)
    principal.update()
    #---------------------------------------------------------------------------------------