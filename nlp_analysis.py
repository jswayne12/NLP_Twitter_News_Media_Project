from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from spacy.language import Language
import nltk
import pandas as pd
nltk.download('vader_lexicon')
nltk.download('punkt')
Language.component("spacytextblob")
class Nlp_analysis:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe('spacytextblob')
    def sentiment_analysis(self, df):
        df['Overall Sentiment'] = [self.analyzer.polarity_scores(list)['compound'] for list in df['CONTENT']]
        return df
    def NER_string(self, string):
        doc = self.nlp(string)
        entities = [ent.text for ent in doc.ents]
        return entities
    def NER_string_text(self, list):
        entity_list = []
        for element in list:
            doc = self.nlp(element)
            entities = [ent.text for ent in doc.ents]
            sentiment = self.analyzer.polarity_scores(element)['compound']
            entity_sentiment = [entities, sentiment]
            entity_list.append(entity_sentiment)
        return entity_list
    def name_entity_analysis(self, df):
        df['Named Entities'] = [self.NER_string(content) for content in df['CONTENT']]
        return df
    def name_sentiment(self, df):
        df['Name Sentiment Analysis'] = [nltk.tokenize.sent_tokenize(content)for content in df['CONTENT']]
        df['Name Sentiment Analysis'] = [self.NER_string_text(list) for list in df['Name Sentiment Analysis']]
        return df
    def subjectivity_analysis(self, df):
        df['Subjectivity'] = [self.nlp(list)._.subjectivity for list in df['CONTENT']]
        return df
    def full_analysis(self, df):
        sentiment_df = self.sentiment_analysis(df)
        subjectivity_df = self.subjectivity_analysis(sentiment_df)
        ner_df = self.name_entity_analysis(subjectivity_df)
        nlp_df = self.name_sentiment(ner_df)
        return nlp_df