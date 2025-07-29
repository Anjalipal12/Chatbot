from dotenv import load_dotenv 
import streamlit as st 
import os 
import google.generativeai as genai 

# Step 1: Load environment variables from .env
load_dotenv() 

# Step 2: Configure Gemini API key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Step 3: Initialize Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Step 4: Create a function to handle user query
def get_gemini_response(query):
    response = model.generate_content(query)
    print("Gemini raw response:", response)   # 👈 yeh line add karo
    return response.text


# Step 5: Streamlit UI Setup
st.set_page_config(page_title="Sync_pro_bot")
st.header("🤖 Sync_pro_bot")

# Step 6: User input field
user_input = st.text_input("You:", placeholder="Ask anything...", key="input")  

# Step 7: Submit button
if st.button("Ask your query"):
    if user_input.strip() != "":
        with st.spinner("Thinking... 💭"):
            result = get_gemini_response(user_input)
            st.subheader("The Response is:")
            st.write(result)
    else:
        st.warning("Please enter a query to get a response.")
