import streamlit as st

#ブラウザタブのアイコンに使用
icon ='https://upload.wikimedia.org/wikipedia/commons/4/48/Markdown-mark.svg'
mimikousi_icon = r'pages/business_kousi.jpg'

layout = 'wide'
#layout = 'centered'

st.set_page_config(
    page_title='Markdown Cheatsheet',
    page_icon=icon,
    layout=layout
)

st.logo(mimikousi_icon, link='https://github.com/mimikousi')

st.markdown('# Markdown チートシート')
left, right = st.columns(2)
left.markdown('**:memo:テキスト書式**')
left.markdown('''
    要素 | :green[HTML] | 用法
    ---|---|---
    見出し | `<h1>～<h6>` | `## 見出し`
    太字 | `<strong>` | `**太字**`
    斜体 | `<em>` | `*斜体*`
    取り消し | `<strike>` | `~~取り消し~~`
    引用 | `<blockquote>` | `> 引用文`
    コード | `<code>` | `` ` `` `` ` ``
    区切り線 | `<hr>` | `---`
    改行 | `<br/>` | `␣␣`（空白2つ）
    ESC | -- | `\\`（特殊文字）
''')

with right:
    st.markdown('**:clipboard: リスト**')
    st.markdown('''
要素 | :green-background[HTML] | 用法
---|---|---
順序なし | `<ul><li>` | `- `
順番付き | `<ol><li>` | `1.`
''')
    
    with st.expander('**リンク**', icon='🔗'):
        st.markdown('''
            要素 | HTML | 用法
            ---|---|---
            リンク | `<a href=...>` | `[文字列](url)`
            画像 | `<img src=...>` | `![代替テキスト](url)`
            ''')

with right.expander('**表**', icon=':material/table:', expanded=True):
    '''```
ヘッダ1 | ヘッダ2 | ヘッダ3 
---|---|---
行1セル1 | 行1セル2 | 行1セル3
行2セル1 | 行2セル2 | 行2セル3
行3セル1 | 行3セル2 | 行3セル3
```'''

st.markdown('----')
#段組みコンテナ
cols = st.columns(
    3,#[0.2, 0.5, 0.3]を指定すると指定した割合で分割
    gap='large',#デフォルトは'small'、'medium'も使える
    vertical_alignment='center'#デフォルトは'top'（上端揃え）、'bottom'(下端揃え)も使用可能
)
st.markdown('----')

numbers = ':blue[0]123456789'*3

for i in range(3):
    cols[i].markdown(numbers)