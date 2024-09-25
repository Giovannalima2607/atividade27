# Inicializa uma lista para armazenar os nomes dos convidados
convidados = []

# Loop para receber os nomes dos 7 convidados
for i in range(1, 8):
    nome = input(f"Digite o nome do convidado {i}: ")
    convidados.append(nome)

# Pergunta ao usuário se deseja remover algum convidado
remover = input("Deseja remover algum convidado da lista? (sim/não): ").strip().lower()

if remover == 'sim':
    nome_remover = input("Digite o nome do convidado a ser removido: ")
    if nome_remover in convidados:
        convidados.remove(nome_remover)
        print(f"{nome_remover} foi removido da lista.")
    else:
        print(f"{nome_remover} não está na lista de convidados.")

# Exibe a lista final de convidados
print("Lista final de convidados:")
for convidado in convidados:
    print(convidado)