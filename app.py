import streamlit as st
import pandas as pd

yen_tama = 83.3
df_waza = pd.read_csv('waza_machine_data.csv')

def calc_margin_rate(waza_tama, waza_yen):
    purchase = yen_tama * waza_tama
    margin = waza_yen - purchase
    rate = margin / purchase
    return round(rate*100)

st.write('# 技マシンの番号を入力')
w1_number = st.number_input('技マシン1のナンバー', step=1, value=1, min_value=1, max_value=100)
w2_number = st.number_input('技マシン2のナンバー', step=1, value=1, min_value=1, max_value=100)
w3_number = st.number_input('技マシン3のナンバー', step=1, value=1, min_value=1, max_value=100)
w4_number = st.number_input('技マシン4のナンバー', step=1, value=1, min_value=1, max_value=100)
_, mei1, yen1 = df_waza[df_waza['No']==w1_number].values[0]
_, mei2, yen2 = df_waza[df_waza['No']==w2_number].values[0]
_, mei3, yen3 = df_waza[df_waza['No']==w3_number].values[0]
_, mei4, yen4 = df_waza[df_waza['No']==w4_number].values[0]

st.write('# 技マシンの交換に必要なタマの種類と数')
w1_kind_tama = st.selectbox('技マシン1の交換に必要なタマの種類', ['赤タマ','青タマ'])
w1_buy_tama = st.number_input('技マシン1のの購入タマ数', step=1, value=10, min_value=1, max_value=90)
w2_kind_tama = st.selectbox('技マシン2の交換に必要なタマの種類', ['赤タマ','青タマ'])
w2_buy_tama = st.number_input('技マシン2のの購入タマ数', step=1, value=10, min_value=1, max_value=90)
w3_kind_tama = st.selectbox('技マシン3の交換に必要なタマの種類', ['赤タマ','青タマ'])
w3_buy_tama = st.number_input('技マシン3のの購入タマ数', step=1, value=10, min_value=1, max_value=90)
w4_kind_tama = st.selectbox('技マシン4の交換に必要なタマの種類', ['赤タマ','青タマ'])
w4_buy_tama = st.number_input('技マシン4のの購入タマ数', step=1, value=10, min_value=1, max_value=90)

# st.write('# 技マシンの売値を入力')
# w1_sell_price = st.number_input(f'1【No. {w1_number} {df_waza.iloc[w1_number-1, 1]}】', step=100, value=1500, min_value=100, max_value=9000)
# w2_sell_price = st.number_input(f'2【No. {w2_number} {df_waza.iloc[w2_number-1, 1]}】', step=100, value=1500, min_value=100, max_value=9000)
# w3_sell_price = st.number_input(f'3【No. {w2_number} {df_waza.iloc[w2_number-1, 1]}】', step=100, value=1500, min_value=100, max_value=9000)
# w4_sell_price = st.number_input(f'4【No. {w2_number} {df_waza.iloc[w2_number-1, 1]}】', step=100, value=1500, min_value=100, max_value=9000)

w1_rate = calc_margin_rate(w1_buy_tama, yen1)
w2_rate = calc_margin_rate(w2_buy_tama, yen2)
w3_rate = calc_margin_rate(w3_buy_tama, yen3)
w4_rate = calc_margin_rate(w4_buy_tama, yen4)

st.write('# 利益率')
st.write(f'【No.{w1_number} {mei1}】利益率1: {w1_rate}% -> {w1_kind_tama}: {w1_buy_tama}個と交換')
st.write(f'【No.{w2_number} {mei2}】利益率2: {w2_rate}% -> {w2_kind_tama}: {w2_buy_tama}個と交換')
st.write(f'【No.{w3_number} {mei3}】利益率3: {w3_rate}% -> {w3_kind_tama}: {w3_buy_tama}個と交換')
st.write(f'【No.{w4_number} {mei4}】利益率4: {w4_rate}% -> {w4_kind_tama}: {w4_buy_tama}個と交換')

st.markdown('''
## ※参考\n
しかくいだいざM: べにタマS 12個\n
えんけいのだいざM: あおタマS 12個
'''
)

