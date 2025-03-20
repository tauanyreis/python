import random

def distribuir_tarefas(exercicios, participantes_exercicios, participantes_apresentacao):
    random.shuffle(participantes_exercicios)
    random.shuffle(participantes_apresentacao)
    
    apresentadora = random.choice(participantes_apresentacao)
    apresentadoras = ["Ingrid", apresentadora]
    outra_participante = next(p for p in participantes_apresentacao if p != apresentadora)
    participantes_exercicios.append(outra_participante)
    
    random.shuffle(participantes_exercicios)
    atribuicao_exercicios = {p: [] for p in participantes_exercicios}
    
    for i, exercicio in enumerate(exercicios):
        participante = participantes_exercicios[i % len(participantes_exercicios)]
        atribuicao_exercicios[participante].append(exercicio)
    
    # Garantir que todas tenham pelo menos um exercício
    for participante in participantes_exercicios:
        if not atribuicao_exercicios[participante]:
            atribuicao_exercicios[participante].append(random.choice(exercicios))
    
    return atribuicao_exercicios, apresentadoras

exercicios = [
    "1. Análise de distribuição de idade, tempo de assinatura, frequência de uso e região",
    "2. Gráficos para padrões de clientes que mantêm e cancelam",
    "3. Testes estatísticos sobre tempo de assinatura e taxa de cancelamento",
    "4. Cálculo do tamanho da amostra para diferentes margens de erro"
]

participantes_exercicios = ["Naielly", "Letícia", "Talita", "Geovana"]
participantes_apresentacao = ["Tauany", "Odaleia"]

atribuicao, apresentadoras = distribuir_tarefas(exercicios, participantes_exercicios, participantes_apresentacao)

print("Distribuição dos exercícios:")
for participante, tarefas in atribuicao.items():
    print(f"{participante}: {', '.join(tarefas)}")

print("\nApresentadoras:")
print(", ".join(apresentadoras))