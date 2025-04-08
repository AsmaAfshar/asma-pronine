#Project 9 Build a Python Website in 15 Minutes With Streamlit

import streamlit as st
import pandas as pd
import random

# Set page configuration
st.set_page_config(page_title="Student Data Generator", layout="wide")
st.title("Student CSV File Generator")

# List of names
names = ["Ali","Ahmed","Laiba","Kiran","Humaira","Saba","Saham","Immad","Hammad","Jaweria","Shumaila","Faraz","Waqar","Asad","Tazeen","Iffat","Afifa","Asfia","Ayaz","Khizar"]

# Create a list to store student dictionaries
students = []  
# Generate student data
for i in range(1, 21):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A","B","C","D","E","F"]),
        "Marks": random.randint(40,100),
    }
    students.append(student)

# Create DataFrame
df = pd.DataFrame(students)

# Display student data
st.subheader("Generated Students Data")
st.dataframe(df)

# Create download button for CSV
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("Download CSV File", csv_file, "students.csv", "text/csv")
st.success("Students Record Generated Successfully!")
