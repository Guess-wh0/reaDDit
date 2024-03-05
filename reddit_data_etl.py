import praw
import pandas as pd
from datetime import datetime
from google.cloud import storage
import os
from dotenv import load_dotenv

# loading secrets from .env
load_dotenv()

def reddit_etl():
  print("*************************STARTED DATA FETCH********************")

  reddit = praw.Reddit(
    client_id = os.getenv("CLIENT_ID"),
    client_secret = os.getenv("CLIENT_SECRET"),
    user_agent="reddit client to get new 50 posts of popular"
    )

  submissions = reddit.subreddit("popular").hot(limit=100)
  reddit_posts = []

  i = 0
  for submission in submissions:
    print("*************************parsing post %s********************" % i)
    i +=1

    post_details = {
      'post_id': submission.id,
      'author': submission.author.name,
      'author_id': submission.author.id,
      'title': submission.title,
      'comments_count': submission.num_comments,
      'locked': submission.locked,
      'score': submission.score,
      'upvote_ratio': submission.upvote_ratio,
      'created_at': datetime.utcfromtimestamp(submission.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    }
    reddit_posts.append(post_details)

  df = pd.DataFrame(reddit_posts)
  client = storage.Client.from_service_account_json(json_credentials_path=os.getenv('GCP_KEY_PATH'))
  bucket = client.get_bucket(os.getenv("BUCKET_NAME"))
      
  bucket.blob(datetime.now().strftime("%Y%m%d%H%M%S") + 'fetched_reddit_data.csv').upload_from_string(df.to_csv(), 'text/csv')

  print("*************************ENDED DATA FETCH********************")
