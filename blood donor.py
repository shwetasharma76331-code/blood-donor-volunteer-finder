import streamlit as st
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