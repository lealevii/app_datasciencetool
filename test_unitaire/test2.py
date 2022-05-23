#ici on verifie qu'on arrive bien à envoyer la requete

import streamlit as st
import requests

tags = st.selectbox('choisissez votre thème : ', ('love', 'humor', 'life', 'books', 'inspirational', 'friendship'))

url = f"https://quotes.toscrape.com/tag/{tags}/"

res = requests.get(url)
st.write(res)
