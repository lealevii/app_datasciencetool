#ici on verifie que Beautifulsoup prends bien le "content" des reponses

import streamlit as st
import requests
from bs4 import BeautifulSoup

tags = st.selectbox('choisissez votre thème : ', ('love', 'humor', 'life', 'books', 'inspirational', 'friendship'))

url = f"https://quotes.toscrape.com/tag/{tags}/"

res = requests.get(url)

#Beautifulsoup prends le content des reponses, et html car les reponses sont en html
content = BeautifulSoup(res.content, 'html.parser')
st.code(content)
