# SAP Process Analyzer

Projeto Python que simula e analisa dados de processos corporativos no estilo SAP.
Criado para fins de estudo, nível iniciante em Python.

---

## O que o projeto faz

- **`gerar_dados.py`**  Gera um arquivo CSV com 200 processos SAP falsos (simulados), contendo módulo, tempo, status e departamento.
- **`analise.py`**  Lê o CSV e exibe:
  - Tempo médio por módulo SAP (FI, MM, SD, HR)
  - Quantidade de erros por departamento
  - Qual módulo tem mais processos pendentes
  - Um gráfico de barras com a distribuição dos processos

---

## Estrutura de arquivos

```
sap-process-analyzer/
├── gerar_dados.py       # Gera o CSV com dados falsos
├── analise.py           # Lê o CSV e faz a análise
├── requirements.txt     # Bibliotecas necessárias
└── README.md            # Este arquivo
```

Após rodar os scripts, dois arquivos novos aparecem na pasta:
- `processos_sap.csv` — dados gerados
- `grafico_processos.png` — gráfico salvo automaticamente

---

## Como instalar as bibliotecas

Abra o terminal na pasta do projeto e rode:

```bash
pip install -r requirements.txt
```

---

## Como rodar

**Passo 1 — Gerar os dados:**
```bash
python gerar_dados.py
```

**Passo 2 — Rodar a análise:**
```bash
python analise.py
```

---

## Bibliotecas utilizadas

| Biblioteca  | Para que serve                          |
|-------------|------------------------------------------|
| `pandas`    | Ler e manipular o CSV                   |
| `matplotlib`| Criar o gráfico de barras               |
| `random`    | Gerar dados aleatórios (já vem no Python)|
| `csv`       | Escrever o arquivo CSV (já vem no Python)|

---

## Exemplo de saída no terminal

```
==================================================
   ANÁLISE DE PROCESSOS SAP
==================================================

Tempo médio (horas) por módulo SAP:
FI    23.45
HR    25.10
MM    22.87
SD    24.33

Erros por departamento:
Financeiro    8
Logística     7
RH            6
TI            9
Vendas        5

Módulo com mais pendências: HR (15 processos)
```
