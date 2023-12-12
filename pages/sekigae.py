import streamlit as st
import pandas as pd
import numpy as np

# 8x7のランダムな数値を持つDataFrameを作成する
data = np.random.randint(1, 41, size=(6, 7))
df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(7)])

# Streamlitアプリケーションの作成
st.write("席替えシミュレーター")
st.subheader("かぶってるけどヨシ")

# ボタンを追加して数値をシャッフルして表示する
if st.button("シャッフル"):
    # データフレームの値をシャッフルする
    shuffled_df = df.apply(np.random.permutation, axis=0)
    st.write(shuffled_df)
else:
    st.write(df)
