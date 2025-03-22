import streamlit as st
import pandas as pd

# データの読み込み
@st.cache_data
def load_data():
    df = pd.read_csv("players.csv", encoding="utf-8-sig")
    return df

df = load_data()

# チーム名を動的に取得
teams = ["チーム選択なし"] + list(df["チーム名"].unique())  # 初期値として「チーム選択なし」を追加

# サイドバーでチームを選択
selected_team = st.sidebar.selectbox("チームを選択", teams)

st.title("高校野球")

# チームが選択されていない場合はメッセージを表示
if selected_team == "チーム選択なし":
    # h2のような見出しを作成
    st.write("チームを選択してください。")
else:
    # 選択されたチームの選手一覧を表示
    filtered_df = df[df["チーム名"] == selected_team].drop(columns=["チーム名"])

    st.markdown(f"## {selected_team}")
    st.markdown(f"### 選手一覧")
    st.dataframe(filtered_df, hide_index=True)
