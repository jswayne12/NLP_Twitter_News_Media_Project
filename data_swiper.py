import snscrape.modules.twitter as sntwitter
import pandas as pd
import nltk
from sumy.utils import get_stop_words
import string
nltk.download('stopwords')
stopwords = list(get_stop_words('english'))

#This is the class used to pull, format, and pre-process the data from twitter
class Data_swiper:
    def __init__(self):
        self.size = 10
    def get_tweets(self, person):
        #This is the lowest level of the data extraction. It collects the tweet of each entity
        tweet_list = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{person["entity"]}').get_items()):
            if i >= person['tweet number']:
                break
            else:
                tweet_list.append([tweet.id, tweet.username, tweet.date, [tweet.content]])
        return tweet_list
    def pull_from_twitter(self, nested_list):
        #This incorporates the get_tweets method in order to make a complete list of all tweets to be used
        complete_twitter_list = []
        for alignment in nested_list:
            alignment_list = [self.get_tweets(person) for person in alignment]
            complete_twitter_list.extend(alignment_list)
        return complete_twitter_list
    def add_data_together(self, list, news_type):
        #We use this to combine a set of tweets together into a dataframe. Each set represents a 'news type'
        #The list is rendered into a format able to be transformed into a dataframes
        if news_type == 'alternative':
            tweet_list = []
            for person in list:
                tweet_list.extend(person)
            lib = pd.DataFrame(tweet_list[0:306], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            con = pd.DataFrame(tweet_list[306:], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])

            #Adding the features of Political Alignment
            lib['Political Alignment'] = 'Liberal'
            con['Political Alignment'] = 'Conservative'
            df_2 = lib.append(con, ignore_index=True)
            df_2['News Source Type'] = 'Alternative'
        elif news_type == 'politician':
            tweet_list = []
            for person in list:
                tweet_list.extend(person)
            con = pd.DataFrame(tweet_list[0:216], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            mod = pd.DataFrame(tweet_list[216:432], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            lib = pd.DataFrame(tweet_list[432:], columns=['Tweet ID', 'Username', 'Datetime', 'Content'] )

            lib['Political Alignment'] = 'Liberal'
            con['Political Alignment'] = 'Conservative'
            mod['Political Alignment'] = 'Moderate'
            df_2 = con.append(mod, ignore_index=True)
            df_2 = df_2.append(lib, ignore_index=True)
            df_2['News Source Type'] = 'Politician'
        elif news_type == 'traditional':
            tweet_list = []
            for person in list:
                tweet_list.extend(person)
            con = pd.DataFrame(tweet_list[0:1794], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            mod = pd.DataFrame(tweet_list[1794:3588], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            lib = pd.DataFrame(tweet_list[3588:], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])

            lib['Political Alignment'] = 'Liberal'
            con['Political Alignment'] = 'Conservative'
            mod['Political Alignment'] = 'Moderate'
            df_2 = con.append(mod, ignore_index=True)
            df_2 = df_2.append(lib, ignore_index=True)
            df_2['News Source Type'] = 'Traditional'
        return df_2
    def combine_dataframes(self, df1, df2, df3):
        df = df1.append(df2, ignore_index=True)
        df = df.append(df3, ignore_index=True)
        return df
    def clean_data(self,string_):
        #Used as the low level method that cleans each individual tweet

        #Eliminating all punctuation from the tweet, rendering it as a list of characters
        string_punctuation = [char for char in string.punctuation]
        string_list = [char for char in string_ if char not in string_punctuation]

        #Rejoin the list of characters into a string again
        clean_of_punt = ''.join(string_list)

        #Eliminate stopwords
        clean_punct_list = clean_of_punt.split()
        clean_of_stop_words = [word for word in clean_punct_list if word not in stopwords]
        return clean_of_stop_words

    def add_clean_content_column(self, df):
        #Using the clean_data method to create a column of cleaned tweets
        df['Cleaned Tweets'] = df['Content'].apply(self.clean_data)
        return df

    def clean_time(self, df):
        #This cleans up the formatting of the datetime column
        datetime = []
        for element in df['Datetime']:
            element = str(element)
            #Eliminating irrelevant data
            new_element = element[0:10]
            datetime.append(new_element)
        #Create a dataframe holding our new Datetime, eliminating the old Datetime column and appending the new dataframe to original
        df_datetime = pd.DataFrame(datetime, columns=['Datetime'])
        df = df.drop(columns=['Datetime'])
        df = pd.concat([df, df_datetime], axis=1)
        return df

    def make_clean_dataframe(self, df):
        #Final dataframe function
        final_df = self.add_clean_content_column(df)
        return final_df