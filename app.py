
import streamlit as st
from calculos import calcular_preco
from banco import criar_tabela, salvar_peca, listar_pecas

criar_tabela()

usuarios = {
    "voce": "1234",
    "noivo": "5678"
}

user = st.text_input("Usuário")
senha = st.text_input("Senha", type="password")

if usuarios.get(user) != senha:
    st.stop()
    
st.title("Sistema de Precificação 3D")

dados = {}
dados["nome"] = st.text_input("Nome da peça")
dados["preco_kg"] = st.number_input("Preço do filamento (R$/kg)", value=68.0)
dados["peso_g"] = st.number_input("Peso usado (g)", value=196.96)
dados["potencia_w"] = st.number_input("Potência da impressora (W)", value=400)
dados["tempo_h"] = st.number_input("Tempo de impressão (h)", value=6.27)
dados["kwh"] = st.number_input("Valor do kWh (R$)", value=0.95)
dados["valor_maquina"] = st.number_input("Valor da impressora", value=0.0)
dados["horas_trabalho"] = st.number_input("Horas de trabalho", value=1.0)
dados["petg"] = st.checkbox("Material PETG", True)
dados["multipartes"] = st.checkbox("Peça multipartes", True)
dados["acabamento"] = st.selectbox("Acabamento", ["nenhum", "lixa", "pintura"])
dados["markup"] = st.slider("Markup", 2.0, 8.0, 6.0)

if st.button("Calcular preço"):
    resultado = calcular_preco(dados)

st.success("Resultado")
st.write(f"Custo total: R$ {resultado['custo_total']}")
st.write(f"Preço de venda: R$ {resultado['preco_venda']}")
st.write(f"Lucro: R$ {resultado['lucro']}")

if st.button("Salvar peça no banco"):
    salvar_peca(dados, resultado)
    st.success("Peça salva com sucesso!")

st.header("📚 Histórico de Peças")

pecas = listar_pecas()

for p in pecas:
    st.write(
        f"🧩 {p[1]} | {p[2]} | "
        f"Preço: R$ {p[6]} | Lucro: R$ {p[7]} | "
        f"Data: {p[9]}"
    )

