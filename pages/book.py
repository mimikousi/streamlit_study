#!/usr/bin/env -S python -m streamlit run

import streamlit as st
from aozora import get_aozora, parse_text_into_sentences
from wc import get_tokens, get_pos_ids, get_wordcloud

@st.cache_data
def retrieve_aozora(url):
    print(f'Retrieving Aozora: {url}.')
    return get_aozora(url)


@st.cache_data
def prepare_pos_ids():
    print(f'Retriving POS_IDs.')
    return get_pos_ids()


@st.cache_data
def process_tokens(text):
    print(f'Generating tokens from the text.')
    return get_tokens(text)


tab_text, tab_wc = st.tabs(['テキスト', 'ワードクラウド'])

with tab_text:
    aozora_url = st.text_input('**青空文庫 Zip ファイル URL**', value='https://www.aozora.gr.jp/cards/000074/files/427_ruby_19792.zip')

with tab_wc:
    pos_ids = prepare_pos_ids()
    pos_list = st.multiselect('品詞', pos_ids, default='名詞')

if aozora_url is not None:
    try:
        text = retrieve_aozora(aozora_url)
    except Exception as e:
        st.error(
            f'`{aozora_url}`が取得できない、あるいはそのZipが正しく解凍できませんでした。',
            icon=':material/network_locked:')
        st.exception(e)
        st.stop()

    with tab_text:
        st.markdown(text.replace('\n', '\n\n'))

    with tab_wc:
        tokens = process_tokens(text)
        img = get_wordcloud(tokens, pos_list)
        st.image(img, width=800)
