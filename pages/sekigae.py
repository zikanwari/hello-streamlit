import streamlit as st
import pandas as pd
import numpy as np

# 8x7のランダムな数値を持つDataFrameを作成する
data = np.random.randint(1, 100, size=(8, 7))
df = pd.DataFrame(data, columns=[f"Column {i+1}" for i in range(7)])

# Streamlitアプリケーションの作成
st.write("8x7 Table with Random Values")
df