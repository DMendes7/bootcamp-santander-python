# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:

def prioridade(paciente):
    nome, idade, status = paciente
    # Urgente: prioridade máxima (0)
    # Idoso: prioridade média (1)
    # Demais: prioridade baixa (2)
    if status == "urgente":
        return (0, -idade)  # urgente, mais velhos primeiro
    elif idade >= 60:
        return (1, -idade)  # idosos, mais velhos primeiro
    else:
        return (2, 0)  # demais
    
pacientes_ordenados = sorted(pacientes, key=prioridade)
nomes = [p[0] for p in pacientes_ordenados]
print("Ordem de Atendimento: " + ", ".join(nomes))