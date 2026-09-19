import streamlit as st
with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )
from database import create_database,add_donor, get_donors

create_database()

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
    st.header("Donor Registeration")
    name = st.text_input("Enter your name")
elif menu == "Volunteer":
    st.header("About BloodConnect")
    st.write(
        "BloodConnect is a college developed  using"
        "Pyhton,Streamlit,HTML,and CSS."
    )                                                                                                                                                          
elif menu == "Register as Donor":

    st.header("Donor Registration")
    st.write("Enter your details to register as a blood donor.")

    name = st.text_input("Full Name")
    
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=65,
        step=1
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "Select Blood Group",
            "A+",
            "A-",
            "B+",
            "B-",
            "AB+",
            "AB-",
            "O+",
            "O-"
        ]
    )

    city = st.text_input("City/Location")
    phone = st.text_input("Phone Number")

    if st.button("Register as Donor"):

        if name.strip() == "":
            st.error("Please enter your name.")

        elif blood_group == "Select Blood Group":
            st.error("Please select your blood group.")

        elif city.strip() == "":
            st.error("Please enter your city.")

        elif phone.strip() == "":
            st.error("Please enter your phone number.")

        else:  add_donor(
        name,
        age,
        blood_group,
        city,
        phone
    )

        st.success("Donor registered successfully.")
elif menu == "Find Donor":

    st.header("Find a Blood Donor")

    st.markdown("""
    <div class="search-card">
        <h2>Search for Donors</h2>
        <p>Find registered donors by blood group and city.</p>
    </div>
    """, unsafe_allow_html=True)

    blood_group = st.selectbox(
        "Required Blood Group",
        ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    )

    city = st.text_input("Enter City")

    if st.button("Search Donor"):

        donors = get_donors()

        found = False

        for donor in donors:

            if donor[3] == blood_group and donor[4].lower() == city.lower():

                st.write("Name:", donor[1])
                st.write("Age:", donor[2])
                st.write("Blood Group:", donor[3])
                st.write("City:", donor[4])
                st.write("Phone:", donor[5])

                st.divider()

                found = True

        if not found:
            st.warning("No matching donor found.")   
elif menu == "Volunteer":

    st.header("Volunteer Registration")

    st.markdown("""
    <div class="form-card">
        <h2>Become a Volunteer</h2>
        <p>Support blood donation activities in your community.</p>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Volunteer Name")
    city = st.text_input("Volunteer City")
    phone = st.text_input("Contact Number")

    if st.button("Register as Volunteer"):

        if name == "":
            st.error("Please enter your name.")

        elif city == "":
            st.error("Please enter your city.")

        elif phone == "":
            st.error("Please enter your phone number.")

        else:
            st.success("Volunteer registered successfully.")  
elif menu == "About":

    st.header("About BloodConnect")

    st.markdown("""
    <div class="form-card">
        <h2>BloodConnect</h2>
        <p>
        BloodConnect is a web-based blood donor and volunteer
        finder application.
        </p>

        <p>
        It helps users find suitable blood donors based on
        blood group and location.
        </p>

        <p>
        The project is developed using Python, Streamlit,
        HTML, CSS and SQLite.
        </p>
    </div>
    """, unsafe_allow_html=True)                           
