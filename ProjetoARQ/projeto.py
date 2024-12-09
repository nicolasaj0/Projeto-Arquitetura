import customtkinter as ctk
from tkinter import messagebox
from processadores import obter_recomendacao

# Inserção dos critérios
def recomendar():
    uso = uso_var.get()
    desempenho = desempenho_var.get()
    custo = custo_var.get()
    energia = energia_var.get()

    if not uso or not desempenho or not custo or not energia:
        messagebox.showerror("Erro", "Por favor, preencha todos os critérios.") 
        return

    recomendacao = obter_recomendacao(uso, desempenho, custo, energia)

    # Janela com a CPU recomendada
    nova_janela = ctk.CTkToplevel(root)
    nova_janela.title("Resultado da Recomendação")
    nova_janela.geometry("500x400")

    # Título
    ctk.CTkLabel(nova_janela, text="Recomendação de CPU", font=("Arial", 20, "bold")).pack(pady=10)

    # Container do resultado
    container = ctk.CTkFrame(nova_janela)
    container.pack(pady=20, padx=20, fill="both", expand=True)

    # Exibição dos resultados no container
    resultado_texto = (
        f"Modelo: {recomendacao['modelo']}\n"
        f"Arquitetura: {recomendacao['arquitetura']}\n"
        f"Cache: {recomendacao['cache']}\n"
        f"Frequência: {recomendacao['frequencia']}\n\n"
        f"Justificativa:\n{recomendacao['justificativa']}"
    )
    ctk.CTkLabel(container, text=resultado_texto, font=("Arial", 14), justify="left", wraplength=450).pack(pady=10)

    # Botão de fechar a janela
    ctk.CTkButton(nova_janela, text="Fechar", command=nova_janela.destroy).pack(pady=10)

# Janela principal
root = ctk.CTk()
root.title("Recomendador de CPUs")
root.geometry("600x500")

# Título
ctk.CTkLabel(root, text="Critérios de Seleção de CPU", font=("Arial", 24, "bold")).pack(pady=20)

# Os tipos de uso
ctk.CTkLabel(root, text="Tipo de Uso:", font=("Arial", 16)).pack(anchor="w", padx=20)
uso_var = ctk.StringVar()
ctk.CTkOptionMenu(root, variable=uso_var, values=["Jogos", "Edição de Vídeo", "IA", "IoT"]).pack(fill="x", padx=20, pady=5)

# Critérios de desempenho
ctk.CTkLabel(root, text="Desempenho Esperado:", font=("Arial", 16)).pack(anchor="w", padx=20)
desempenho_var = ctk.StringVar()
ctk.CTkOptionMenu(root, variable=desempenho_var, values=["Baixo", "Médio", "Alto"]).pack(fill="x", padx=20, pady=5)

# Orçamento
ctk.CTkLabel(root, text="Custo:", font=("Arial", 16)).pack(anchor="w", padx=20)
custo_var = ctk.StringVar()
ctk.CTkOptionMenu(root, variable=custo_var, values=["Econômico", "Intermediário", "Alto"]).pack(fill="x", padx=20, pady=5)

# Consumo de energia
ctk.CTkLabel(root, text="Consumo de Energia:", font=("Arial", 16)).pack(anchor="w", padx=20)
energia_var = ctk.StringVar()
ctk.CTkOptionMenu(root, variable=energia_var, values=["Baixo", "Médio", "Alto"]).pack(fill="x", padx=20, pady=5)

# Botão para recomendar
ctk.CTkButton(root, text="Recomendar", command=recomendar, fg_color="blue").pack(pady=20)

root.mainloop()
