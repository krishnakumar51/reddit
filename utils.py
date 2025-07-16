# utils.py
import re


def validate_reddit_url(url):
    """Validate and extract username from Reddit profile URL."""
    pattern = r"https?://(www\.)?reddit\.com/user/([A-Za-z0-9_-]+)/?"
    match = re.match(pattern, url)
    return match.group(2) if match else None


def clean_text(text):
    """Clean text by removing URLs and special characters."""
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^A-Za-z0-9\s]", "", text)  # Remove special characters
    return text.strip()