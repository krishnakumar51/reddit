import sys
import os
import argparse
from scraper import scrape_user_data
from analyzer import get_characteristics
from persona import generate_persona

def main():
    parser = argparse.ArgumentParser(description="Generate Reddit User Persona")
    parser.add_argument("url", help="Reddit profile URL (e.g., https://www.reddit.com/user/kojied/)")
    args = parser.parse_args()

    # Extract username from URL
    if "/user/" not in args.url or not args.url.startswith("https://www.reddit.com/"):
        print("Invalid Reddit profile URL. Use format: https://www.reddit.com/user/username/")
        sys.exit(1)
    username = args.url.split("/user/")[1].strip("/")

    print(f"Scraping data for user: {username}")
    posts, comments = scrape_user_data(username)

    print("Analyzing data with Gemini...")
    characteristics = get_characteristics(posts, comments)

    print("Generating persona...")
    persona = generate_persona(username, characteristics)

    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = f"output/{username}.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {output_file}")

if __name__ == "__main__":
    main()