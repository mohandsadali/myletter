import streamlit as st
import pathlib

import components.cardsAggregator as cardsAggregator

# Function to load CSS from the 'assets' folder
def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the external CSS
css_path = pathlib.Path("assets/custom_style.css")
load_css(css_path)

st.session_state.senderFirstName = ""  # Prénom de l'expéditeur
st.session_state.senderLastName = ""  # Nom de l'expéditeur
st.session_state.senderPhone = ""      # Numéro de téléphone
st.session_state.senderAddress = ""   # Adresse postale
st.session_state.senderCity = ""      # Ville pour "Fait à"
st.session_state.recipientInstitution = ""  # Nom de l'organisme destinataire


# Attestation d'hébergement
st.session_state.hostName = ""
st.session_state.hostLastName = ""
st.session_state.guestName = ""
st.session_state.guestLastName = ""
st.session_state.hostAddress = ""
st.session_state.duration = ""

# Attestation de prise en charge financière
st.session_state.guarantorName = ""
st.session_state.guarantorLastName = ""
st.session_state.beneficiaryName = ""
st.session_state.beneficiaryLastName = ""
st.session_state.guarantorIncome = 0
st.session_state.duration = ""

# Attestation de versement
st.session_state.accountHolderName = ""
st.session_state.accountHolderLastName = ""
st.session_state.bankName = ""
st.session_state.amount = 0
st.session_state.accountNumber = ""

# Lettre de motivation
st.session_state.applicantName = ""
st.session_state.applicantLastName = ""
st.session_state.studyProgram = ""
st.session_state.university = ""
st.session_state.currentSituation = ""
st.session_state.motivation = ""

# Call the function inside the Streamlit app
if __name__ == "__main__":
    st.header("My Letter")
    st.markdown("<p class='custom-text'>Quelle lettre voudriez-vous génerer aujourd'hui ?</p>", unsafe_allow_html=True)
    visaLetters = ["Attestation d'hébergement", "Attestation de prise en charge financière", "Attestation de versement", "Lettre de motivation"]
    visaLettersDescriptions = ["Certifiez l'hébergement d'une personne à votre domicile", "Garantissez le soutien financier d'un étudiant","Confirmez le dépôt d'argent sur un compte bancaire", "Exprimez votre motivation pour vos études en France"]
    cardsAggregator.generate(visaLetters, visaLettersDescriptions, 2, 2)
    