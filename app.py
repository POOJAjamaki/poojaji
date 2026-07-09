# app.py

import streamlit as st

# N3 level Kanji dictionary
kanji_dict = {
    "学校": "がっこう",
    "先生": "せんせい",
    "会社": "かいしゃ",
    "仕事": "しごと",
    "時間": "じかん",
    "電車": "でんしゃ",
    "駅": "えき",
    "病院": "びょういん",
    "旅行": "りょこう",
    "料理": "りょうり",
    "勉強": "べんきょう",
    "電話": "でんわ",
    "住所": "じゅうしょ",
    "家族": "かぞく",
    "友達": "ともだち",
    "天気": "てんき",
    "新聞": "しんぶん",
    "映画": "えいが",
    "毎日": "まいにち",
    "便利": "べんり"
}

# App title
st.title("漢字ふりがな表示アプリ")
st.write("N3レベルの漢字の読み方を表示します")

# User input
kanji = st.text_input("漢字を入力してください")

# Button
if st.button("表示"):
    if kanji in kanji_dict:
        st.success(f"ふりがな: {kanji_dict[kanji]}")
    else:
        st.error("この漢字は登録されていません")

# Clear button
if st.button("クリア"):
    st.write("")