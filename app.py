#streamlit
import streamlit as st

st.set_page_config(page_title= "Growth Mindset Project", project_icon="➶")
st.title("Growth Mindset Challenge: Web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Embrace Challenges, learn from mistakes,and unlock your full potential.This AI-powered app helps you build a growth mindset with reflection,challenges,and achievements!.➶")

#Quote
st.header("Growth Mindset Quote")
st.write("SUCCESS IS A JOURNEY,NOT A DESTINATION.THE DOING IS OFTEN MORE IMPORTANT THAN THE OUTCOME.-ARTHUR ASHE")
st.header("What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

#condition
if user_input:
    st.success(f" You're facing:{user_input}.Keep going towards your goal!")
else:
    st.warning("Tell us about your difficulties to get started!")  

#reflecting
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your reflection here:")

if reflection:
    st.success(f"Great insight!Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience will help you grow.Share your difficulties.")   

#achievements
st.header("Celebrate your Wins")
achievements = st.text_input("Share something that you have recently accomplished.")

if achievements:
    st.text_success(f"Bravo! You have achieved: {achievements}")
else:
    st.info("Failure is not the opposite of success,it's part of success.")

#footer
st.write("- - -")
st.write("The harder you work for something.The greater you will feel when you achieve it.")
st.write("Created by Sabahat Aslam")





