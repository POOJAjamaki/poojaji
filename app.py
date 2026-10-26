import streamlit as st

# Kanji dictionary
kanji_dict = {
    "学校": "がっこう",
    "先生": "せんせい",
    "学生": "がくせい",
    "勉強": "べんきょう",
    "時間": "じかん",
    "電車": "でんしゃ",
    "食事": "しょくじ",
    "旅行": "りょこう",
    "会社": "かいしゃ",
    "日本語": "にほんご",
    "友達": "ともだち",
    "家族": "かぞく",
    "毎日": "まいにち",
    "天気": "てんき",
    "料理": "りょうり",
    "買い物": "かいもの",
    "病院": "びょういん",
    "仕事": "しごと",
    "名前": "なまえ",
    "電話": "でんわ"
}

# Title
st.title("漢字ふりがな表示アプリ")
st.write("N3レベルの漢字の読み方を表示します")

# User input
kanji = st.text_input("漢字を入力してください")

# Display button
if st.button("表示"):
    if kanji in kanji_dict:
        st.success(f"ふりがな: {kanji_dict[kanji]}")
    else:
        st.error("この漢字は登録されていません")

# Clear button
if st.button("クリア"):
    st.rerun()