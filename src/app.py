import streamlit as st
from pathlib import Path
from services.blob_services import upload_blob
from services.credit_card_service import analize_credit_card

def configure_interface():
    st.title("Upload de Arquivo Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        blob_url = upload_blob(uploaded_file, fileName)
        
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analize_credit_card(blob_url) 
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(image_url, credit_card_info):
    st.image(image_url, caption="Imagem enviada", use_column_width=True)
    
    if credit_card_info:
        st.subheader("Informações do Cartão de Crédito Detectadas:")
        st.write(f"Nome do Titular: {credit_card_info.get('card_name', 'N/A')}")
        st.write(f"Número do Cartão: {credit_card_info.get('card_number', 'N/A')}")
        st.write(f"Data de Expiração: {credit_card_info.get('expiry_date', 'N/A')}")
        st.write(f"Nome do Banco: {credit_card_info.get('bank_name', 'N/A')}")
    else:
        st.write("Nenhuma informação de cartão de crédito detectada.")