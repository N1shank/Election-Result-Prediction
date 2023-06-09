#------------------------------US Elections Prediction------------------------------------------                         

# K.Nishank CS20B1095
import pandas as pd
import numpy as np
from textblob import TextBlob
import plotly.graph_objects as pt


trump_reviews = pd.read_csv("D:\Codes\Python\DS Project\Trump_Twitter.csv")      
biden_reviews = pd.read_csv("D:\Codes\Python\DS Project\Biden_Twitter.csv")

# Prints first 5 rows of both data sets extracted from twitter 
print(trump_reviews.head())        
print(biden_reviews.head())

#Simple text classification based on sentiment
textblob1 = TextBlob(trump_reviews["text"][10])
print("Trump :",textblob1.sentiment)

textblob2 = TextBlob(biden_reviews["text"][500])
print("Biden :",textblob2.sentiment)


# Polarity
def find_pol(review):
    return TextBlob(review).sentiment.polarity
trump_reviews["Sentiment Polarity"] = trump_reviews["text"].apply(find_pol)
print(trump_reviews.tail())

biden_reviews["Sentiment Polarity"] = biden_reviews["text"].apply(find_pol)
print(biden_reviews.tail())


# Adding new Attribute in Data sets 
# Polarity = 0 means they are neutral with the Politician
trump_reviews["Expression Label"] = np.where(trump_reviews["Sentiment Polarity"]>0, "positive", "negative")
trump_reviews["Expression Label"][trump_reviews["Sentiment Polarity"]==0]="Neutral"
print(trump_reviews.tail())

biden_reviews["Expression Label"] = np.where(biden_reviews["Sentiment Polarity"]>0, "positive", "negative")
biden_reviews["Expression Label"][trump_reviews["Sentiment Polarity"]==0]="Neutral"
print(biden_reviews.tail())


# Cleaning
reviews1 = trump_reviews[trump_reviews['Sentiment Polarity'] == 0.0000]
print(reviews1.shape)

cond1=trump_reviews['Sentiment Polarity'].isin(reviews1['Sentiment Polarity'])
trump_reviews.drop(trump_reviews[cond1].index, inplace = True)
print(trump_reviews.shape)

reviews2 = biden_reviews[biden_reviews['Sentiment Polarity'] == 0.0000]
print(reviews2.shape)

cond2=biden_reviews['Sentiment Polarity'].isin(reviews1['Sentiment Polarity'])
biden_reviews.drop(biden_reviews[cond2].index, inplace = True)
print(biden_reviews.shape)

# Donald Trump
np.random.seed(10)
remove_n =324
drop_indices = np.random.choice(trump_reviews.index, remove_n, replace=False)
df_subset_trump = trump_reviews.drop(drop_indices)
print(df_subset_trump.shape)
# Joe Biden
np.random.seed(10)
remove_n =31
drop_indices = np.random.choice(biden_reviews.index, remove_n, replace=False)
df_subset_biden = biden_reviews.drop(drop_indices)
print(df_subset_biden.shape)


# Analysis

count_1 = df_subset_trump.groupby('Expression Label').count()
print(count_1)

negative_per1 = (count_1['Sentiment Polarity'][0]/1000)*10
positive_per1 = (count_1['Sentiment Polarity'][1]/1000)*100

count_2 = df_subset_biden.groupby('Expression Label').count()
print(count_2)

negative_per2 = (count_2['Sentiment Polarity'][0]/1000)*100
positive_per2 = (count_2['Sentiment Polarity'][1]/1000)*100

Politicians = ['Joe Biden', 'Donald Trump']
lis_pos = [positive_per1, positive_per2]
lis_neg = [negative_per1, negative_per2]


#Showing Everything in Bar Graph
fig = pt.Figure(data=[
    pt.Bar(name='Positive', x=Politicians, y=lis_pos),
    pt.Bar(name='Negative', x=Politicians, y=lis_neg)
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()

