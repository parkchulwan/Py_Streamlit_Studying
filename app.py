import streamlit as st

view = [100, 150, 30]
st.write('# Youtbue view count')
view

st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview