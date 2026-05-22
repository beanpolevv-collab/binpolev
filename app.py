import streamlit as st
import pandas as pd

st.set_page_config(page_title="갈현3구역 탐색기", layout="wide")
st.title("🏡 갈현3구역 갭투자 타겟")

# 가상 매물 데이터
data = {
    '매물명': ['갈현A동 빌라', '연신내역 역세권 빌라', '대지지분 대형 빌라', '초기투자 최저가'],
    '매매가(만원)': [45000, 38000, 52000, 34000],
    '전세가(만원)': [25000, 23000, 24000, 21000]
}
df = pd.DataFrame(data)
df['갭(만원)'] = df['매매가(만원)'] - df['전세가(만원)']

# 폰에서 조절할 슬라이더
max_gap = st.slider("원하는 최대 갭 (만원)", 5000, 30000, 15000, step=1000)

# 필터링 결과 보여주기
filtered_df = df[df['갭(만원)'] <= max_gap]
st.dataframe(filtered_df.sort_values(by='갭(만원)'), use_container_width=True)
