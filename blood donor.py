import streamlit as st
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=true
    )

st.set_page_config(
    page_title="BloodConnect",
    layout="wide"
)
st.title("BloodConnect")
st.subheader("Blood Donor & Volunteer Finder")
st.write(
    "Connecting people who need blood with donors volunteers."
)
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Find a Donor")
    st.write("Search for a suitable blood donor.")
    st.button("Find Donor")
with col2:
    st.header("Register as Donor")
    st.write("Register yourself as a blood donor.")
    st.button("Register Donor")
with col3:
    st.header("Become a Volunteer")
    st.write("Join us and help in people in need.")
    st.button("Register Volunteer")
st.divider()
st.header("How BloodConnect Works")
st.write("""
1. Search for the required blood group.
2. Find available donors.
3. Donors can register their dettails.
4. Volunteers can register to help.""")            

import streamlit as st
st.set_page_config(
    page_title="BloodConnect",
    layout="wide"
)
st.markdown(
    '<div class="main-title">BloodConnect</div>',
    unsafe_allow_html=true
)
st.markdown(
    '<div class="main-title">Blood Donor & Volunteer Finder</div>',
    unsafe_allow_html=true
)
st.subheader("Blood Donor & Volunteer Finer")
st.write("A platform that helps  connect people who need blood" \
"with suitable donors and volunteers.")
st.divider()
menu = st.sidebar.selectbox(
    "select page",
    ["Home","Find Donor",
     "Register as Donor","Volunteer","About"]
)
if menu == "Home":
    st.header("Welcome to Blood Connect")
    st.write("BloodConnect makes it easier to find blood donors" \
    "and volunteers based on blood group and location. ")
    col1 ,col2,col3 = st.columns(3)
    with col1:
        st.subheader("Find a Donor")
st.write("Search for donors according to blood group and location.")
with col2:
    st.subheader("Register as a donor")
    st.write("Register your details to help people in need.")
    with col3:
        st.subheader("Become a Volunteer")
st.write("Join as a volunteer and support the community.")
st.divider()
st.header("How BloodConnect Works")
st.write("""
1. Select the required blood group.
2. Enter your location.
3. Search for available donors.
4. Donors and volunteers can register themselves.
""")
