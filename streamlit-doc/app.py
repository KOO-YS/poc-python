import streamlit as st

# Add a title to your app
st.title("Login")

# Add some text input
user_id = st.text_input("Enter ID:")

# Display the input
st.write(f"You entered: {user_id}")


