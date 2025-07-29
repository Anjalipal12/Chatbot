import streamlit as st

def main():
    st.title("Gemini Chatbot 💬")

    user_input = st.text_input("Ask something:")

    if user_input:
        st.write("You asked:", user_input)
        st.success("Response: (Chatbot response here)")  # Placeholder

if __name__ == "__main__":
    main()

