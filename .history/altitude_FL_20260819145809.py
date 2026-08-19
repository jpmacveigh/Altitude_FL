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


# ------------------------------------------------------------
# Entrées
# ------------------------------------------------------------

FL = st.number_input(
    "FL",
    min_value=1,
    max_value=650,
    value=115,
    step=1
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
    min_value=900.0,
    max_value=1100.0,
    value=1013.25,
    step=0.1
)

# ------------------------------------------------------------
# Calcul
# ------------------------------------------------------------

if st.button("Calculer", type="primary"):
        altitude=alti_FL(FL,QNH,T_sol)
        st.write("---")
        st.write(f"**Altitude pression du FL{FL:03.0f} :** {altitude:.0f} m")
        st.write(f"**QNH :** {QNH:.1f} hPa")
        st.write(f"**Température au sol :** {T_sol:.1f} °C")

