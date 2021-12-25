from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from spacy.language import Language
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
Language.component("spacytextblob")
class Nlp_analysis:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe('spacytextblob')

    def sentiment_analysis(self, df):
        #Creates a new column in the dataframe that provided the sentiment of the tweet
        df['Overall Sentiment'] = [self.analyzer.polarity_scores(list)['compound'] for list in df['CONTENT']]
        return df

    def NER_string(self, string):
        #Returns all of the Named Entities in a string
        doc = self.nlp(string)
        entities = [ent.text for ent in doc.ents]
        return entities

    def NER_string_text(self, list):
        # Returns a nested list encompasses lists that give a Named Entity and the sentimental context that Entity is found in
        entity_list = []
        for element in list:
            doc = self.nlp(element)
            entities = [ent.text for ent in doc.ents]
            sentiment = self.analyzer.polarity_scores(element)['compound']
            entity_sentiment = [entities, sentiment]
            entity_list.append(entity_sentiment)
        return entity_list

    def name_entity_analysis(self, df):
        # Creates Named Entity column by applying the NER_string method on each row of the CONTENT column
        df['Named Entities'] = [self.NER_string(content) for content in df['CONTENT']]
        return df

    def name_sentiment(self, df):
        # Creates Name Sentiment Analysis column by applying the NER_string_text method on each row of the CONTENT column
        #after separating the Content column values into sentences.
        df['Name Sentiment Analysis'] = [nltk.tokenize.sent_tokenize(content)for content in df['CONTENT']]
        df['Name Sentiment Analysis'] = [self.NER_string_text(list) for list in df['Name Sentiment Analysis']]
        return df

    def subjectivity_analysis(self, df):
        # Creates the Subjectivity column by running nltk's subjectivity function on the elements of the Content column
        df['Subjectivity'] = [self.nlp(list)._.subjectivity for list in df['CONTENT']]
        return df

    def full_analysis(self, df):
        #Pulls all the functions of the class together to create new dataframe that has extracted nlp-related data
        sentiment_df = self.sentiment_analysis(df)
        subjectivity_df = self.subjectivity_analysis(sentiment_df)
        ner_df = self.name_entity_analysis(subjectivity_df)
        nlp_df = self.name_sentiment(ner_df)
        return nlp_df