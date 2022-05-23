#ici on verifie que l'url s'affiche bien avec le mot choisis dans la box

import streamlit as st

tags = st.selectbox('choisissez votre thème : ', ('love', 'humor', 'life', 'books', 'inspirational', 'friendship'))

url = f"https://quotes.toscrape.com/tag/{tags}/"
st.write(url)
