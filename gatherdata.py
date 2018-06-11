import praw
from praw.models import MoreComments

import pickle

import datetime

import config

# Courtesy of reddit user /u/programmeroftheday
def get_date(submission):
	time = submission.created
	return datetime.datetime.fromtimestamp(time)

def store_comment(comment):
    with open('./comment-data/' + comment.subreddit.display_name  + '/' + comment.id + '.pkl', 'wb') as output:
        pickle.dump(comment, output, pickle.HIGHEST_PROTOCOL)
 
# Initialize PRAW with a custom User-Agent
 
reddit = praw.Reddit(client_id= config.client_id,
                     client_secret= config.client_secret,
                     password= config.password,
                     user_agent='testscript by /u/msftsummerintern',
                     username= config.username)

print("Logged in")

acq_date = datetime.datetime.strptime('03062018',"%d%m%Y") 

comments_analyzed_counter = 0

valid_comments_counter = 0

subreddit_name = 'programmerhumor'

for submission in reddit.subreddit(subreddit_name).new(limit=None):
    print(submission.title + " | " + str(submission.num_comments))
    # Only look for submissions up to the acquisition date
    if (get_date(submission) < acq_date):
        break

    submission_text = submission.title.lower()

    if submission_text.find("microsoft") != -1 and submission_text.find("github") != -1:
        all_comments_valid = True
    else:
        all_comments_valid = False

    # Analyze all comments of each submission
    submission.comments.replace_more(limit=None)
    for comment in submission.comments.list():
        body_text = comment.body.lower()

        comment_is_valid = False

        if all_comments_valid:
            comment_is_valid = True
        else:
            if body_text.find("microsoft") != -1 and body_text.find("github") != -1:
                comment_is_valid = True

        if comment_is_valid:
            store_comment(comment)
            valid_comments_counter = valid_comments_counter + 1

        comments_analyzed_counter = comments_analyzed_counter + 1

    print("Analyzed: " + str(comments_analyzed_counter) + " comments so far, " + str(valid_comments_counter) + " are valid")

print("Total Analyzed: " + str(comments_analyzed_counter) + " comments")