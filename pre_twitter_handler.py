from twitter_modeler import Twitter_modeler
import numpy as np
from collections import Counter
class Pre_twitter:
    def __init__(self, list):
        self.list = list
    def make_weighted_twitter_list(self):
        entity_list = []
        twitter_list = []
        all_list = []
        for i in self.list:
            entity = i['entity']
            twitter = i['twitter']
            all = Twitter_modeler(entity, twitter)
            entity_list.append(entity)
            twitter_list.append(twitter)
            all_list.append(all)
        array = entity_list[len(entity_list) - 1]
        weighted_twitter_list = []
        n=0
        for i in twitter_list:
            elements = [i] * array[n]
            n += 1
            weighted_twitter_list.extend(elements)
        return(weighted_twitter_list)
    def make_list(self, list_slice, number):
        tweet_call_list = []
        for list in list_slice:
            search_list = []
            scale = round(number / len(list))
            weighted_array = np.array(list)
            for entity in weighted_array:
                scaled_entity = [entity] * scale
                search_list.extend(scaled_entity)
            search_list = Counter(search_list)
            tweet_call_list.append(search_list)
        return tweet_call_list
    def tweet_counter(self, weighted_lists):
        news = weighted_lists[0:3]
        politicians = weighted_lists[3:6]
        alt = weighted_lists[6:8]
        news_tweet_call_list = self.make_list(news, 1800)
        politician_tweet_call_list = self.make_list(politicians,210)
        alt_tweet_call_list = self.make_list(alt, 300)
        all_tweet_call = news_tweet_call_list+politician_tweet_call_list+alt_tweet_call_list
        tweet_value_counts = [dict(i) for i in all_tweet_call]
        return tweet_value_counts