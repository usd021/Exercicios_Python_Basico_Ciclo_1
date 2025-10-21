import streamlit as st

st.sidebar.title("aluguel de carros")
st.sidebar.image("logo.png")
st.sidebar.write("escolha o carro ideal para voce!")
carros = ["Gol", "BMW", "Toro","Corsa"]

opcao= st.sidebar.selectbox("selecione o modelo do carro:", carros)

st.title("maximus cars - aluguel de carros")
st.image(f"{opcao}.png")
st.markdown(f"## voce alugou o modelo: {opcao}")

dias = st.text_input(f'por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'quantos km voce rodou com o {opcao}')

if opcao == "BMW":
    diaria = 3000

elif opcao == "Gol":
    diaria = 500

elif opcao == "Toro":
    diaria = 800

elif opcao == "Corsa":
    diaria = 800


if st.button("calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total= total_dias + total_km

    st.warning(f"voce alugou o {opcao} por {dias} dias e rodou{km} km. valor total a pagar é R${aluguel_total:.2f}")