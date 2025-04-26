import streamlit as st
import pandas as pd
import pydeck as pdk
import os

# File paths
REPORTS_FILE = "reports.csv"
INITIATIVES_FILE = "initiatives.csv"
POINTS_FILE = "points.csv"

# Initialize files if they don't exist
if not os.path.exists(REPORTS_FILE):
    pd.DataFrame(columns=["description", "latitude", "longitude", "username"]).to_csv(REPORTS_FILE, index=False)

if not os.path.exists(INITIATIVES_FILE):
    pd.DataFrame(columns=["name", "description", "contact"]).to_csv(INITIATIVES_FILE, index=False)

if not os.path.exists(POINTS_FILE):
    pd.DataFrame(columns=["username", "lifepoints"]).to_csv(POINTS_FILE, index=False)

# List of cities (USA, India, UAE)
cities = [
    ("New York, USA", 40.7128, -74.0060), ("Los Angeles, USA", 34.0522, -118.2437), ("Chicago, USA", 41.8781, -87.6298),
    ("Houston, USA", 29.7604, -95.3698), ("Phoenix, USA", 33.4484, -112.0740), ("Philadelphia, USA", 39.9526, -75.1652),
    ("San Antonio, USA", 29.4241, -98.4936), ("San Diego, USA", 32.7157, -117.1611), ("Dallas, USA", 32.7767, -96.7970),
    ("San Jose, USA", 37.3382, -121.8863), ("Austin, USA", 30.2672, -97.7431), ("Jacksonville, USA", 30.3322, -81.6557),
    ("Fort Worth, USA", 32.7555, -97.3308), ("Columbus, USA", 39.9612, -82.9988), ("Charlotte, USA", 35.2271, -80.8431),
    ("San Francisco, USA", 37.7749, -122.4194), ("Indianapolis, USA", 39.7684, -86.1581), ("Seattle, USA", 47.6062, -122.3321),
    ("Denver, USA", 39.7392, -104.9903), ("Washington, USA", 38.9072, -77.0369),

    ("Mumbai, India", 19.0760, 72.8777), ("Delhi, India", 28.6139, 77.2090), ("Bangalore, India", 12.9716, 77.5946),
    ("Hyderabad, India", 17.3850, 78.4867), ("Ahmedabad, India", 23.0225, 72.5714), ("Chennai, India", 13.0827, 80.2707),
    ("Kolkata, India", 22.5726, 88.3639), ("Pune, India", 18.5204, 73.8567), ("Jaipur, India", 26.9124, 75.7873),
    ("Lucknow, India", 26.8467, 80.9462), ("Kanpur, India", 26.4499, 80.3319), ("Nagpur, India", 21.1458, 79.0882),
    ("Indore, India", 22.7196, 75.8577), ("Bhopal, India", 23.2599, 77.4126), ("Patna, India", 25.5941, 85.1376),
    ("Ludhiana, India", 30.9000, 75.8573), ("Agra, India", 27.1767, 78.0081), ("Nashik, India", 19.9975, 73.7898),
    ("Vadodara, India", 22.3072, 73.1812), ("Rajkot, India", 22.3039, 70.8022),

    ("Dubai, UAE", 25.276987, 55.296249), ("Abu Dhabi, UAE", 24.4539, 54.3773), ("Sharjah, UAE", 25.3463, 55.4209),
    ("Al Ain, UAE", 24.1917, 55.7606), ("Ajman, UAE", 25.4052, 55.5136), ("Ras Al Khaimah, UAE", 25.8007, 55.9762),
    ("Fujairah, UAE", 25.1288, 56.3265), ("Umm Al Quwain, UAE", 25.5647, 55.5552), ("Khor Fakkan, UAE", 25.3313, 56.3565),
    ("Dibba, UAE", 25.6180, 56.2724), ("Kalba, UAE", 25.0951, 56.3623), ("Hatta, UAE", 24.8223, 56.1040),
    ("Madinat Zayed, UAE", 23.5843, 53.7084), ("Ruwais, UAE", 24.1103, 52.7300), ("Liwa Oasis, UAE", 23.1300, 53.7700),
    ("Jebel Ali, UAE", 24.9876, 55.0602), ("Al Dhaid, UAE", 25.2881, 55.8810), ("Ghayathi, UAE", 23.8859, 52.7513),
    ("Mirfa, UAE", 24.1063, 53.4842), ("Dhaid, UAE", 25.2881, 55.8810)
]

# Page config
st.set_page_config(page_title="EarthAid", layout="wide")

# Home with Tabs
st.title("🌍 EarthAid")
tabs = st.tabs(["Home", "Report Environment", "Live Earth Map", "Initiatives", "Profile", "Leaderboard"])

# Home Page
with tabs[0]:
    st.header("🏠 Home")
    st.markdown("**“We cut trees, build paper from it, and then write save trees on it — isn’t it ironic?”**")
    st.markdown("— Atharv Johari, Creator of EarthAid")
    st.markdown("**“EarthAid is a powerful, student-driven platform that turns everyday concern for the planet into real-world action.”**")
    st.markdown("From reporting environmental issues to joining eco-initiatives, EarthAid empowers users to actively protect our world — while earning LifePoints and recognition for their contributions.")
    
    st.markdown("")
    st.header("🌱 About EarthAid")
    st.markdown("EarthAid is more than just an app — it’s a youth-led environmental movement. It allows users to:")
    st.markdown(" * Report issues in their surroundings that harm the environment.")
    st.markdown(" * Share and join initiatives for clean-ups, green drives, and sustainability efforts.")
    st.markdown(" * View a global impact map showing real-time eco-activities.")
    st.markdown(" * Track LifePoints, climb the Leaderboard, and earn a Certificate of Impact for their contributions.")
    
    st.markdown("")
    st.header("👨‍💻 About the Creator")
    st.markdown(" Atharv Johari, the 12-year-old visionary behind EarthAid, is no ordinary student.")
    st.markdown(" He’s a budding innovator, environmentalist, and tech enthusiast whose dedication to the planet is already making waves. With a sharp mind and a big heart, Atharv designed EarthAid entirely on his own — coding the app, planning its structure, and adding unique features like LifePoints, initiative sharing, and real-time environmental reporting.")
    st.markdown(" Despite his age, Atharv has demonstrated remarkable skills in app development and a maturity far beyond his years. His mission? To make the world a better place — one report, one initiative, one small step at a time.")
    st.markdown(" EarthAid is not just a project. It’s Atharv’s vision of a better future, powered by youth, supported by community, and driven by technology.")
    
    st.markdown("")
    st.header("🧠 Features")
    st.markdown("**📝 Report Your Surroundings**")
    st.markdown("Spotted pollution? Overflowing waste? Damaged green spaces? Use EarthAid’s quick reporting tool to document issues and help raise awareness.")
    st.markdown("**📍 Live Earth Map**")
    st.markdown("Track eco-activity from around the world on a vibrant, interactive map showing reports and initiatives submitted by EarthAid users.")
    st.markdown("**🤝 Share & Join Initiatives**")
    st.markdown("Start your own green mission or join one nearby! Connect with like-minded people and take action together — because real change is collaborative.")
    st.markdown("**🏆 LifePoints & Leaderboard**")
    st.markdown("Earn points every time you act. Whether it’s submitting a report or joining an initiative, your efforts are counted. Top users shine on the global Leaderboard.")
    st.markdown("**🎓 Certificate of Impact**")
    st.markdown("Hard work deserves recognition. Active users can receive a Certificate of Impact, officially honoring their contribution to protecting the environment.")

# Report Environment Tab
with tabs[1]:
    st.header("📢 Report Your Environment")
    desc = st.text_area("Describe the issue:")
    city = st.selectbox("Select City", [c[0] for c in cities])
    lat, lon = next(((lat, lon) for c, lat, lon in cities if c == city), (None, None))
    username = st.text_input("Enter your Username")

    if st.button("Submit Report"):
        if desc and lat and lon and username:
            df = pd.read_csv(REPORTS_FILE)
            df = pd.concat([df, pd.DataFrame([{"description": desc, "latitude": lat, "longitude": lon, "username": username}])], ignore_index=True)
            df.to_csv(REPORTS_FILE, index=False)

            points_df = pd.read_csv(POINTS_FILE)
            if username in points_df["username"].values:
                points_df.loc[points_df["username"] == username, "lifepoints"] += 1
            else:
                points_df = pd.concat([points_df, pd.DataFrame([[username, 1]], columns=["username", "lifepoints"])], ignore_index=True)
            points_df.to_csv(POINTS_FILE, index=False)

            st.success("✅ Report submitted and LifePoints updated!")
        else:
            st.warning("Please fill in all fields.")

# Live Earth Map Tab
with tabs[2]:
    st.header("🗺️ Live Earth Map")
    df = pd.read_csv(REPORTS_FILE)
    if not df.empty:
        st.pydeck_chart(pdk.Deck(
            map_style='mapbox://styles/mapbox/light-v9',
            initial_view_state=pdk.ViewState(
                latitude=df["latitude"].mean(),
                longitude=df["longitude"].mean(),
                zoom=2,
                pitch=50
            ),
            layers=[
                pdk.Layer(
                    'ScatterplotLayer',
                    data=df,
                    get_position='[longitude, latitude]',
                    get_color='[200, 30, 0, 160]',
                    get_radius=10000,
                )
            ]
        ))
    else:
        st.info("No reports yet to display on the map.")

# Initiatives Tab
with tabs[3]:
    st.header("🤝 Initiatives")
    tab1, tab2 = st.tabs(["Submit Initiative", "View Initiatives"])

    with tab1:
        name = st.text_input("Initiative Name")
        description = st.text_area("Describe your initiative")
        contact = st.text_input("Your contact info (email or phone)")
        username = st.text_input("Your Username")

        if st.button("Submit Initiative"):
            if name and description and contact and username:
                df = pd.read_csv(INITIATIVES_FILE)
                df = pd.concat([df, pd.DataFrame([{"name": name, "description": description, "contact": contact}])], ignore_index=True)
                df.to_csv(INITIATIVES_FILE, index=False)

                points_df = pd.read_csv(POINTS_FILE)
                if username in points_df["username"].values:
                    points_df.loc[points_df["username"] == username, "lifepoints"] += 1
                else:
                    points_df = pd.concat([points_df, pd.DataFrame([[username, 1]], columns=["username", "lifepoints"])], ignore_index=True)
                points_df.to_csv(POINTS_FILE, index=False)
                st.success("✅ Initiative submitted and LifePoints updated!")
            else:
                st.warning("Please complete all fields.")

    with tab2:
        df = pd.read_csv(INITIATIVES_FILE)
        if not df.empty:
            st.dataframe(df)
        else:
            st.info("No initiatives submitted yet.")

# Profile Tab
with tabs[4]:
    st.header("👤 User Profile")
    username = st.text_input("Enter your Username to check LifePoints")
    if username:
        points_df = pd.read_csv(POINTS_FILE)
        if username in points_df["username"].values:
            points = points_df.loc[points_df["username"] == username, "lifepoints"].values[0]
            st.success(f"{username}, you have {points} LifePoints.")
        else:
            st.warning("Username not found. Try submitting a report or initiative first.")

# Leaderboard Tab
with tabs[5]:
    st.header("🏆 Leaderboard")
    points_df = pd.read_csv(POINTS_FILE)
    if not points_df.empty:
        sorted_df = points_df.sort_values(by="lifepoints", ascending=False).reset_index(drop=True)
        sorted_df["medal"] = ""
        if len(sorted_df) > 0:
            sorted_df.at[0, "medal"] = "🥇"
        if len(sorted_df) > 1:
            sorted_df.at[1, "medal"] = "🥈"
        if len(sorted_df) > 2:
            sorted_df.at[2, "medal"] = "🥉"
        sorted_df["display"] = sorted_df["username"] + " " + sorted_df["medal"] + " - " + sorted_df["lifepoints"].astype(str) + " pts"
        st.write("### Rankings")
        for line in sorted_df["display"]:
            st.write(line)
    else:
        st.info("No users have submitted reports or initiatives yet.")