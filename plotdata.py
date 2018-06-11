import plotly.plotly as py
import plotly.figure_factory as ff
import plotly.graph_objs as go

import pandas

import plotly

import numpy as np

import config

import datetime

# Plot a distribution of the overall sentiment
def plotSentimentDistributions(dataframe):

    subreddit_name_list = []

    # Get possible values of subreddit names
    for record in dataframe.values:
        if not subreddit_name_list.__contains__(record[2]):
            subreddit_name_list.append(record[2])

    subreddit_sentiment_list = []
    for subreddit_name in subreddit_name_list:
        subreddit_dataframe = dataframe[dataframe['subreddit'] == subreddit_name]
        subreddit_sentiment_distribution_np = np.array(subreddit_dataframe.values \
                                            [:,4].astype(float))
        subreddit_sentiment_list.append(subreddit_sentiment_distribution_np)

    # Create distplot with custom bin_size
    fig = ff.create_distplot(subreddit_sentiment_list, subreddit_name_list, show_rug=False, show_hist=False)

    # Plot!
    py.iplot(fig, filename='Sentiment Distribution Plot by Subreddit')

# Plot a pie chart of generalized sentiments
def plotSentimentPieChart(dataset):
    
    subreddit_name_list = []

    # Get possible values of subreddit names
    for record in dataframe.values:
        if not subreddit_name_list.__contains__(record[2]):
            subreddit_name_list.append(record[2])

    subreddit_sentiment_list = []
    subreddit_magnitude_list = []
    for subreddit_name in subreddit_name_list:
        subreddit_dataframe = dataframe[dataframe['subreddit'] == subreddit_name]
        subreddit_sentiment_distribution_np = np.array(subreddit_dataframe.values \
                                            [:,4].astype(float))
        subreddit_magnitude_distribution_np = np.array(subreddit_dataframe.values \
                                            [:,5].astype(float))
        subreddit_sentiment_list.append(subreddit_sentiment_distribution_np)
        subreddit_magnitude_list.append(subreddit_magnitude_distribution_np)
    
    # Get a list of all sentiments

    pos_count_list = []
    neg_count_list = []
    neutral_count_list = []
    mixed_count_list = []
    for sub_sentiment,sub_magnitude in zip(subreddit_sentiment_list, \
                                                    subreddit_magnitude_list):
        
        number_negative = (sub_sentiment < 0).sum()
        number_positive = (sub_sentiment > 0).sum()

        number_neutral = ((sub_sentiment == 0) & (sub_magnitude == 0)).sum()
        number_mixed = ((sub_sentiment == 0) & (sub_magnitude > 0)).sum()

        pos_count_list.append(number_positive)
        neg_count_list.append(number_negative)
        neutral_count_list.append(number_neutral)
        mixed_count_list.append(number_mixed)
        
    subreddit_name_list.append("All Data")
    pos_count_list.append(sum(pos_count_list))
    neg_count_list.append(sum(neg_count_list))
    neutral_count_list.append(sum(neutral_count_list))
    mixed_count_list.append(sum(mixed_count_list))
    
    pie_labels = ['Positive','Negative','Neutral','Mixed']    

    trace_list = []
    for num_pos,num_neg,num_neu,num_mix,sub_name in zip(pos_count_list,neg_count_list,neutral_count_list,\
                                                mixed_count_list,subreddit_name_list):
        trace = go.Pie(labels=pie_labels,values=[num_pos,num_neg,num_neu,num_mix],name=sub_name)
        trace_list.append(trace)


    button_list = []

    for index, sub_name in enumerate(subreddit_name_list):
        visibility_list = [ x == index for x in range(len(sub_name))]
        # To ensure that 'All Data' doesn't get modified
        if index != (len(subreddit_name_list) -1):
            final_sub_name = '/r/' + sub_name
        else:
            final_sub_name = sub_name
        dict_item = dict(label = final_sub_name,
                        method = 'update',
                        args = [{'visible': visibility_list}])
        button_list.append(dict_item)

    updatemenus = list([
        dict(active=(len(subreddit_name_list)-1),
            buttons=button_list,
            direction = 'down',
            pad = {'r': 10, 't': 10},
            showactive = True,
            x = 0.13,
            xanchor = 'left',
            y = 1.1,
            yanchor = 'top' 
        )
    ])

    annotations = list([
        dict(text='Subreddit filter:', x=0, y=1.07, yref='paper', align='left', showarrow=False)
    ])

    layout = dict(title='Overall Sentiment of Reddit Comments',updatemenus=updatemenus)

    layout['annotations'] = annotations

    fig = dict(data=trace_list, layout=layout)

    py.iplot(fig, filename='Sentiment Pie Chart')

# Plot a pie chart of generalized sentiments
def plotSentimentPieChart2(dataset):
    sentiment_distribution = dataset[:,4].astype(float)
    magnitude_distribution = dataset[:,5].astype(float)

    sentiment_distribution_np = np.array(sentiment_distribution)
    magnitude_distribution_np = np.array(magnitude_distribution)

    number_negative = (sentiment_distribution_np < 0).sum()
    number_positive = (sentiment_distribution_np > 0).sum()

    number_neutral = ((sentiment_distribution_np == 0) & (magnitude_distribution_np == 0)).sum()
    number_mixed = ((sentiment_distribution_np == 0) & (magnitude_distribution_np > 0)).sum()

    pie_labels = ['Positive','Negative','Neutral','Mixed']
    pie_values = [number_positive,number_negative,number_neutral,number_mixed]

    trace = go.Pie(labels=pie_labels, values=pie_values)

    py.iplot([trace], filename='Sentiment Pie Chart')

def plotDiscussionTimes(dataframe):

    subreddit_name_list = []

    # Get possible values of subreddit names
    for record in dataframe.values:
        if not subreddit_name_list.__contains__(record[2]):
            subreddit_name_list.append(record[2])

    subreddit_sentiment_list = []
    for subreddit_name in subreddit_name_list:
        subreddit_dataframe = dataframe[dataframe['subreddit'] == subreddit_name]
        subreddit_sentiment_distribution_np = np.array(subreddit_dataframe.values \
                                            [:,1].astype(datetime.datetime))
        subreddit_sentiment_list.append(subreddit_sentiment_distribution_np)

    histogram_list = []
    for subreddit_sentiment, subreddit_name in zip(subreddit_sentiment_list,subreddit_name_list):
        trace = go.Histogram(x=subreddit_sentiment,opacity=0.75,name=subreddit_name)
        histogram_list.append(trace)

    layout = go.Layout(barmode='overlay')
    fig = go.Figure(data=histogram_list, layout=layout)

    py.iplot(fig, filename='Comment Times by Subreddit')


# Start of executing statements
# Set credentials
plotly.tools.set_credentials_file(username=config.plotly_username, api_key=config.plotly_api_key)

# Load the data
dataframe = pandas.read_csv("cumulative-comment-data.csv")
dataset = dataframe.values

# Plot different charts
#plotSentimentDistributions(dataframe)
plotSentimentPieChart(dataset)
#plotDiscussionTimes(dataframe)