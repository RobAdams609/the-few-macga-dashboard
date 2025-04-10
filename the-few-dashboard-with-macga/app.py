import random

std_messages = [
    "✅ MACGA! Make America's Health Insurance Great Again — one clean case at a time.",
    "🦅 Approved faster than a bald eagle clears TSA. Welcome to Tariff-Free coverage.",
    "🎆 Risk? Low. Freedom? High. You've been liberty-approved.",
    "🚀 Cleared for takeoff — this app’s more American than apple pie."
]

ic_messages = [
    "⚠️ This one’s heading up the chain of command. Barb in underwriting’s on it.",
    "📡 Liberty Line 1: requesting second review. It’s not a no, it’s a stand-by.",
    "🤔 This one needs a closer look. Let the freedom-fueled reviewers decide.",
    "🧠 Uncle Sam’s underwriters are thinking it over — stay tuned."
]

pp_messages = [
    "🕒 Temporarily grounded. Even Lincoln had to wait for reinforcements.",
    "🔁 Postponed — not denied. Recheck when the storm clears.",
    "🧯 Hold up, patriot — this one needs a little more time in the freedom fryer.",
    "🚧 Liberty delay — check back after stabilization."
]

d_messages = [
    "⛔ Declined harder than British tea in Boston Harbor.",
    "🚫 Too spicy for freedom. This one’s a no-go, champ.",
    "💥 Declined. Not even an eagle endorsement could save it.",
    "🔒 Risk denied. Tariffs we can handle — this risk? Nope."
]

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
        st.success(random.choice(std_messages))
    elif decision == "IC":
        st.warning(random.choice(ic_messages))
    elif decision == "PP":
        st.info(random.choice(pp_messages))
    elif decision == "D":
        st.error(random.choice(d_messages))
