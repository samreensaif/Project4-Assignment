import streamlit as st

# Set the title and sidebar
st.set_page_config(page_title="My Python Website", page_icon="🌟", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "About", "Contact"])



# Home Page
if page == "Home":
    st.image("avatar.webp", width=200, caption="Samreen Saif")
    st.title("Welcome to My Python Website!")
    st.write("This is a simple website built with Streamlit in just 15 minutes. 🚀")

    # Interactive Slider
    st.header("Interactive Slider Example")
    number = st.slider("Select a number:", 1, 100)
    st.write(f"Your selected number is {number}!")

    # Data Input Example
    st.header("Form Example")
    name = st.text_input("Enter your name:")
    if st.button("Submit"):
        st.write(f"Hello, {name}! Thank you for visiting.")

# About Page
elif page == "About":
    st.title("About This Website")
    st.write("""
    This website is built using **Streamlit**, a Python framework for creating interactive web applications easily.

    - **Author:** [Samreen Saif](https://portfolio-ncfinal.vercel.app)
    - **Purpose:** Demonstrating how to build Python-powered websites quickly.
    - **Features:** Interactive widgets, easy data input, and more.
    """)

# Contact Page
elif page == "Contact":
    st.title("Contact Us")
    st.write("Feel free to get in touch!")

    # Simple Contact Form
    email = st.text_input("Enter your email:")
    message = st.text_area("Your message:")
    if st.button("Send"):
        st.write("Thank you for your message. We will get back to you shortly!")

