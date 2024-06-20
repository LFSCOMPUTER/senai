# pip install streamlit

import streamlit as st

with st.sidebar:
    st.title("Calculadora IMC")

    st.header("IMC: Deefinição?")

    st.write("Índice de Massa Corporal (IMC")

    st.write("É o índice que relaciona peso e altura de uma pessoa")

    st.write("É utilizado como medida de saúde geral e para determinar se uma pessoa está em um pesoa saudável para a sua altura")

st.title("Calculadora")

peso = st.number_input(label= "Digite o seu peso em kg", min_value=0.0)

altura = st.number_input(label="Digite a sua altura em metros", min_value=0.0)

if st.button("Calcular"):

    imc = peso / (altura ** 2)
    imc = round(imc, 2)
    st.write(f"Seu IMC é {imc}")


