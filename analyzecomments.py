import pickle
import os
import matplotlib.pyplot as plt
import numpy as np
import datetime
import sentimentAnalyzer

def contains_github_and_microsoft(input_text):
    if input_text.find("microsoft") != -1 and input_text.find("github") != -1:
        return True
    else:
        return False

output_csv = open("cumulative-comment-data.csv","w")

output_csv.write("comment_id,post-date,subreddit,contains_github_and_microsoft,sentiment,magnitude\n")

commentAnalyzer = sentimentAnalyzer.sentimentAnalyzer()

numCommentsAnalyzed = 0

for foldername in os.listdir('./comment-data/'):
    print("Starting folder: {} with total {} comments.".format(foldername,len(os.listdir('./comment-data/' + foldername + '/'))))
    for filename in os.listdir('./comment-data/' + foldername + '/'):
        with open('./comment-data/' + foldername + '/' + filename, 'rb') as input:
            comment = pickle.load(input)

            commentBody = comment.body.lower()

            sentimentResult = commentAnalyzer.analyzeText(commentBody)
            containsGHandMS = contains_github_and_microsoft(commentBody)

            if containsGHandMS:
                containsGHandMSResult = "Y"
            else:
                containsGHandMSResult = "N"

            rowString = str(comment.id) + "," \
                        + str(datetime.datetime.fromtimestamp(comment.created)) + "," \
                        + str(comment.subreddit.display_name) + "," + containsGHandMSResult + "," \
                        + str(sentimentResult[0]) + "," \
                        + str(sentimentResult[1]) + "\n"

            output_csv.write(rowString)

            numCommentsAnalyzed = numCommentsAnalyzed + 1

            if numCommentsAnalyzed % 50 == 0:
                print("Analyzed 50 comments")
