import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_calendar import calendar

# Set page configuration
st.set_page_config(page_title="Roster Management", page_icon="📆", layout="wide", initial_sidebar_state="expanded")

# Apply background color from config
st.markdown(
    """
    <style>
    body {
        background-color: #F5F5F5;
        font-family: 'sans serif';
        color: #212121;
    }
    .stSidebar {
        background-color: #E0E0E0;
    }
    .profile-image {
        border-radius: 10px;
        padding: 5px;
        border: 2px solid #4CAF50;
        width: 150px;
        height: 150px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Option Menu Navigation
with st.sidebar:
    selected_page = option_menu(
        "Navigation",
        ["Home", "Menu", "Operations", "Contact", "Settings"],
        icons=["house", "clipboard", "people", "telephone", "gear"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#E0E0E0"},
            "icon": {"color": "white", "font-size": "25px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "0px",
                "color": "#212121",
            },
            "nav-link-selected": {"background-color": "#4CAF50"},
        },
    )

# Define the employees list with correct paths
employees = [
    {"name": "Alice", "role": "Manager", "image": "images/manager1.png"},
    {"name": "Jean", "role": "Chef", "image": "images/chef.png"},
    {"name": "Luc", "role": "Waiter", "image": "images/waiter.png"},
    {"name": "David", "role": "Assistant Manager", "image": "images/manager2.png"}
]

# Home Page
if selected_page == "Home":
    st.title("Roster Management")

    # KPIs
    # Center the KPIs in a horizontal line using columns
    kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

    with kpi_col1:
        st.markdown(
            """
            <div style="background-color:rgba(255, 255, 255, 0.8);border-radius:15px;padding:20px;margin:10px;box-shadow:2px 2px 15px rgba(0, 0, 0, 0.1);text-align:center;">
                <div style="font-size:40px;color:#212121;">👥</div>
                <div style="color:#212121;font-weight:bold;font-size:20px;">Total Employees</div>
                <div style="font-size:30px;font-weight:bold;margin:10px 0;">6</div>
                <div style="font-size:16px;font-weight:bold;color:#4CAF50;"> _ </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi_col2:
        st.markdown(
            """
            <div style="background-color:rgba(255, 255, 255, 0.8);border-radius:15px;padding:20px;margin:10px;box-shadow:2px 2px 15px rgba(0, 0, 0, 0.1);text-align:center;">
                <div style="font-size:40px;color:#212121;">✅</div>
                <div style="color:#212121;font-weight:bold;font-size:20px;">Shifts Covered</div>
                <div style="font-size:30px;font-weight:bold;margin:10px 0;">95%</div>
                <div style="font-size:16px;font-weight:bold;color:#4CAF50;">+5%</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with kpi_col3:
        st.markdown(
            """
            <div style="background-color:rgba(255, 255, 255, 0.8);border-radius:15px;padding:20px;margin:10px;box-shadow:2px 2px 15px rgba(0, 0, 0, 0.1);text-align:center;">
                <div style="font-size:40px;color:#212121;">⏰</div>
                <div style="color:#212121;font-weight:bold;font-size:20px;">Overtime Hours</div>
                <div style="font-size:30px;font-weight:bold;margin:10px 0;">120 hrs</div>
                <div style="font-size:16px;font-weight:bold;color:#F44336;">-10 hrs</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("---")
    
    # Roster Management Section
    st.subheader("Current Roster")
    
    data = {
        'Employee': ['Alice', 'Jean', 'Luc', 'David'],
        'Monday': ['9-5', '10-6', '12-8', '9-5'],
        'Tuesday': ['9-5', 'Off', '12-8', '10-6'],
        'Wednesday': ['9-5', '10-6', 'Off', '12-8'],
        'Thursday': ['9-5', '10-6', '12-8', 'Off'],
        'Friday': ['9-5', '10-6', '12-8', '9-5'],
        'Saturday': ['Off', '10-6', '12-8', 'Off'],
        'Sunday': ['Off', 'Off', 'Off', '10-6']
    }
    
    df = pd.DataFrame(data)
    st.dataframe(df)

    st.write("---")
    
    # Profile Carousel
    st.subheader("Employee Profiles")
    current_profile = st.selectbox("", [emp["name"] for emp in employees])
    
    selected_emp = next((emp for emp in employees if emp["name"] == current_profile), None)
    
    if selected_emp:
        import base64

        def get_base64_image(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")

        # Example usage
        selected_emp_image_base64 = get_base64_image(selected_emp['image'])

        # Create two columns: one for the image and one for the parameters
        col1, col2 = st.columns([1, 2])

        with col1:

            st.markdown(f"""
                <img src="data:image/png;base64,{selected_emp_image_base64}" class="profile-image">
            """, unsafe_allow_html=True)
            st.markdown(f"""
                <div class="profile-details">
                    <h3>{selected_emp['name']}</h3>
                    <p>{selected_emp['role']}</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:

            
            # Add the sliders and buttons for profile parameters
            max_hours = st.slider(f"{selected_emp['name']}'s Maximum Working Hours per Week", min_value=20, max_value=60, value=40)
            min_breaks = st.slider(f"{selected_emp['name']}'s Minimum Breaks per Shift", min_value=0, max_value=5, value=1)
            notify = st.checkbox(f"Notify {selected_emp['name']} of schedule changes")
            submit = st.button(f"Save {selected_emp['name']}'s Parameters")


    st.write('')
    st.write("---")

    # Updated events with events for the last days of July and emojis
    events = [
        # July events
        {"title": "🌟 Alice's Shift", "start": "2024-07-29 09:00:00", "end": "2024-07-29 17:00:00"},  # Monday
        {"title": "🍳 Jean's Shift", "start": "2024-07-29 10:00:00", "end": "2024-07-29 18:00:00"},    # Monday
        {"title": "🍽️ Luc's Shift", "start": "2024-07-30 12:00:00", "end": "2024-07-30 20:00:00"}, # Tuesday
        {"title": "📝 David's Review", "start": "2024-07-30 09:00:00", "end": "2024-07-30 11:00:00"},   # Tuesday
        {"title": "🌟 Alice's Extra Shift", "start": "2024-07-31 09:00:00", "end": "2024-07-31 17:00:00"}, # Wednesday
        {"title": "🍳 Jean's Extra Shift", "start": "2024-07-31 10:00:00", "end": "2024-07-31 18:00:00"},   # Wednesday
        {"title": "🍽️ Luc's Extra Shift", "start": "2024-07-31 12:00:00", "end": "2024-07-31 20:00:00"}, # Wednesday
        
        # August events
        {"title": "🌟 Alice's Shift", "start": "2024-08-01 09:00:00", "end": "2024-08-01 17:00:00"},  # Thursday
        {"title": "🍳 Jean's Shift", "start": "2024-08-02 10:00:00", "end": "2024-08-02 18:00:00"},    # Friday
        {"title": "🍽️ Luc's Shift", "start": "2024-08-03 12:00:00", "end": "2024-08-03 20:00:00"}, # Saturday
        {"title": "📝 David's Shift", "start": "2024-08-04 09:00:00", "end": "2024-08-04 17:00:00"},   # Sunday
        {"title": "🌟 Alice's Meeting", "start": "2024-08-05 14:00:00", "end": "2024-08-05 15:00:00"}, # Monday
        {"title": "🍳 Jean's Training", "start": "2024-08-06 09:00:00", "end": "2024-08-06 11:00:00"},  # Tuesday
        {"title": "📦 Luc's Inventory", "start": "2024-08-07 10:00:00", "end": "2024-08-07 12:00:00"}, # Wednesday
        {"title": "📝 David's Review", "start": "2024-08-08 13:00:00", "end": "2024-08-08 14:00:00"},  # Thursday
        {"title": "📋 Team Briefing", "start": "2024-08-09 10:00:00", "end": "2024-08-09 11:00:00"},   # Friday
        {"title": "🍳 Jean's Shift", "start": "2024-08-10 10:00:00", "end": "2024-08-10 18:00:00"},     # Saturday
        {"title": "🍽️ Luc's Shift", "start": "2024-08-11 12:00:00", "end": "2024-08-11 20:00:00"}, # Sunday
        {"title": "📝 David's Shift", "start": "2024-08-12 09:00:00", "end": "2024-08-12 17:00:00"},   # Monday
        {"title": "🌟 Alice's Shift", "start": "2024-08-13 09:00:00", "end": "2024-08-13 17:00:00"},   # Tuesday
        
        # Additional shifts to meet the requirement
        {"title": "🍳 Jean's Extra Shift", "start": "2024-08-02 12:00:00", "end": "2024-08-02 20:00:00"}, # Friday
        {"title": "🍽️ Luc's Extra Shift", "start": "2024-08-02 14:00:00", "end": "2024-08-02 22:00:00"}, # Friday
        
        {"title": "📝 David's Extra Shift", "start": "2024-08-03 09:00:00", "end": "2024-08-03 17:00:00"}, # Saturday
        {"title": "🌟 Alice's Extra Shift", "start": "2024-08-03 08:00:00", "end": "2024-08-03 16:00:00"}, # Saturday
        
        {"title": "🍳 Jean's Extra Shift", "start": "2024-08-04 10:00:00", "end": "2024-08-04 18:00:00"}, # Sunday
        {"title": "🍽️ Luc's Extra Shift", "start": "2024-08-04 12:00:00", "end": "2024-08-04 20:00:00"}, # Sunday
        
        {"title": "🌟 Alice's Extra Shift", "start": "2024-08-06 09:00:00", "end": "2024-08-06 17:00:00"}, # Tuesday
        {"title": "📝 David's Extra Shift", "start": "2024-08-06 14:00:00", "end": "2024-08-06 22:00:00"}, # Tuesday
        
        {"title": "🍳 Jean's Extra Shift", "start": "2024-08-07 11:00:00", "end": "2024-08-07 19:00:00"}, # Wednesday
        {"title": "🍽️ Luc's Extra Shift", "start": "2024-08-07 15:00:00", "end": "2024-08-07 23:00:00"}, # Wednesday
        
        {"title": "🌟 Alice's Extra Shift", "start": "2024-08-08 09:00:00", "end": "2024-08-08 17:00:00"}, # Thursday
        {"title": "🍳 Jean's Extra Shift", "start": "2024-08-08 12:00:00", "end": "2024-08-08 20:00:00"}, # Thursday
    ]

    calendar(events)



# Operations Page
if selected_page == "Operations":
    st.title("Operations 👥")
    
    for emp in employees:
        st.subheader(emp["name"])
        st.markdown(f'<img src="{emp["image"]}" class="profile-image">', unsafe_allow_html=True)
        st.write(f"Role: {emp['role']}")
        st.write("---")

# Contact Page
if selected_page == "Contact":
    st.title("Contact 📞")
    st.write("Content to be added")
    # Example content
    st.write("Add your contact information here.")

# Settings Page
if selected_page == "Settings":
    st.title("Settings ⚙️")
    st.write("Content to be added")
    # Example content
    st.write("Add your settings here.")

st.markdown("<div style='text-align: center; margin-top: 50px;'>© 2024 Made by Yoluko Solutions - Alexandre Kocev</div>", unsafe_allow_html=True)
