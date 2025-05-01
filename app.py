import streamlit as st
import pandas as pd
import pickle

# Laad het getrainde model (compatibel met scikit-learn 1.2)
with open("model_streamlit_sklearn12.pkl", "rb") as f:
    model = pickle.load(f)

# Titel
st.title("Schatting staalgewicht onderconstructie voor siloblok")

# Invoer siloblok
st.header("Afmetingen siloblok")
silo_lengte = st.number_input("Lengte siloblok (m)", value=5.0)
silo_breedte = st.number_input("Breedte siloblok (m)", value=5.0)
silo_hoogte = st.number_input("Hoogte siloblok (m)", value=4.0)

# Invoer soortelijk gewicht
st.header("Producteigenschappen")
soortelijk_gewicht = st.number_input("Soortelijk gewicht (kg/m³)", value=800)

# Invoer onderconstructie
st.header("Afmetingen onderconstructie")
lengte = st.number_input("Lengte onderconstructie (m)", value=5.0)
breedte = st.number_input("Breedte onderconstructie (m)", value=5.0)
hoogte = st.number_input("Hoogte onderconstructie (m)", value=9.5)

# Berekening
if st.button("Voorspel staalgewicht"):
    silo_volume = silo_lengte * silo_breedte * silo_hoogte
    belasting = silo_volume * soortelijk_gewicht / 1000  # ton

    input_df = pd.DataFrame([{
        "lengte_m": lengte,
        "breedte_m": breedte,
        "hoogte_m": hoogte,
        "silo_lengte_m": silo_lengte,
        "silo_breedte_m": silo_breedte,
        "silo_hoogte_m": silo_hoogte,
        "soortelijk_gewicht_kg_m3": soortelijk_gewicht,
        "silo_volume_m3": silo_volume,
        "belasting_product_ton_corr": belasting
    }])

    voorspelling = model.predict(input_df)[0]
    st.success(f"Geschat staalgewicht: {voorspelling:.0f} kg")