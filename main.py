# hello_world_function.py

import streamlit as st

st.markdown("""
    <style>
        div.stButton > button {
            background-color: #4CAF50; /* Green background */
            color: white; /* White text */
            font-size: 16px; /* Font size */
            padding: 10px 20px; /* Padding */
            border: none; /* Remove border */
            border-radius: 8px; /* Rounded corners */
            cursor: pointer; /* Pointer cursor on hover */ 
        }

        div.stButton > button:hover {
            background-color: #45a049; /* Darker green on hover */
        }
    </style>
    """, unsafe_allow_html=True)

# Define a function to display the "Hello, World" message
def display_message():
    st.title("MyLetter")
    st.write("Cliquer sur l'une des propositions suivantes pour commencer")

def render_rectangles(rectangles):
    """
    Renders rectangles with text in a 2x2 layout in Streamlit.
    
    Parameters:
    rectangles (list of str): A list of strings to display inside the rectangles. 
                              Should contain exactly 4 items.
    """
    
    if len(rectangles) != 4:
        st.error("The 'rectangles' list must contain exactly 4 items.")
        return

    # First row of rectangles
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Générer une lettre d'hébergement"):
            st.write("You clicked the styled button!")
    with col2:
        st.markdown(f"""
            <div style="border: 2px solid black; padding: 20px; text-align: center;">
                <p>{rectangles[1]}</p>
            </div>
        """, unsafe_allow_html=True)

    # Second row of rectangles
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"""
            <div style="border: 2px solid black; padding: 20px; text-align: center;">
                <p>{rectangles[2]}</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
            <div style="border: 2px solid black; padding: 20px; text-align: center;">
                <p>{rectangles[3]}</p>
            </div>
        """, unsafe_allow_html=True)

# Call the function inside the Streamlit app
if __name__ == "__main__":
    display_message()
    rectangle_texts = ["Attestation d'hébergement", "Attestation de prise en charge", "Attestation de versement d'une somme dans un compte courant français", "Lettre explicative de mes ressources financières"]
    render_rectangles(rectangle_texts)


    