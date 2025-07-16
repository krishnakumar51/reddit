import praw
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT
def scrape_user_data(username):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )
    user = reddit.redditor(username)
    posts = []
    comments = []
    for submission in user.submissions.new(limit=None):
        posts.append({"text": submission.title + " " + submission.selftext, "url": submission.url})
    for comment in user.comments.new(limit=None):
        comments.append({"text": comment.body, "url": f"https://www.reddit.com{comment.permalink}"})
    print(f"Fetched {len(posts)} posts and {len(comments)} comments for {username}")
    for post in posts:
        print(f"Post: {post['text']} URL: {post['url']}")
    for comment in comments:
        print(f"Comment: {comment['text']} URL: {comment['url']}")
    return posts, comments