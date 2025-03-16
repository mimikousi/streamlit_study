import streamlit as st

#ブラウザタブのアイコンに使用
icon ='https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg'
mimikousi_icon = 'business_kousi.jpeg'

layout = 'wide'
#layout = 'centered'

st.set_page_config(
    page_title='Markdown Cheatsheet',
    page_icon=icon,
    layout=layoutss
)

st.logo(mimikousi_icon, link='https://github.com/mimikousi')