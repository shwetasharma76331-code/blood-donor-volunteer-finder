import streamlit as st
st.set_page_config(
    page_title="BloodConnect",
    layout="wide"
)
# CSS
st.markdown("""
<style>
.main-title{
     font-size: 42px;
     font-weight: bold;
     text-align: center;
     margin-bottom: 10px;
}
.subtitle {
    font-size: 22px;
    text-align: center;
    margin-bottom: 25px;
}
.card{
    padding: 25px;
    border-radius: 12px;
    text-align: center;
    margin: 10px;
}
.second-title{
    font-size: 28px;
    font-weight: bold;
    margin-top: 25p;
}
</style>
""", unsafe_allow_html=True)
#HTML
st.markdown(
    '<divclass="main-title">BloodConnect</div>',
    unsafe_allow_html=True
) 
st.markdown(
    '<div class="subtitle">Blood Donor & Volunteer Finder</div>',
    unsafe_allow_html=True
)  
st.write(
    "A platform that helps connect people who need blood"
    "with suitable donors and volunteers."
)
st.divider()
menu=st.sidebar.selectbox(
    "Select Page",
    ["Home", "Find Donor",
     "Register as Donor", "Volunteer",
     "About"]
)        
if menu == "Home":
    st.header("Welcome to BloodConnect")
    st.write(
        "BloodConnect makes it easier to find blood donors"
        "and volunteers based on blood group and location."
         )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            '<div class="card"><h3>Find a Donor</h3>'
            '<p>Search donors according to blood group and location.</p></div>',
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="card"><h3>Register as a Donor</h3>'
            '<p>Register your details to help people in need.</p></div',
            unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            '<div class="card"><h3>Become a Volunteer</h3>'
            '<p>Join as a volunteer and support the community.</p><div>',
            unsafe_allow_html=True
        )    
        st.divider()
        st.header("How BloodConnect Works")
        st.write("""
        1. Select the required blood group.
        2. Enter your location.
        3. Search for available donors.
        4. Donors and Volunteers can register themselves.
          """)
elif menu == "Find Donor":
    st.header("Find a Blood Donor")
    st.info("Donor search feature will be added in Day 5.")
elif menu == "Register as Donor":
    st.header("Donor registeration form will be added in Day 3.")
elif menu == "Volunteer":
    st.header("About BloodConnect")
    st.write(
        "BloodConnect is a college developed  using"
        "Pyhton,Streamlit,HTML,and CSS."
    )                                                                                                                                                          
elif menu == "Register as Donor":
    st.header("Donor Registration")
    st.markdown("""
    <div class="form-card">
        <h2>Register as a Blood 
        Donor</h2>
                <p>Enter your details
        to help people who need
        blood.</p>
             </div>
            """,
    unsafe_allow_html=True)                                                                                                                      
    name = st.text_input("Full Name")
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        step=1
    )
    blood_group = st.selectbox(
        "Blood Group",
        ["Select Blood Group",
         "A+","A-","B+","B-",
         "AB+","AB-","0+","0-"]
    )
    city = st.text_input("City/Location")
    phone = st.text_input("Phone Number")
if st.button("Register as Donor"):
    if name == "":
      st.error("Please enter your name.")
    elif blood_group == "Select Blood Group":
        st.error("Please enter your blood group.")
    elif city == "":
        st.error("Please enter your city.")
    elif phone == "":
        st.error("Please enter your phone number.")
    else:
        st.success("Donor registration submitted succesfully.")                     