import streamlit as st
import pandas as pd
import joblib

st.title("Previsão de risco acadêmico")

# carregar modelo
modelo = joblib.load("modelo_risco_defasagem.pkl")

# inputs
fase = st.selectbox("Fase", ["0", "1", "2", "3", "4", "5", "6", "7", "ALFA"])
idade = st.number_input("Idade", 6, 25, 14)
genero = st.selectbox("Gênero", ["Masculino", "Feminino"])
iaa = st.slider("IAA", 0.0, 10.0, 5.0)
ieg = st.slider("IEG", 0.0, 10.0, 5.0)
ips = st.slider("IPS", 0.0, 10.0, 5.0)
ipp = st.slider("IPP", 0.0, 10.0, 5.0)
ida = st.slider("IDA", 0.0, 10.0, 5.0)
ipv = st.slider("IPV", 0.0, 10.0, 5.0)
inde = st.slider("INDE", 0.0, 10.0, 5.0)

if st.button("Prever risco"):
    entrada = pd.DataFrame([{
        "Fase": fase,
        "Idade": idade,
        "Gênero": genero,
        "IAA": iaa,
        "IEG": ieg,
        "IPS": ips,
        "IPP": ipp,
        "IDA": ida,
        "IPV": ipv,
        "INDE": inde
    }])

    pred = modelo.predict(entrada)[0]
    prob = modelo.predict_proba(entrada)[0][1]

    if pred == 1:
        st.error(f"Alto risco ({prob:.1%})")
    else:
        st.success(f"Baixo risco ({prob:.1%})")
