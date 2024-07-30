import streamlit as st
import pyqrcode
import png
from pyqrcode import QRCode
from io import BytesIO

def generate_qr_code(data):
    qr = pyqrcode.create(data)
    buffer = BytesIO()
    qr.png(buffer, scale=4)
    buffer.seek(0)
    return buffer

st.title("QR Code Generator")

# Session state to keep track of the input
if 'data' not in st.session_state:
    st.session_state.data = ""

# Input for the user to enter the data for the QR code
data = st.text_input("Digite para gerar o seu QR Code:", st.session_state.data)

if st.button("Gerar QR Code"):
    st.session_state.data = data

if st.button("Limpar"):
    data=''
    st.session_state.data = data
    st.experimental_rerun()  # Rerun the app to clear the input field
    #st.experimental_set_query_params()

if st.session_state.data:
    qr_buffer = generate_qr_code(st.session_state.data)
    
    st.image(qr_buffer, caption='Gerar QR Code',width=300)
    
    # Download button
    st.download_button(
        label="Download QR Code",
        data=qr_buffer,
        file_name="qr_code.png",
        mime="image/png"
    )

    #streamlit run c:/Users/NTI-003/Desktop/Codigos/Projetos/streamlit/streamlit_qr_code.py --server.port 8502
