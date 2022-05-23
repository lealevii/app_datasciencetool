#ici on verifie qu'on a pris les bonnes classes et qu'on arrive bien à ressortir l'auteur et le "content"

import streamlit as st
import requests
from bs4 import BeautifulSoup


tags = st.selectbox('choisissez votre thème : ', ('love', 'humor', 'life', 'books', 'inspirational', 'friendship'))


url = f"https://quotes.toscrape.com/tag/{tags}/"

res = requests.get(url)

content = BeautifulSoup(res.content, 'html.parser')

quotes = content.find_all('div', class_='quote')
quote_file = []

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    st.write(author)
