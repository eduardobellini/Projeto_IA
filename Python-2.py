import streamlit as st
from Modelo import gerar_resumo

st.title("IA de Resumo de Textos 📚")
texto = st.text_area("Digite o texto para resumir:")

if st.button("Gerar Resumo"):
    resumo = gerar_resumo(texto)
    st.write("### Resumo:")
    st.write(resumo)
