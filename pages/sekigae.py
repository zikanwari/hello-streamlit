import streamlit as st
import pandas as pd
import numpy as np

# 8x7のランダムな数値を持つDataFrameを作成する
data = np.random.choice(np.arange(1, 42), size=(6, 7), replace=False)
df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(7)])

# Streamlitアプリケーションの作成
st.write("席替え")

# ボタンを追加して数値をシャッフルして表示する
if st.button("シャッフル"):
    new_data = np.random.choice(np.setdiff1d(np.arange(1, 42), df.values.flatten()), size=(6, 7), replace=False)
    df = pd.DataFrame(new_data, columns=[f"Column {i+1}" for i in range(7)])
    df
else:
    df
