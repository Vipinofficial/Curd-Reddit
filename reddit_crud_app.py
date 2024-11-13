import praw
import streamlit as st

# Reddit API credentials input
st.title("Reddit CRUD App - Enter Reddit Credentials")

REDDIT_CLIENT_ID = st.text_input("Client ID")
REDDIT_CLIENT_SECRET = st.text_input("Client Secret", type="password")
REDDIT_USERNAME = st.text_input("Username")
REDDIT_PASSWORD = st.text_input("Password", type="password")
REDDIT_USER_AGENT = st.text_input("User Agent", "my_reddit_app")

# Display debug messages
st.write("Loading Reddit Client...")

try:
    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        username=REDDIT_USERNAME,
        password=REDDIT_PASSWORD,
        user_agent=REDDIT_USER_AGENT,
    )
    st.success("Reddit Client Loaded Successfully!")
except Exception as e:
    st.error("Failed to load Reddit Client")
    st.write(str(e))

# Application UI
st.title("Reddit CRUD Operations")

# 1. Create a Post
st.header("Create a Post")
subreddit_name = st.text_input("Subreddit", "test")  # Change default to your desired subreddit
post_title = st.text_input("Title")
post_content = st.text_area("Content")
if st.button("Create Post"):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        submission = subreddit.submit(title=post_title, selftext=post_content)
        st.success(f"Post created with ID: {submission.id}")
    except Exception as e:
        st.error("Failed to create post")
        st.write(str(e))

# Store the post ID for update and delete operations
post_id = st.text_input("Enter Post ID for Update/Delete", "")

# 2. Read a Post
st.header("Read a Post")
if st.button("Read Post"):
    try:
        if post_id:
            submission = reddit.submission(id=post_id)
            st.write(f"*Title:* {submission.title}")
            st.write(f"*Content:* {submission.selftext}")
        else:
            st.error("Please enter a Post ID.")
    except Exception as e:
        st.error("Failed to read post")
        st.write(str(e))

# 3. Update a Post
st.header("Update a Post")
new_content = st.text_area("New Content for Update")
if st.button("Update Post"):
    try:
        if post_id:
            submission = reddit.submission(id=post_id)
            submission.edit(new_content)
            st.success("Post updated successfully!")
        else:
            st.error("Please enter a Post ID.")
    except Exception as e:
        st.error("Failed to update post")
        st.write(str(e))

# 4. Delete a Post
st.header("Delete a Post")
if st.button("Delete Post"):
    try:
        if post_id:
            submission = reddit.submission(id=post_id)
            submission.delete()
            st.success("Post deleted successfully!")
        else:
            st.error("Please enter a Post ID.")
    except Exception as e:
        st.error("Failed to delete post")
        st.write(str(e))
