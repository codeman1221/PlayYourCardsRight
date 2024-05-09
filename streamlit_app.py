import streamlit as st
import random 
from streamlit import session_state as session

def game():
    st.title("Higher or Lower Game")
    st.write("Welcome! Guess whether the next card will be higher or lower than the current card.")
    
    if 'score' not in session:
        session.score = 0
        session.option = list(range(1, 14))
        session.first_card = None
        session.end = False
    if session.score < 5:
        if session.first_card is None:
            session.first_card = random.choice(session.option)

        second_card = random.choice(session.option)

        with st.form("my_form"):
            st.write(f"First card: {session.first_card}")

            human_input = st.selectbox("Higher Or Lower", options=["Lower", "Higher"])

            submitted = st.form_submit_button("Submit")

            if submitted:
                if (human_input == "Lower" and session.first_card > second_card) or \
                   (human_input == "Higher" and session.first_card < second_card):
                    st.write(f"Correct! It was {second_card}")
                    session.score += 1
                    st.write(f"Score: {session.score}")
                else:
                    st.write(f"Wrong! It was {second_card}")
                    st.write(f"Score: {session.score}")
                    end = True

                session.first_card = second_card
        if end == True:
            st.write("You Lost")
            session.clear()  # Reset session state after winning
        if session.score >= 5:
            st.write("Congratulations! You won!")
            session.clear()  # Reset session state after winning

if __name__ == "__main__":
    game()
