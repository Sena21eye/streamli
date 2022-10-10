import numpy as np
import pandas as pd
import streamlit  as st
from PIL import Image

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

import time

for i in range(100):
  latest_interation.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

text = st.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味は', text,'です'

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:',condition

option = st.sidebar.selectbox(
    'あなたが好きな数字を教えてください'
    ,list(range(1,11))
)

'あなたの好きな数字は、', option ,'です'

st.write('Display Image')

if st.sidebar.checkbox('Show Image'):
  Img = Image.open('sample.JPG')
  st.image(Img, caption = 'Hiroki Takei', use_column_width = True)

st.write('DataFrame')

#pandasの特徴にpandas.DataFrameというオブジェクトがある。データフレームで２次元の表形式のデータを処理する
# https://docs.pyq.jp/python/pydata/pandas/dataframe.html

df = pd.DataFrame(
    np.random.rand(100,2)/[50, 50] + [35.69, 139.70]
    ,columns=['lat', 'lon']
)

#map作った緯度と経度が分かればできた
st.map(df)

#折れ線グラフ作った
st.line_chart(df)

#エリアチャート作った
st.area_chart(df)

#棒グラフ
st.bar_chart(df)

#表を表示させるためにst.writeを使う()の中は表示させたいDataFrame
st.write(df)

st.table(df.style.highlight_max(axis=0))

# マジックコマンド
# マークダウンとは
#https://tech-camp.in/note/technology/84353/

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """