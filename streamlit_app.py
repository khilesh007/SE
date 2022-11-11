import streamlit as st
import requests
import pandas as pd
import numpy as np
import warnings
from txtai.embeddings import Embeddings

warnings.simplefilter(action='ignore', category=FutureWarning)

st.set_page_config(page_title="Text Module Search Engine", page_icon="search", layout='centered')

st.title('Text Module Search')

key=st.text_input(label='Enter Keyword')

submit_button = st.button('Search')
#--------------------------------------------------------------------------

data=pd.read_excel(r"data.xlsx")

embeddings = Embeddings({
    
    "path": "T-Systems-onsite/german-roberta-sentence-transformer-v2"
})

embeddings.load("models")

txtai_data = []
i=0
for text in data['Article']:
    txtai_data.append((i, text, None))
    i=i+1

#----------------------------------------------------------------------------





if(submit_button):
    
    res = embeddings.search(key, 5)

    st.title("Showing Results....")

    for i in res:
        st.write(data['Title'][i[0]])
        st.write(txtai_data[i[0]][1])
        st.write(" ")

st.write('')
st.write('')
st.write('')

