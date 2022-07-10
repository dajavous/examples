import streamlit as st
from streamlit_folium import st_folium
import folium

# center on example
m = folium.Map(location=[53.081560, -0.753180], zoom_start=16)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)
