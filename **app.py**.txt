{\rtf1\ansi\ansicpg949\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ```python\
import streamlit as st\
import pandas as pd\
st.set_page_config(page_title="\uc0\u44040 \u54788 3\u44396 \u50669  \u53456 \u49353 \u44592 ", layout="wide")\
st.title("\uc0\u55356 \u57313  \u44040 \u54788 3\u44396 \u50669  \u44077 \u53804 \u51088  \u53440 \u44191 ")\
data = \{\
'\uc0\u47588 \u47932 \u47749 ': ['\u44040 \u54788 A\u46041  \u48716 \u46972 ', '\u50672 \u49888 \u45236 \u50669  \u50669 \u49464 \u44428  \u48716 \u46972 ', '\u45824 \u51648 \u51648 \u48516  \u45824 \u54805  \u48716 \u46972 ', '\u52488 \u44592 \u53804 \u51088  \u52572 \u51200 \u44032 '],\
'\uc0\u47588 \u47588 \u44032 (\u47564 \u50896 )': [45000, 38000, 52000, 34000],\
'\uc0\u51204 \u49464 \u44032 (\u47564 \u50896 )': [25000, 23000, 24000, 21000]\
\}\
df = pd.DataFrame(data)\
df['\uc0\u44077 (\u47564 \u50896 )'] = df['\u47588 \u47588 \u44032 (\u47564 \u50896 )'] - df['\u51204 \u49464 \u44032 (\u47564 \u50896 )']\
max_gap = st.slider("\uc0\u50896 \u54616 \u45716  \u52572 \u45824  \u44077  (\u47564 \u50896 )", 5000, 30000, 15000, step=1000)\
filtered_df = df[df['\uc0\u44077 (\u47564 \u50896 )'] <= max_gap]\
st.dataframe(filtered_df.sort_values(by='\uc0\u44077 (\u47564 \u50896 )'), use_container_width=True)\
}