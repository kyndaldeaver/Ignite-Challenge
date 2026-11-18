pip install streamlit
import streamlit as st
 
st.title('Temperature Slide')
temp = st.slide('Set temperature',0,100,50)
st.write(f'You select {temp}')
