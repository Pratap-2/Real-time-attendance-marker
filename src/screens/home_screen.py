import streamlit as st

def home_screen():
    
    st.header("Welcome to the School Management System!")

    st.write("Please select your login type to continue.")

    col1,col2=st.columns(2) 

    with col1:
        if st.button('Login as Teacher'):
            st.session_state['login_type']='teacher'
            st.rerun()

    with col2:
        if st.button('Login as Student'):
            st.session_state['login_type']='student'
            st.rerun()