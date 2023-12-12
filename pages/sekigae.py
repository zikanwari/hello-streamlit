import streamlit as st
import pandas as pd
import numpy as np

# 重複のない8x7のランダムな数値を持つDataFrameを作成する
data = np.random.choice(np.arange(1, 101), size=(8, 7), replace=False)
df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(7)])

# Streamlitアプリケーションの作成
st.write("8x7 Table with Unique Random Values")

# ボタンを追加して数値をシャッフルして表示する
if st.button("シャッフル"):
    # 重複のない新しいデータを作成し、データフレームを更新する
    new_data = np.random.choice(np.setdiff1d(np.arange(1, 101), df.values.flatten()), size=(8, 7), replace=False)
    df = pd.DataFrame(new_data, columns=[f"Column {i+1}" for i in range(7)])
    st.write(df)
else:
    st.write(df)
