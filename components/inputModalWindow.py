import streamlit as st
import src.utils.myPdf as myPdf

@st.dialog("Veuillez saisir les informations suivantes")
def generateLetter(letterType):
    st.write("Remplissez les informations suivantes pour pouvoir générer une", st.session_state.letterState)
    
    st.session_state.senderFirstName = st.text_input("Prénom de l'expéditeur")
    st.session_state.senderLastName = st.text_input("Nom de l'expéditeur")
    st.session_state.senderPhone = st.text_input("Numéro de téléphone de l'expéditeur")
    st.session_state.senderAddress = st.text_input("Adresse complète de l'expéditeur")
    st.session_state.senderCity = st.text_input("Ville de rédaction de la lettre")
    st.session_state.recipientInstitution = st.text_input("Nom de l'organisme destinataire (préfecture, consulat, etc.)")

    
    if st.session_state.letterState == "Attestation d'hébergement":
        hostName = st.text_input("Quel est le nom de l'hébergeur ?")
        hostLastName = st.text_input("Quel est le prénom de l'hébergeur ?")
        guestName = st.text_input("Quel est le nom de l'hébergé ?")
        guestLastName = st.text_input("Quel est le prénom de l'hébergé ?")
        hostAddress = st.text_input("Quelle est votre adresse complète ?")
        duration = st.text_input("Quelle est la durée d'hébergement prévue ?")
        
    elif st.session_state.letterState == "Attestation de prise en charge financière":
        guarantorName = st.text_input("Quel est le nom du garant ?")
        guarantorLastName = st.text_input("Quel est le prénom du garant ?")
        beneficiaryName = st.text_input("Quel est le nom du bénéficiaire ?")
        beneficiaryLastName = st.text_input("Quel est le prénom du bénéficiaire ?")
        guarantorIncome = st.number_input("Quel est votre revenu mensuel (en euros) ?", min_value=0)
        duration = st.text_input("Quelle est la durée de prise en charge prévue ?")
        
    elif st.session_state.letterState == "Attestation de versement":
        accountHolderName = st.text_input("Quel est le nom du titulaire du compte ?")
        accountHolderLastName = st.text_input("Quel est le prénom du titulaire du compte ?")
        bankName = st.text_input("Quel est le nom de la banque ?")
        amount = st.number_input("Quel est le montant du versement (en euros) ?", min_value=0)
        accountNumber = st.text_input("Quel est le numéro de compte (IBAN) ?")
        
    elif st.session_state.letterState == "Lettre de motivation":
        applicantName = st.text_input("Quel est votre nom ?")
        applicantLastName = st.text_input("Quel est votre prénom ?")
        studyProgram = st.text_input("Quel est le programme d'études visé ?")
        university = st.text_input("Quelle est l'université ou l'école visée ?")
        currentSituation = st.text_area("Quelle est votre situation actuelle ?")
        motivation = st.text_area("Quelles sont vos motivations principales ?")

    if st.button("Générer", key="generate"):
        if st.session_state.letterState == "Attestation d'hébergement":
            st.session_state.hostName = hostName
            st.session_state.hostLastName = hostLastName
            st.session_state.guestName = guestName
            st.session_state.guestLastName = guestLastName
            st.session_state.hostAddress = hostAddress
            st.session_state.duration = duration
            
        elif st.session_state.letterState == "Attestation de prise en charge financière":
            st.session_state.guarantorName = guarantorName
            st.session_state.guarantorLastName = guarantorLastName
            st.session_state.beneficiaryName = beneficiaryName
            st.session_state.beneficiaryLastName = beneficiaryLastName
            st.session_state.guarantorIncome = guarantorIncome
            st.session_state.duration = duration
            
        elif st.session_state.letterState == "Attestation de versement d'une somme dans un compte courant français":
            st.session_state.accountHolderName = accountHolderName
            st.session_state.accountHolderLastName = accountHolderLastName
            st.session_state.bankName = bankName
            st.session_state.amount = amount
            st.session_state.accountNumber = accountNumber
            
        elif st.session_state.letterState == "Lettre de motivation":
            st.session_state.applicantName = applicantName
            st.session_state.applicantLastName = applicantLastName
            st.session_state.studyProgram = studyProgram
            st.session_state.university = university
            st.session_state.currentSituation = currentSituation
            st.session_state.motivation = motivation
        
        # Generate PDF after setting the state variables
        pdf_buffer = myPdf.generate()
        
        st.download_button(
            label="Télécharger",
            data=pdf_buffer,
            file_name="lettre.pdf",
            mime="application/pdf"
        )