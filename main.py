import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import requests  # Add this import at the top

st.markdown("""
    <style>
        div.stButton > button {
            background-color: #4CAF50; /* Green background */
            color: black; /* White text */
            font-size: 16px; /* Font size */
            padding: 10px 20px; /* Padding */
            border: none; /* Remove border */
            border-radius: 8px; /* Rounded corners */
            cursor: pointer; /* Pointer cursor on hover */ 
            box-shadow: 0 1.5em 2.5em -.5em rgba(#000000, .1);
        }

        div.stButton > button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
        
        div.stTitle {
            color : blue;
        }

        .custom-text {
            font-size: 18px;
            color: gray;
        }

        .input-div {
            display: block;
            margin: auto;
            width: 50rem;
            height: 15rem;
            background-color: white;
            padding: 10px;
            border: 1px solid blue;
            border-radius: 5px;
        }

    </style>
    """, unsafe_allow_html=True)

st.session_state.letterState = ""
st.session_state.hostName = ""
st.session_state.hostLastName = ""
st.session_state.guestName = ""
st.session_state.guestLastName = ""

def generate_letter_content():
    # Construct the prompt with session state variables
    prompt = f"""Please generate a formal letter for {st.session_state.letterState}.
    Host Name: {st.session_state.hostName} {st.session_state.hostLastName}
    Guest Name: {st.session_state.guestName} {st.session_state.guestLastName}
    Please write this letter in French."""

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

def generate_pdf():
    # Get the generated letter content
    letter_content = generate_letter_content()
    if not letter_content:
        return None
        
    buffer = io.BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    c.setTitle("Generated Letter")
    
    # Add the generated content to PDF
    y_position = 750  # Starting position
    for line in letter_content.split('\n'):
        c.drawString(100, y_position, line)
        y_position -= 20  # Move down for next line
    
    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

@st.dialog("Veuillez saisir les informations suivantes")
def generateLetter(letterType):
    st.write("Remplissez les informations suivantes pour pouvoir générer une", st.session_state.letterState)
    hostName = st.text_input("Quel est le nom de l'hébergeur ?")
    hostLastName = st.text_input("Quel est le prénom de l'hébergeur ?")
    guestName = st.text_input("Quel est le nom de l'hébergé?")
    guestLastName = st.text_input("Quel est le prénom de l'hébergé?")
    
    if st.button("Génerer ma lettre"):
        # Set the session state variables directly
        st.session_state.hostName = hostName
        st.session_state.hostLastName = hostLastName
        st.session_state.guestName = guestName
        st.session_state.guestLastName = guestLastName
        
        # Generate PDF after setting the state variables
        pdf_buffer = generate_pdf()
        
        st.download_button(
            label="Télécharger le PDF",
            data=pdf_buffer,
            file_name="lettre.pdf",
            mime="application/pdf"
        )

def renderLetterType(letterType):
    """
    Renders letterType buttons with text in a 2x2 layout in Streamlit.
    
    Parameters:
    letterType (list of str): A list of strings to display inside the letterType. 
                              Should contain exactly 4 items.
    """
    
    if len(letterType) != 4:
        st.error("The 'letterType' list must contain exactly 4 items.")
        return

    # First row of letterType
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(letterType[0]):
            st.session_state.letterState = letterType[0]
            generateLetter(letterType[0])

    with col2:
        if st.button(letterType[1]):
            st.session_state.letterState = letterType[1]
            generateLetter(letterType[1])


    # Second row of letterType
    col3, col4 = st.columns(2)
    
    with col3:
        if st.button(letterType[2]):
            st.session_state.letterState = letterType[2]
            generateLetter(letterType[2])

            
    with col4:
        if st.button(letterType[3]):
            st.session_state.letterState = letterType[3]
            generateLetter(letterType[3])

# Call the function inside the Streamlit app
if __name__ == "__main__":

    st.markdown("<h1> MyLetter </h1>", unsafe_allow_html=True)
    st.markdown("<p class='custom-text'>Que voudriez-vous générer aujourd'hui ?</p>", unsafe_allow_html=True)
    rectangle_texts = ["Attestation d'hébergement", "Attestation de prise en charge", "Attestation de versement d'une somme dans un compte courant français", "Lettre explicative de mes ressources financières"]
    renderLetterType(rectangle_texts)



    