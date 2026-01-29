import streamlit as st
st.title ("Conversor de lempiras a dolares en entorno virtual de Iza")

lempiras=st.number_input("Digita la cantidad en LPS para convertir a dolares", min_value=1)
if st.button("Ejecutar"):
    dolares=lempiras/26.00
    st.write(f"El resultado de la conversion es: $ {dolares: .2f}")



