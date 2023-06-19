import streamlit as st
import pandas as pd
from process_n_nuc import process_n_nuc
from process_mean_std import process_mean_std

st.title('Automatic plate.tsv processing')
st.write("""
1. **Upload** a file.tsv
2. **Choose** the type of processing to carry out 
3. **Download** the processed.csv file

*** Remember to **remove** the existing file before uploading a new one
""")

tsv = st.file_uploader('Choose a file')
action = st.selectbox('What processing would you like to carry out?', ['n_nuc', 'mean_std'])

st.write('#')
st.write('#')

if tsv is None:
    st.title('Upload a file to proceed')
else:
    file = process_n_nuc(tsv) if action == 'n_nuc' else process_mean_std(tsv)
    st.download_button(f'Download the {action} processed file', file.to_csv(), 'processed.csv')