import streamlit as st
import pandas as pd

# Load data
weekly_data = pd.read_csv("weekly_submitted.csv")
activity_data = pd.read_csv("agent_activity.csv")
ytd_data = pd.read_csv("ytd_data.csv")

st.set_page_config(page_title="THE FEW Dashboard", layout="wide")
st.title("🔥 THE FEW | Sales Performance Dashboard")

# Weekly Leaderboard
st.subheader("🏆 Weekly Submitted AV Leaderboard")
weekly_data = weekly_data.sort_values(by="Submitted_AV", ascending=False).reset_index(drop=True)
weekly_data["% to Goal ($20K)"] = (weekly_data["Submitted_AV"] / 20000 * 100).round(1)
st.dataframe(weekly_data.style.highlight_max(subset="Submitted_AV", color="lightgreen"), use_container_width=True)

# Race Track View
st.subheader("🏁 Race to $20K - Agent Goal Progress")
st.bar_chart(weekly_data.set_index("Agent")["% to Goal ($20K)"])

# Close Rate and Talk Time
st.subheader("📞 Agent Activity & Close Rate")
st.dataframe(activity_data.sort_values(by="Close_Rate_%", ascending=False).reset_index(drop=True), use_container_width=True)

# YTD Performance
st.subheader("📈 Year-to-Date AV + Taken Rate")
ytd_data["Taken_Rate_%"] = (ytd_data["YTD_Taken_Rate"] * 100).round(1)
st.dataframe(ytd_data[["Agent", "YTD_Issued", "Taken_Rate_%"]].sort_values(by="YTD_Issued", ascending=False), use_container_width=True)

st.caption("Built for THE FEW ⚔️ Few Will Hunt")

