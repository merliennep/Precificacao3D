import streamlit as st
from calculos import calcular_preco
from banco import criar_tabela, salvar_peca, listar_pecas

criar_tabela()


st.title("Sistema Interno de Precificação 3D")

st.header("Dados da Impressão")


dados = {
    "preco_kg": st.number_input("Preço do filamento (R$/kg)", 0.0, value=68.0),
    "peso_g": st.number_input("Peso usado (g)", 0.0, value=196.96),
    "potencia_w": st.number_input("Potência da impressora (W)", 0, value=400),
    "tempo_h": st.number_input("Tempo de impressão (h)", 0.0, value=6.27),
    "kwh": st.number_input("Valor do kWh (R$)", 0.0, value=0.95),
    "valor_maquina": st.number_input("Valor da impressora (0 se quitada)", 0.0, value=0.0),
    "horas_trabalho": st.number_input("Horas de trabalho manual", 0.0, value=1.0),
    "petg": st.checkbox("Material PETG", value=True),
    "multipartes": st.checkbox("Peça multipartes", value=True),
    "acabamento": st.selectbox("Acabamento", ["nenhum", "lixa", "pintura"]),
    "markup": st.slider("Markup", 2.0, 8.0, 6.0)
}

dados["nome"] = st.text_input("Nome da peça", "Prateleira Modular")

if st.button("Calcular preço"):
    resultado = calcular_preco(dados)

    st.success("Resultado")
    st.write(f"Custo total: R$ {resultado['custo_total']}")
    st.write(f"Preço de venda: R$ {resultado['preco_venda']}")
    st.write(f"Lucro: R$ {resultado['lucro']}")

if st.button("Salvar peça no banco"):
    salvar_peca(dados, resultado)
    st.success("Peça salva com sucesso!")

