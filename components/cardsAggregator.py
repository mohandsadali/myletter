import streamlit as st
import components.inputModalWindow as inputModalWindow

def generate(caseTypeElements, caseTypeElementsDescriptions, rows, cols):
    """
    Renders clickable cards in a grid layout in Streamlit.
    
    Parameters:
    caseTypeElements (list of str): A list of strings to display inside the clickable cards
    rows (int): Number of rows in the grid
    cols (int): Number of columns in the grid
    total_cards (int): Total number of clickable cards to display
    """
    
    total_cards = len(caseTypeElements)

    card_index = 0
    for row in range(rows):
        columns = st.columns(cols)
        for col in range(cols):
            if card_index < total_cards:
                with columns[col]:
                    with st.container():
                        st.markdown(f'<div>{caseTypeElements[card_index]}</div>', unsafe_allow_html=True)
                        st.markdown(f'<p>{caseTypeElementsDescriptions[card_index]}</p>', unsafe_allow_html=True)
                        if st.button("", key=caseTypeElements[card_index]):
                            st.session_state.letterState = caseTypeElements[card_index]
                            inputModalWindow.generateLetter(caseTypeElements[card_index])
                card_index += 1