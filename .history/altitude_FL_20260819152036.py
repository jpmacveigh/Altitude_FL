import streamlit as st
from alti_fl import alti_FL
st.set_page_config(
    page_title="Altitude d'un FL",
    page_icon="✈️",
    layout="centered"
)
st.title("✈️ Altitude géométrique d'un niveau de vol")
st.write(
    "Calcul de l'altitude géométrique correspondant à un FL "
    "en fonction du QNH et de la température au sol."
)
# Entrées
FL = st.number_input(
    "FL",
    min_value=1,
    max_value=650,
    value=115,
    step=5
)
T_sol = st.number_input(
    "Température au sol (°C)",
    min_value=-60.0,
    max_value=60.0,
    value=35.0,
    step=0.1
)
QNH = st.number_input(
    "QNH (hPa)",
    min_value=900,
    max_value=1100,
    value=1013,
    step=1
)
# Calcul
altitude=alti_FL(FL,QNH,T_sol)
#st.write(f"**Altitude pression du FL{FL:03.0f} :** {altitude:.0f} m")
st.markdown(
    f"<h2>Altitude pression du FL{FL:03.0f} : {altitude:.0f} m</h2>",
    unsafe_allow_html=True
)