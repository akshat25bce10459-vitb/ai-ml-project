import streamlit as st
from planner import create_schedule
import matplotlib.pyplot as plt

st.title(" Smart Study Planner (AI Based)")
subjects = []
n = st.number_input("Number of subjects", 1, 5)

for i in range(n):
    st.subheader(f"Subject {i+1}")

    name = st.text_input(f"Name {i+1}")
    difficulty = st.slider(f"Difficulty {i+1}", 1, 5)
    days = st.number_input(f"Days left {i+1}", 1, 30)
    subjects.append((name, difficulty, days))

if st.button("Generate Plan"):
    schedule = create_schedule(subjects)

    if len(schedule) == 0:
        st.warning("Enter at least one subject")
    else:
        st.subheader(" Study Plan")

        for s in schedule:
            st.write(f" {s[0]} → Priority: {round(s[3],2)}")
        names = [s[0] for s in schedule]
        priorities = [s[3] for s in schedule]
        plt.figure()
        plt.bar(names, priorities)
        plt.xlabel("Subjects")
        plt.ylabel("Priority")
        st.pyplot(plt)