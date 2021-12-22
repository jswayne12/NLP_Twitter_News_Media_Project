import snscrape.modules.twitter as sntwitter
import pandas as pd
from textblob import TextBlob

import nltk
nltk.download('stopwords')
from sumy.utils import get_stop_words
stopwords = list(get_stop_words('english'))
class Data_swiper:
    def __init__(self):
        self.size = 10
    def pull_from_sql(self):
        pass
    def get_tweets(self, person):
        tweet_list = []
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{person["entity"]}').get_items()):
            if i >= person['tweet number']:
                break
            else:
                tweet_list.append([tweet.id, tweet.username, tweet.date, [tweet.content]])
        return tweet_list
    def pull_from_twitter(self, nested_list):
        complete_twitter_list = []
        for alignment in nested_list:
            alignment_list = [self.get_tweets(person) for person in alignment]
            complete_twitter_list.extend(alignment_list)
        return complete_twitter_list
    def delete_repeated_data(self):
        pass
    def add_data_together(self, list, news_type):
        #list is equal to tweet_list1
        if news_type == 'alternative':
            tweet_list = []
            for person in list:
                tweet_list.extend(person)
            lib = pd.DataFrame(tweet_list[0:306], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])
            con = pd.DataFrame(tweet_list[306:], columns=['Tweet ID', 'Username', 'Datetime', 'Content'])

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
        import string
        string_punctuation = [char for char in string.punctuation]
        string_list = [char for char in string_ if char not in string_punctuation]
        clean_of_punt = ''.join(string_list)
        clean_punct_list = clean_of_punt.split()
        clean_of_stop_words = [word for word in clean_punct_list if word not in stopwords]
        return clean_of_stop_words
    def clean_data_partial(self, string_):
        import string
        string_punctuation = [char for char in string.punctuation]
        string_list = [char for char in string_ if char not in string_punctuation]
        joined_list = ''.join(string_list)
        return joined_list
    def add_POS_column(self,df):
        df['Part of Speech'] = [TextBlob(x).tags for x in df['Content']]
        n=0
        for POS in df['Part of Speech'].copy():
            df['Part of Speech'][n] = [tuple_ for tuple_ in POS if tuple_[0].lower() not in stopwords]
            n+=1
        return df
    def add_clean_content_column(self, df):
        df['Cleaned Tweets'] = df['Content'].apply(self.clean_data)
        return df
    def clean_time(self, df):
        datetime = []
        for element in df['Datetime']:
            element = str(element)
            new_element = element[0:10]
            datetime.append(new_element)
        df_datetime = pd.DataFrame(datetime, columns=['Datetime'])
        df = df.drop(columns=['Datetime'])
        df = pd.concat([df, df_datetime], axis=1)
        return df
    def make_clean_dataframe(self, df):
        final_df = self.add_clean_content_column(df)
        return final_df