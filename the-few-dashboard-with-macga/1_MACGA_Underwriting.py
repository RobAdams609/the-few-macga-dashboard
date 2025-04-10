
import streamlit as st

st.set_page_config(page_title="MACGA Underwriting Tool", layout="centered")

st.title("🦅 America's Insurance | MACGA Underwriting Tool")
st.caption("Tariff-Free Insurance Decisions • Red, White & Blue Edition")

st.markdown("---")

# User input section
age = st.number_input("Applicant Age", min_value=18, max_value=100)
height = st.number_input("Height (in inches)", min_value=48, max_value=84)
weight = st.number_input("Weight (lbs)", min_value=70, max_value=400)
conditions = st.text_area("Medical Conditions (separate by commas)")
meds = st.text_area("Current Medications")
surgeries = st.text_area("Past Surgeries (optional)")
tobacco = st.radio("Tobacco Use in Last 5 Years?", ["No", "Yes"])
notes = st.text_area("Additional Notes / Risk Factors", "")

if st.button("🔥 FIRE IT OFF!"):
    decision = "STD"
    if "depression" in conditions.lower() and age < 25:
        decision = "IC"
    if "bipolar" in conditions.lower() or "cancer" in conditions.lower():
        decision = "D"
    if "pending" in notes.lower() or "recent hospital" in notes.lower():
        decision = "PP"

    st.markdown("---")
    st.subheader(f"🧾 Underwriting Decision: **{decision}**")

    if decision == "STD":
        st.success("✅ MACGA! Make America's Health Insurance Great Again — one clean case at a time.")
    elif decision == "IC":
        st.warning("⚠️ Individual Consideration — This one's going up the chain of command.")
    elif decision == "PP":
        st.info("🕒 Postpone — Temp grounded. Recheck when stable.")
    elif decision == "D":
        st.error("⛔ Declined — Risk too spicy for freedom. No-go for launch.")
