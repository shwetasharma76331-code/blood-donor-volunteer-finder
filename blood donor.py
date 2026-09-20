import streamlit as st
import sqlite3
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Blood Connect",
    page_icon="🩸",
    layout="wide"
)
st.markdown(
("<h2>Welcome to Blood Connect</h2>"),
     unsafe_allow_html=True)

# =========================================================
# DATABASE
# =========================================================

conn = sqlite3.connect(
    "blood_connect.db",
    check_same_thread=False
)

cursor = conn.cursor()

# Donor table
cursor.execute("""
CREATE TABLE IF NOT EXISTS donors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    blood_group TEXT NOT NULL,
    city TEXT NOT NULL,
    contact TEXT NOT NULL,
    availability TEXT
)
""")

# Volunteer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS volunteers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact TEXT NOT NULL,
    city TEXT NOT NULL,
    availability TEXT,
    help_type TEXT
)
""")

conn.commit()

# =========================================================
# HTML + CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f8f9fa;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    color: #d71920;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #555555;
    margin-bottom: 30px;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #eeeeee;
    margin-bottom: 20px;
}

.section-title {
    color: #d71920;
    font-size: 30px;
    font-weight: bold;
}

.info-box {
    background-color: #fff1f1;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #d71920;
}

.feature-card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #eeeeee;
    min-height: 170px;
}

.stButton > button {
    width: 100%;
    border-radius: 8px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
    """
    <h1 style="color:#d71920;">🩸 Blood Connect</h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.write("❤️ Blood Donor & Volunteer Finder")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "📌 Navigation",
    [
        "🏠 Home",
        "🔍 Find Blood Donor",
        "🩸 Register Donor",
        "🤝 Volunteer",
        "🗄️ Database Records",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("❤️ Together We Save Lives")


# =========================================================
# HOME PAGE
# =========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">🩸 Blood Connect</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">❤️ Blood Donor & Volunteer Finder</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h2 style="text-align:center;">
    ❤️ Connecting Blood Donors, Recipients & Volunteers
    </h2>

    <p style="text-align:center;">
    Blood Connect is a simple platform that helps people
    find blood donors and volunteers quickly.
    </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>🔍 Find Blood</h3>
        <p>
        Search for donors according to blood group
        and city.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🩸 Become a Donor</h3>
        <p>
        Register yourself as a blood donor and
        help someone in need.
        </p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>🤝 Become a Volunteer</h3>
        <p>
        Register as a volunteer and support people
        during emergencies.
        </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <div class="info-box">

    <h3>🎯 Our Mission</h3>

    <p>
    Our mission is to make blood donor searching easier,
    faster and more organized by connecting donors,
    recipients and volunteers.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FIND BLOOD DONOR
# =========================================================

elif page == "🔍 Find Blood Donor":

    st.markdown(
        '<div class="section-title">🔍 Find a Blood Donor</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Search for a suitable donor using blood group and city."
    )

    col1, col2 = st.columns(2)

    with col1:

        blood_group = st.selectbox(
            "🩸 Blood Group",
            [
                "All",
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

    with col2:

        city = st.text_input(
            "📍 City / Location",
            placeholder="Enter city name"
        )

    if st.button("🔎 Search Donor"):

        query = """
        SELECT
            name,
            age,
            blood_group,
            city,
            contact,
            availability
        FROM donors
        WHERE 1=1
        """

        params = []

        if blood_group != "All":
            query += " AND blood_group = ?"
            params.append(blood_group)

        if city.strip():
            query += " AND LOWER(city) LIKE LOWER(?)"
            params.append("%" + city.strip() + "%")

        data = pd.read_sql_query(
            query,
            conn,
            params=params
        )

        st.subheader("❤️ Available Donors")

        if len(data) > 0:

            st.dataframe(
                data,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.warning(
                "😔 No matching donor found."
            )


# =========================================================
# REGISTER DONOR
# =========================================================

elif page == "🩸 Register Donor":

    st.markdown(
        '<div class="section-title">🩸 Register as a Blood Donor</div>',
        unsafe_allow_html=True
    )

    st.write(
        "❤️ Enter your details to register as a donor."
    )

    with st.form("donor_form"):

        name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your name"
        )

        age = st.number_input(
            "🎂 Age",
            min_value=18,
            max_value=100,
            value=18
        )

        blood_group = st.selectbox(
            "🩸 Blood Group",
            [
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

        city = st.text_input(
            "📍 City",
            placeholder="Enter your city"
        )

        contact = st.text_input(
            "📞 Contact Number",
            placeholder="Enter phone number"
        )

        availability = st.selectbox(
            "🕐 Availability",
            [
                "Available",
                "Not Available",
                "Available on Emergency"
            ]
        )

        submitted = st.form_submit_button(
            "❤️ Register Donor"
        )

        if submitted:

            if not name or not city or not contact:

                st.error(
                    "⚠️ Please fill all required fields."
                )

            else:

                cursor.execute(
                    """
                    INSERT INTO donors
                    (
                        name,
                        age,
                        blood_group,
                        city,
                        contact,
                        availability
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        name,
                        age,
                        blood_group,
                        city,
                        contact,
                        availability
                    )
                )

                conn.commit()

                st.success(
                    "✅ Donor registered successfully!"
                )


# =========================================================
# VOLUNTEER PAGE
# =========================================================

elif page == "🤝 Volunteer":

    st.markdown(
        '<div class="section-title">🤝 Become a Volunteer</div>',
        unsafe_allow_html=True
    )

    st.write(
        "❤️ Register yourself as a volunteer and help people in need."
    )

    with st.form("volunteer_form"):

        name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your name"
        )

        contact = st.text_input(
            "📞 Contact Number",
            placeholder="Enter phone number"
        )

        city = st.text_input(
            "📍 City",
            placeholder="Enter your city"
        )

        availability = st.selectbox(
            "🕐 Availability",
            [
                "Available",
                "Not Available",
                "Available on Emergency"
            ]
        )

        help_type = st.selectbox(
            "🤝 Help Type",
            [
                "Blood Donation Support",
                "Emergency Support",
                "Donor Searching",
                "Awareness",
                "Other"
            ]
        )

        submitted = st.form_submit_button(
            "❤️ Register Volunteer"
        )

        if submitted:

            if not name or not contact or not city:

                st.error(
                    "⚠️ Please fill all required fields."
                )

            else:

                cursor.execute(
                    """
                    INSERT INTO volunteers
                    (
                        name,
                        contact,
                        city,
                        availability,
                        help_type
                    )
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        name,
                        contact,
                        city,
                        availability,
                        help_type
                    )
                )

                conn.commit()

                st.success(
                    "✅ Volunteer registered successfully!"
                )


# =========================================================
# DATABASE RECORDS
# =========================================================

elif page == "🗄️ Database Records":

    st.markdown(
        '<div class="section-title">🗄️ Database Records</div>',
        unsafe_allow_html=True
    )

    st.write(
        "📊 View donor and volunteer records stored in the database."
    )

    tab1, tab2 = st.tabs(
        [
            "🩸 Donor Records",
            "🤝 Volunteer Records"
        ]
    )

    # ---------------- DONORS ----------------

    with tab1:

        donors = pd.read_sql_query(
            "SELECT * FROM donors",
            conn
        )

        if len(donors) > 0:

            st.dataframe(
                donors,
                use_container_width=True,
                hide_index=True
            )

            st.info(
                f"🩸 Total Donors: {len(donors)}"
            )

        else:

            st.info(
                "📭 No donor records available."
            )

    # ---------------- VOLUNTEERS ----------------

    with tab2:

        volunteers = pd.read_sql_query(
            "SELECT * FROM volunteers",
            conn
        )

        if len(volunteers) > 0:

            st.dataframe(
                volunteers,
                use_container_width=True,
                hide_index=True
            )

            st.info(
                f"🤝 Total Volunteers: {len(volunteers)}"
            )

        else:

            st.info(
                "📭 No volunteer records available."
            )


# =========================================================
# ABOUT PAGE
# =========================================================

elif page == "ℹ️ About":

    st.markdown(
        '<div class="section-title">ℹ️ About Blood Connect</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

    <h3>🎯 Project Objective</h3>

    <p>
    Blood Connect is a blood donor and volunteer finder
    application designed to make it easier to find suitable
    blood donors and volunteers.
    </p>

    <h3>⚙️ How It Works</h3>

    <ol>
        <li>🔍 Search for a blood donor.</li>
        <li>🩸 Register as a blood donor.</li>
        <li>🤝 Register as a volunteer.</li>
        <li>🗄️ Store information in the database.</li>
        <li>📊 View registered records.</li>
    </ol>

    <h3>💻 Technologies Used</h3>

    <ul>
        <li>🐍 Python</li>
        <li>🌐 Streamlit</li>
        <li>HTML</li>
        <li>CSS</li>
        <li>🗄️ SQLite Database</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)

    st.success(
        "❤️ Together We Can Save Lives!"
    )


# =========================================================
# CLOSE DATABASE
# =========================================================

# Database connection remains active while Streamlit is running.                          
