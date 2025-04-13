import streamlit as st
import requests

def generate_letter_content():
    # Construct the prompt based on letter type
    if st.session_state.letterState == "Attestation d'hébergement":
        prompt = f"""Rédige uniquement le **corps** d'une attestation d'hébergement en français, sans mention de lieu, date ni objet.
        Informations :
        - Hébergeur : {st.session_state.hostName} {st.session_state.hostLastName}
        - Hébergé : {st.session_state.guestName} {st.session_state.guestLastName}
        - Adresse : {st.session_state.hostAddress}
        - Durée d'hébergement : {st.session_state.duration}
        
        Le texte doit être formel et certifier que l'hébergeur accepte d'héberger l'hébergé à cette adresse pour la durée mentionnée."""

    elif st.session_state.letterState == "Attestation de prise en charge financière":
        prompt = f"""Rédige uniquement le **corps** d'une attestation de prise en charge financière en français, sans mention de lieu, date ni objet.
        Informations :
        - Garant : {st.session_state.guarantorName} {st.session_state.guarantorLastName}
        - Bénéficiaire : {st.session_state.beneficiaryName} {st.session_state.beneficiaryLastName}
        - Revenu mensuel du garant : {st.session_state.guarantorIncome}€
        - Durée de la prise en charge : {st.session_state.duration}
        
        Le texte doit être formel et exprimer l'engagement du garant à prendre en charge financièrement le bénéficiaire durant cette période."""

    elif st.session_state.letterState == "Attestation de versement":
        prompt = f"""Rédige uniquement le **corps** d'une attestation de versement en français, sans mention de lieu, date ni objet.
        Informations :
        - Titulaire du compte : {st.session_state.accountHolderName} {st.session_state.accountHolderLastName}
        - Banque : {st.session_state.bankName}
        - Montant : {st.session_state.amount}€
        - IBAN : {st.session_state.accountNumber}
        
        Le texte doit être formel et certifier le versement du montant indiqué sur le compte bancaire mentionné."""

    elif st.session_state.letterState == "Lettre de motivation":
        prompt = f"""Rédige uniquement le **corps** d'une lettre de motivation en français, sans mention de lieu, date ni objet.
        Informations :
        - Candidat : {st.session_state.applicantName} {st.session_state.applicantLastName}
        - Programme d'études : {st.session_state.studyProgram}
        - Université/École : {st.session_state.university}
        - Situation actuelle : {st.session_state.currentSituation}
        - Motivations : {st.session_state.motivation}
        
        Le texte doit être convaincant, formel, adapté à une candidature académique, et mettre en valeur le parcours et les motivations du candidat."""

    # OpenRouter API configuration
    headers = {
        "Authorization": "Bearer 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",  # Replace with your actual API key
        "HTTP-Referer": "YOUR_WEBSITE",  # Replace with your website
        "Content-Type": "application/json"
    }

    # API request payload
    payload = {
        "model": "anthropic/claude-3-sonnet",  # Or any other model you prefer
        "messages": [{
            "role": "user",
            "content": prompt
        }]
    }

    # Make the API request
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        # Extract the generated letter from the response
        letter_content = response.json()["choices"][0]["message"]["content"]
        return letter_content
    else:
        st.error("Failed to generate letter content")
        return None