import random
import csv

# Listas com as opções possíveis para cada coluna
modulos_sap = ["FI", "MM", "SD", "HR"]
status_opcoes = ["concluído", "pendente", "erro"]
departamentos = ["Financeiro", "Logística", "Vendas", "RH", "TI"]

# Nome do arquivo que será gerado
nome_arquivo = "processos_sap.csv"

# Abre o arquivo CSV para escrita
with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)

    # Escreve o cabeçalho (nomes das colunas)
    escritor.writerow(["processo_id", "modulo_sap", "tempo_horas", "status", "departamento"])

    # Gera 200 linhas de dados falsos
    for i in range(1, 201):
        processo_id = f"PROC-{i:04d}"          # Ex: PROC-0001
        modulo = random.choice(modulos_sap)     # Escolhe um módulo aleatório
        tempo = round(random.uniform(0.5, 48.0), 2)  # Tempo entre 0.5h e 48h
        status = random.choice(status_opcoes)   # Escolhe um status aleatório
        departamento = random.choice(departamentos)  # Escolhe um departamento

        escritor.writerow([processo_id, modulo, tempo, status, departamento])

print(f"Arquivo '{nome_arquivo}' gerado com sucesso! 200 processos criados.")
