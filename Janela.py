import tkinter as tk
from tkinter import ttk

def mostrar_valor(event=None):
    try:
        texto_entrada = caixa_entrada.get().replace(',', '.')
        valor = float(texto_entrada) 
        fator = float(caixa_fator.get().replace(',', '.'))
        resultado = operacao(valor, fator)  
        resultado_formatado = f"{resultado:.4f}"
        rotulo_resultado.config(text=f"Resultado: {resultado_formatado}")
    except ValueError:
        rotulo_resultado.config(text="Erro: Entrada inválida")

def operacao(valor, fator):
    return valor * fator

def atualizar_fator(event=None):
    try:
        fator = float(caixa_fator.get().replace(',', '.'))
        rotulo_status.config(text=f"Fator de multiplicação atualizado: {fator}")
    except ValueError:
        rotulo_status.config(text="Erro: Fator inválido")

janela = tk.Tk()
janela.title("Calculadora de ICMS")
janela.geometry("400x300")

style = ttk.Style()
style.configure("TButton", foreground="white", background="blue", padding=10, font=("Arial", 10, "bold"))
style.configure("TLabel", background="lightblue", font=("Arial", 12))
style.configure("TEntry", padding=5, relief="flat")

notebook = ttk.Notebook(janela)
notebook.pack(expand=True, fill='both')

aba_principal = ttk.Frame(notebook)
notebook.add(aba_principal, text='Principal')

rotulo = tk.Label(aba_principal, text="Digite o valor")
rotulo.pack(pady=10)

caixa_entrada = tk.Entry(aba_principal)
caixa_entrada.pack(pady=10)
caixa_entrada.bind('<Return>', mostrar_valor)  # Associa o Enter à função mostrar_valor

botao = tk.Button(aba_principal, text="Mostrar Valor", command=mostrar_valor)
botao.pack(pady=10)

rotulo_resultado = tk.Label(aba_principal, text="")
rotulo_resultado.pack(pady=10)

aba_configuracoes = ttk.Frame(notebook)
notebook.add(aba_configuracoes, text='Configurações')

rotulo_fator = tk.Label(aba_configuracoes, text="ICMS")
rotulo_fator.pack(pady=10)

caixa_fator = tk.Entry(aba_configuracoes)
caixa_fator.pack(pady=10)
caixa_fator.insert(0, "0.02")

botao_atualizar = tk.Button(aba_configuracoes, text="Atualizar Fator", command=atualizar_fator)
botao_atualizar.pack(pady=10)

rotulo_status = tk.Label(aba_configuracoes, text="")
rotulo_status.pack(pady=10)

# Associa o Enter também à atualização do fator, se desejar
caixa_fator.bind('<Return>', atualizar_fator)

if __name__ == "__main__":
    janela.mainloop()
