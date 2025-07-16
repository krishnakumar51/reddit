import streamlit as st
import os
from scraper import scrape_user_data
from analyzer import get_characteristics
from persona import generate_persona

# Set Gemini API key from secrets
# os.environ["GOOGLE_API_KEY"] = st.secrets["gemini"]["api_key"]


st.set_page_config(page_title="Reddit Persona Generator", page_icon="🕵️", layout="wide")

st.title("Reddit User Persona Generator")
st.markdown("Enter a Reddit user profile URL to generate a detailed persona based on their posts and comments.")

# Sidebar for info
with st.sidebar:
    st.header("About")
    st.info("This app uses PRAW for Reddit scraping and Gemini for analysis. Configure API keys in .streamlit/secrets.toml.")
    st.markdown("---")
    st.caption("Built with Streamlit")

# Input form
url = st.text_input("Reddit Profile URL", placeholder="https://www.reddit.com/user/username/")

if st.button("Generate Persona", type="primary"):
    if not url:
        st.error("Please enter a valid URL.")
    else:
        try:
            # Extract username
            if "/user/" not in url or not url.startswith("https://www.reddit.com/"):
                st.error("Invalid Reddit profile URL. Use format: https://www.reddit.com/user/username/")
            else:
                username = url.split("/user/")[1].strip("/")
                st.info(f"Scraping data for user: {username}")

                # # Get credentials from secrets
                # client_id = st.secrets["reddit"]["client_id"]
                # client_secret = st.secrets["reddit"]["client_secret"]
                # user_agent = st.secrets["reddit"]["user_agent"]

                posts, comments = scrape_user_data(username)

                st.info("Analyzing data with Gemini...")
                characteristics = get_characteristics(posts, comments)

                st.info("Generating persona...")
                persona = generate_persona(username, characteristics)

                # Display persona
                st.subheader(f"Persona for {username}")
                st.markdown(persona)

                # Save to file
                output_dir = "output"
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                output_file = f"output/{username}.txt"
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(persona)
                st.success(f"Persona saved to {output_file}")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")