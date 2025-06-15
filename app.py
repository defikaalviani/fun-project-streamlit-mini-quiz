import streamlit as st

# --- Page setup ---
st.set_page_config(page_title="Car Finance Readiness Quiz", page_icon="🚗")

# --- App Logo and Title ---
st.image("https://ddc1.s3.amazonaws.com/NjS7CblGrGnT4miQBA%3D%3D/CDy2BvBgoiXPo024/Vm3pWw%3D%3D/Ejy0F-w%3D/header.jpg", width=1500)
st.title("🚗 Are You Finance-Ready to Buy a Car?")
st.write("Let's find out how ready you are to finance your dream car!")

# --- Initialize session state ---
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = False
if "score" not in st.session_state:
    st.session_state.score = 0

# --- Quiz Questions ---
st.header("📋 Mini Quiz")

# Score variable
score = 0

name = st.text_input("What is your name?")

# Q1
income = st.selectbox("1. What is your monthly income?", 
                      ["< IDR 3 million", "IDR 3–7 million", "IDR 7–15 million", "> IDR 15 million"])
if income == "> IDR 15 million":
    score += 25
elif income == "IDR 7–15 million":
    score += 20
elif income == "IDR 3–7 million":
    score += 10
else:
    score += 5

# Q2
dp = st.selectbox("2. How much down payment are you ready to make?", 
                  ["<10%", "10–20%", "20–30%", ">30%"])
if dp == ">30%":
    score += 25
elif dp == "20–30%":
    score += 20
elif dp == "10–20%":
    score += 10
else:
    score += 5

# Q3
credit = st.radio("3. Do you know your credit score?", ["Yes", "No"])
if credit == "Yes":
    score += 15
else:
    score += 5

# Q4
loans = st.radio("4. Do you currently have any active loans?", ["No", "Yes, small", "Yes, many"])
if loans == "No":
    score += 20
elif loans == "Yes, small":
    score += 10
else:
    score += 5

# Q5
term = st.radio("5. What loan term would you prefer?", ["<1 year", "1–3 years", "3–5 years", ">5 years"])
if term in ["1–3 years", "3–5 years"]:
    score += 15
else:
    score += 5

if st.button("✅ Submit Quiz"):
    st.session_state.quiz_submitted = True
    st.session_state.score = score
    st.success("Your answers have been submitted. Now you can check your score!")

# --- See the Score ---
if st.session_state.quiz_submitted:
    if st.button("🔍 See the Score"):
        st.subheader("📊 Your Finance Readiness Score")
        st.progress(st.session_state.score)

        if st.session_state.score >= 80:
            st.success(f"🎉 Congratulation, {name}!You're **finance-ready** to buy a car! 🚗💨")
        elif st.session_state.score >= 50:
            st.info(f"Hi, {name}! You're almost ready. Let's review some things.")
        else:
            st.warning(f"Hi, {name}! You're not quite ready yet. Learn more before applying.")

# --- Email Submission Section ---
st.markdown("---")
st.write("📩 Want help finding the best financing options?")

if "email_submitted" not in st.session_state:
    st.session_state.email_submitted = False

with st.form("email_form"):
    email = st.text_input("Leave your email here (optional):")
    submitted = st.form_submit_button("📨 Submit Email")
    if submitted:
        if email.strip() != "":
            st.session_state.email_submitted = True
            st.session_state.entered_email = email.strip()
        else:
            st.warning("Please enter a valid email before submitting.")

# Show success message after form is submitted
if st.session_state.email_submitted:
    st.success(f"Thanks! Our advisor will reach out to: {st.session_state.entered_email}")


# --- Footer ---
st.markdown("---")
st.caption("🚘 **FinBuddy** Your Finance Advisor 🚘")
st.caption("by Defika Alviani")
