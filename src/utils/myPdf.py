import src.services.cllm as cllm
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap
import streamlit as st
from datetime import datetime
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

pdfmetrics.registerFont(TTFont("Poppins", "assets/fonts/Poppins-Regular.ttf"))



def generate():
    # Use it in your canvas

    # Get the generated letter content
    letter_content = cllm.generate_letter_content()
    if not letter_content:
        return None

    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setFont("Poppins", 12)
    c.setTitle(st.session_state.letterState)

    width, height = letter
    line_height = 15
    right_margin = 50
    left_margin = 50
    text_width = width - left_margin - right_margin
    y_position = 750

    # Coordonnées de l'expéditeur (en haut à droite)
    sender_info = [
        f"{st.session_state.senderFirstName} {st.session_state.senderLastName}",
        st.session_state.senderPhone,
        st.session_state.senderAddress
    ]
    for line in sender_info:
        c.drawString(left_margin, y_position, line)
        y_position -= line_height

    # Espace entre expéditeur et destinataire
    y_position -= 20

    # Coordonnées du destinataire (en haut à droite aussi)
    recipient_info = [
        st.session_state.recipientInstitution
    ]
    for line in recipient_info:
        c.drawRightString(width - right_margin, y_position, line)
        y_position -= line_height

    # Espace avant le corps de la lettre
    y_position -= 40

    # Corps de la lettre
    for paragraph in letter_content.split('\n'):
        wrapped_lines = wrap(paragraph, width=80)  # ajusté selon largeur
        for line in wrapped_lines:
            if y_position < 50:
                c.showPage()
                y_position = 750
            c.drawString(left_margin, y_position, line)
            y_position -= line_height
        y_position -= 10  # espace entre paragraphes

    # Bas de page : lieu, date, signature (en bas à droite)
    y_position = 100
    today = datetime.today().strftime("%d/%m/%Y")
    footer_lines = [
        f"Fait à {st.session_state.senderCity}, le {today}",
        "",
        "Signature"
    ]
    for line in footer_lines:
        c.drawRightString(width - right_margin, y_position, line)
        y_position -= line_height

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer
