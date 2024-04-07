import streamlit as st
import pandas as pd
import os

page_title = "FaceOlit"
page_icon = "WqegGTeNSs6upA9AgdhrQg.png"
logo_path = "WqegGTeNSs6upA9AgdhrQg.png"  # Path to your app's logo

# Function to load attendance data from CSV file
def load_attendance_data(selected_date):
    filename = f"{selected_date}_attendance.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        return df
    else:
        return None

# Function to render the home page
def home():
    st.title("Welcome to FACEOLIT Smart Attendance Viewer")
    st.image("ClI7A1lWSLen7rFuVQBdCQ.jpg", width=500)
    st.write("This is a simple tool to view attendance records.")

    # Add bold text about the web app
    st.markdown("**FaceOlit** is a smart attendance management system utilizing facial recognition technology to track and manage attendance records efficiently.")

    st.write("Please click the button below to view attendance.")
    # Button to navigate to attendance viewing page
    if st.button("View Attendance"):
        attendance_view()


# Function to render the attendance viewing page
def attendance_view():
    st.title("Attendance Viewer")

    # Create a list of available dates from the filenames
    filenames = [filename for filename in os.listdir() if filename.endswith("_attendance.csv")]
    dates_list = [filename.split('_')[0] for filename in filenames]

    # Select date from the list
    selected_date = st.selectbox("Select Date", dates_list)

    # Load attendance data based on selected date
    df = load_attendance_data(selected_date)

    if df is not None:
        # Display attendance data in a table with better formatting
        st.table(df.style.set_properties(align='center'))
    else:
        st.write(f"No attendance data available for {selected_date}")

# Main function to run the Streamlit app
def main():
    st.set_page_config(page_title=page_title, page_icon=page_icon)
    
    st.sidebar.image(logo_path, use_column_width=True)  # Display app logo
    
    st.sidebar.markdown("---")
    
    page = st.sidebar.selectbox("Select Page", ["Home", "Attendance Viewer"])
    

    if page == "Home":
        home()
    elif page == "Attendance Viewer":
        attendance_view()

if __name__ == "__main__":
    main()
