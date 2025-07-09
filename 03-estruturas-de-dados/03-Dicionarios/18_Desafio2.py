# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())
3
# TODO: Crie um loop para armazenar participantes e seus temas:
for i in range(n):
    # Entrada do nome do participante e do tema
    entrada = input().strip().split()
    participante = entrada[0]
    tema = entrada[1]
    
    # Verifica se o tema já existe no dicionário
    if tema not in eventos:
        eventos[tema] = []
    
    # Adiciona o participante ao tema correspondente
    participante = participante.rstrip(',')  # Remove vírgula do nome
    eventos[tema].append(participante)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")