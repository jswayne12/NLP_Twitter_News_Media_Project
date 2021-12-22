import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from collections import Counter
import nltk
import plotly.graph_objects as go
from NLP_Twitter_News_Media_Project.data_swiper import Data_swiper
class Data_visualization:
    def __init__(self, df):
        self.df = df
        self.data_swiper = Data_swiper()
    def make_word_cloud(self, df, name):
        all_cleaned_data = []
        for list_ in df['CONTENT']:
            string = list_[1:-1]
            cleaned_string = self.data_swiper.clean_data(string)
            all_cleaned_data.extend(cleaned_string)
        count_of_words = Counter(all_cleaned_data)
        word_cloud = WordCloud(width=1000, height=500).generate_from_frequencies(count_of_words)
        plt.figure(figsize=(20, 10))
        plt.figtext(.5, .9, name, fontsize=60, ha='center')
        plt.imshow(word_cloud)
        plt.axis('off')
        plt.show()

    def make_histogram(self, df, attribute, bin_width, hue=None, element='step'):
        sns.histplot(data=df, x=attribute, binwidth=bin_width, kde=True, hue=hue, element=element)

    def hist_comparison(title, sub_titles, dfs, attribute, binwidth, num_hist):
        fig, axes = plt.subplots(1, num_hist, sharex=True, figsize=(10, 5))
        fig.suptitle(title)
        for i in range(num_hist):
            axes[i].set_title(sub_titles[i])
        for i in range(num_hist):
            sns.histplot(ax=axes[i], data=dfs[i], x=attribute, binwidth=binwidth, kde=True, hue=None, element='step')

    def make_word_frequency_graph(self, df):
        all_cleaned_data = []
        for list_ in df['CONTENT']:
            string = list_[1:-1]
            cleaned_string = self.data_swiper.clean_data(string)
            all_cleaned_data.extend(cleaned_string)
        album_frequency = nltk.FreqDist(all_cleaned_data)
        album_frequency.plot(30)
    def make_bar_graph(self, x_axis, y_axis, color=None):
        sns.set(style="darkgrid")
        sns.barplot(x=x_axis,y=y_axis,data=self.df, color=color)

    def q1(self, x):
        return x.quantile(0.25)

    def q3(self, x):
        return x.quantile(0.75)

    def make_candle_plot(self, df, groupby_, attribute):
        group_data = df.groupby([groupby_]).agg({f'{attribute}': ['mean', 'min', 'max', self.q1, self.q3]})
        group_data.rename(columns={'<lambda_0>': '25th', '<lambda_1>': '75th'}, inplace=True)
        group_data.reset_index(inplace=True)
        print(group_data)
        fig = go.Figure(data=[go.Candlestick(x=group_data[groupby_],
                                             open=group_data[attribute]['q1'],
                                             close=group_data[attribute]['q3'],
                                             high=group_data[attribute]['max'],
                                             low=group_data[attribute]['min'])])
        fig.show()

    def make_candle_plot_multi(self, df, groupby_, attribute):
        group_data = df.groupby(groupby_).agg({f'{attribute}': ['mean', 'min', 'max', self.q1, self.q3]})
        group_data.rename(columns={'<lambda_0>': '25th', '<lambda_1>': '75th'}, inplace=True)
        group_data.reset_index(inplace=True)
        group_data['INTERSECTION'] = group_data['POLITICAL_ALIGNMENT'] + ' / ' + group_data['NEWS_SOURCES_TYPE']
        print(group_data)
        fig = go.Figure(data=[go.Candlestick(x=group_data['INTERSECTION'],
                                             open=group_data[attribute]['q1'],
                                             close=group_data[attribute]['q3'],
                                             high=group_data[attribute]['max'],
                                             low=group_data[attribute]['min'])])
        fig.show()
    def make_pie_chart_SA(self):
        self.df['SA_Level'] = 'Neutral'
        self.df['SA_Level'] = ['Positive' for rate in self.df['Overall Sentiment'] if self.df['Overall Sentiment'] > 0.35 ]
        self.df['SA_Level'] = ['Negative' for rate in self.df['Overall Sentiment'] if self.df['Overall Sentiment'] < -0.35]
        groups = self.df.groupby('SA_Level')
        positive = groups.get_group('Positive')
        negative = groups.get_group('Negative')
        neutral = groups.get_group('Neutral')
        slices= [len(positive), len(negative), len(neutral)]
        labels = ['Positive', 'Negative', 'Neutral']
        colors = ['blue', 'red', 'yellow']
        plt.pie(slices, labels=labels, colors=colors)
    def make_common_NE_chart(self):
        named_entities = []
        for entities in self.df['Name Entities']:
            named_entities.extend(entities)
        named_entities_freq = nltk.FreqDist(named_entities)
        named_entities_freq.plot(30)