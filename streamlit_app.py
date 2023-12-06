# Streamlitライブラリをインポート
import streamlit as st
import numpy as np

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('Streamlitのサンプルアプリ')

student = st.slider('生徒数を選んでください', 100, 1000)
avg_val = st.number_input('平均点を入力してください', value=0)
max_val = st.number_input('分散を入力してください', value=10)
target_val = st.number_input('偏差値を求めたい点数を入力してください', value=10)

if st.button('偏差値を求める'):
    st.write(f'偏差値は「{((target_val - avg_val)/np.sqrt(max_val)*10) + 50}」です。')