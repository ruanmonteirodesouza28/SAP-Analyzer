import pandas as pd
import matplotlib.pyplot as plt

# Lê o arquivo CSV gerado pelo gerar_dados.py
df = pd.read_csv("processos_sap.csv")

print("=" * 50)
print("   ANÁLISE DE PROCESSOS SAP")
print("=" * 50)

# ----------------------------------------
# 1. Tempo médio por módulo SAP
# ----------------------------------------
print("\n[1] Tempo medio (horas) por modulo SAP:")
tempo_medio = df.groupby("modulo_sap")["tempo_horas"].mean().round(2)
print(tempo_medio.to_string())

# ----------------------------------------
# 2. Quantidade de erros por departamento
# ----------------------------------------
print("\n[2] Quantidade de erros por departamento:")
erros = df[df["status"] == "erro"]  # Filtra só os processos com erro
erros_por_depto = erros.groupby("departamento")["processo_id"].count()
print(erros_por_depto.to_string())

# ----------------------------------------
# 3. Módulo com mais processos pendentes
# ----------------------------------------
print("\n[3] Processos pendentes por modulo SAP:")
pendentes = df[df["status"] == "pendente"]  # Filtra só os pendentes
pendentes_por_modulo = pendentes.groupby("modulo_sap")["processo_id"].count()
print(pendentes_por_modulo.to_string())

modulo_mais_pendente = pendentes_por_modulo.idxmax()
quantidade = pendentes_por_modulo.max()
print(f"\n>> Modulo com mais pendencias: {modulo_mais_pendente} ({quantidade} processos)")

# ----------------------------------------
# 4. Gráfico de barras: processos por status e módulo
# ----------------------------------------
print("\n[4] Gerando grafico de barras...")

# Conta quantos processos existem por módulo e status
contagem = df.groupby(["modulo_sap", "status"])["processo_id"].count().unstack(fill_value=0)

# Cria o gráfico
contagem.plot(kind="bar", figsize=(10, 6), color=["#e74c3c", "#2ecc71", "#f39c12"])

plt.title("Processos SAP por Módulo e Status", fontsize=14)
plt.xlabel("Módulo SAP")
plt.ylabel("Quantidade de Processos")
plt.xticks(rotation=0)  # Deixa os rótulos do eixo X na horizontal
plt.legend(title="Status")
plt.tight_layout()      # Ajusta o layout para não cortar nada

# Salva o gráfico como imagem e também mostra na tela
plt.savefig("grafico_processos.png")
print("Gráfico salvo como 'grafico_processos.png'")
plt.show()

print("\nAnalise concluida!")
