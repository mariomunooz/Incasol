import streamlit as st
import streamlit.components.v1 as components

# Load the HTML file
with open('multiple_plots2.html', 'r') as f:
    html_string = f.read()

# Display the HTML
st.title("Visualització dels Indicadors de cada projecte")
components.html(html_string, height=800)