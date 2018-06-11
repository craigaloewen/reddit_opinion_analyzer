# Introduction

This repo contains the code used to analyze Reddit comments about the Github acquisition by Microsoft. You can view the full article here [ADD LINK].

# How to use this repo

First create a config.py file. It should contain the following information with the following variable names:

* username = Your Reddit Username
* password = Your Reddit password
* client_id = Reddit Client ID
* client_secret = Reddit Client Secret
* plotly_username = Plotly username
* plotly_api_key = Plotly api key

Then run the scripts in this order, I'll also provide a quick explanation of what each does.

* gatherdata.py : Uses PRAW to gather reddit comments that talk about Microsoft and Github from your subreddit of choice
* analyzecomments.py : Runs all the saved comments through Google Cloud's Natural Language Processor
* plotdata.py : Plots all the data in nice looking graphs using Plot.ly