import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Configure Gemini API


def format_reddit_data(posts, comments):
    """Format Reddit posts and comments into a single string."""
    data = ""
    for post in posts:
        data += f"Post: {post['text']} URL: {post['url']}\n"
    for comment in comments:
        data += f"Comment: {comment['text']} URL: {comment['url']}\n"
    return data

def get_characteristics(posts, comments):

    load_dotenv()
    """Analyze Reddit data with Gemini, including preprocessing."""

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY "))
    reddit_data = format_reddit_data(posts, comments)
    
    # Preprocess: Truncate to 10,000 characters to fit token limit
    reddit_data = reddit_data[:10000]

    # Hot prompt with example
    prompt = f"""
Hey, you’re the ultimate persona generator! Take this Reddit data and build me a detailed user persona similar to the example template. Include:
- Name: A fictional name based on the username.
- Age: Estimated age range.
- Role: Possible occupation or role.
- Location: Inferred location.
- Type: Personality type.
- Motivations: Key drivers.
- Attitude: General outlook.
- Personality: Core traits.
- Goal: Primary objective.
- Frustrations: Main pain points.
- Behaviors & Habits: Daily patterns.
- Quote: A representative quote.

For each field, provide a description and citation to the exact URL where possible. Format it neatly in markdown.

Reddit data:
{reddit_data}
"""

    model = genai.GenerativeModel('gemini-2.0-flash-001')
    response = model.generate_content(prompt)
    
    # For debugging
    print("Gemini response:", response.text)
    
    # Parse response (assuming model follows format; adjust if needed)
    return response.text  # We’ll format this in persona.py
