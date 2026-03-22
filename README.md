# Previsão de Risco Acadêmico - Datathon Passos Mágicos

## Objetivo
Desenvolver um modelo de Machine Learning capaz de prever o risco de defasagem acadêmica de alunos, utilizando indicadores educacionais e psicossociais.

---

## Contexto
A Associação Passos Mágicos atua na transformação da vida de crianças e jovens por meio da educação. 
Este projeto utiliza dados reais de desempenho para gerar insights e apoiar decisões pedagógicas.

---

##  Estrutura do Projeto

- `Fiap_2_2_0.ipynb` → Análise exploratória e modelagem
- `app.py` → Aplicação interativa com Streamlit
- `modelo_risco_defasagem.pkl` → Modelo treinado
- `requirements.txt` → Dependências do projeto

---

## Análise de Dados

Principais insights encontrados:

- Evolução positiva do desempenho acadêmico até 2023
- Engajamento (IEG) possui relação direta com desempenho (IDA)
- Alunos mais engajados tendem a apresentar melhores resultados
- Indicadores psicossociais antecipam risco acadêmico

---

##  Modelo de Machine Learning

- **Algoritmo:** Random Forest
- **Tipo:** Classificação supervisionada
- **Objetivo:** Prever risco de defasagem

### 📈 Métricas:
- Accuracy: **0.88**
- ROC AUC: **0.95**

 O modelo apresentou alta capacidade preditiva e bom equilíbrio entre precisão e recall.

---

##  Aplicação com Streamlit

Foi desenvolvida uma aplicação interativa para simulação de risco acadêmico em tempo real.

###  Funcionalidades:
- Inserção de indicadores do aluno (IEG, IAA, IPS, etc.)
- Cálculo automático do risco
- Retorno com probabilidade de risco


###  Exemplo da aplicação:

![App Streamlit]()
<img width="1861" height="992" alt="Captura de tela 2026-03-22 160936" src="https://github.com/user-attachments/assets/b31ccc25-c9c5-4282-951f-09ff6ccf4cc6" />
<img width="1875" height="991" alt="Captura de tela 2026-03-22 160818" src="https://github.com/user-attachments/assets/c00b4248-d8bb-4c92-8f6a-0127de3650b6" />
---

##  Como executar o projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seu-usuario/datathon-passos-magicos.git
cd datathon-passos-magicos

pip install -r requirements.txt

streamlit run app.py
