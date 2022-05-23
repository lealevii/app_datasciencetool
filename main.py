import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image

st.markdown(
    """
<style>


[class^="st-b"]  {
    color: black;
    font-family: monospace;
}

.st-bb {
    background-color: #F5C5CE;
}
.st-at {
    background-color: #F0F2F6;
    color:black;
}

</style>
""",
    unsafe_allow_html=True,
)

image = Image.open('image/logo.png')
show = st.sidebar.image(image, use_column_width=True)
image2 = Image.open('image/description.png')
show = st.sidebar.image(image2, use_column_width=True)

image3 = Image.open('image/InstaQuote.png')
show = st.image(image3, use_column_width=True)

tags = st.selectbox('choisissez votre thème : ', ('love', 'humor', 'life', 'books', 'inspirational', 'friendship'))


url = f"https://quotes.toscrape.com/tag/{tags}/"

res = requests.get(url)

#Beautifulsoup prends le content des reponses, et html car les reponses sont en html
content = BeautifulSoup(res.content, 'html.parser')

quotes = content.find_all('div', class_='quote')
quote_file = []

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    link = quote.find('a')
    st.success(text)
    st.markdown(f"<a href = https://quotes.toscrape.com{link['href']}> {author} </a>", unsafe_allow_html=True)
    #st.code(f"https://quotes.toscrape.com{link['href']}")
    quote_file.append([text, author, link])

