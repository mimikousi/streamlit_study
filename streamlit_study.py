import streamlit as st

st.snow()
st.balloons()

st.title('Hello World`<h1>`',
         help='``はoption+_で入力できる（Mac）')

st.header('大見出し `<h2>`')

st.subheader(
    body='中見出し`<h3>`',
    anchor='title',
    help='`<h3>`あるいは`###``に相当するStreamlitのコマンド',
    divider=True
)

st.caption('キャプション"<caption>"')

st.text('''
        あいうえお
        かきくけこ
        さしすせそ
        たちつてと
        なにぬねの
        はひふへほ
        まみむめも
        やゐゆゑよ
        わをん       
''')

st.code('''
        import streamlit as st
        st.snow()
        ''',
        language='python',
        line_numbers=True
)

#コードを表示してから実行
with st.echo(code_location='above'): #'below'にすると実行が先になる
    st.title(':red[風船アニメーション]', anchor='balloon')
    st.balloons()
