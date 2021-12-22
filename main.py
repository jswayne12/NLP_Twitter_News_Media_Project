
from twitter_queries import conservative_news, conservative_alt, conservative_politicians, moderate_politicians, moderate_news
from twitter_queries import liberal_news,liberal_alt,liberal_politicians
from pre_twitter_handler import Pre_twitter
from data_swiper import Data_swiper
from sql_storage import Ibm_sql
from nlp_analysis import Nlp_analysis
import pandas as pd
import ibm_db_dbi


pd.set_option('display.max_columns', 15)

ibm_storage = Ibm_sql()
conn = ibm_storage.create_database_connection()
pconn = ibm_db_dbi.Connection(conn)

operation = input("""Which operation will we be using sir/ma'am? \n 'D' for Data-Pull, \n 'PRE SQL' for SQL PRE-NLP,
                    \n 'NLP' for NLP operations, \n 'POST SQL' for SQL POST NLP \n""")

if operation == 'D':
    #We have put all entities and their twitters into a nested list
    all_lists = [conservative_news,moderate_news,liberal_news,conservative_politicians, moderate_politicians,
                 liberal_politicians, liberal_alt, conservative_alt]

    #These lists are all twitters repeated/scaled by their respective array --- twitter_queries
    weighted_lists = []
    for element in all_lists:
        pre_tweet = Pre_twitter(element)
        weighted_lists.append(pre_tweet.make_weighted_twitter_list())

    #Instead of the twitters repeated, we give the tweet and the number it should searched inside a nested list/dictionary
    tweet_counter = pre_tweet.tweet_counter(weighted_lists) #counts but in count object. Need to make a list
    tweet_pull_per_entity = []
    for dic in tweet_counter:
        list_ = [{'entity':key, 'tweet number':value} for (key,value) in dict.items(dic)]
        tweet_pull_per_entity.append(list_)

    #We separated the previous list into the three sections of study
    traditional_news = tweet_pull_per_entity[0:3]
    politicians = tweet_pull_per_entity[3:6]
    alt_news = tweet_pull_per_entity[6:8]

    #Create the twitter swiper object
    twitter_swiper = Data_swiper()

    #All tweets collected in nested lists
    traditional_tweet_list = twitter_swiper.pull_from_twitter(traditional_news)
    alternative_tweet_list = twitter_swiper.pull_from_twitter(alt_news)
    politician_tweet_list = twitter_swiper.pull_from_twitter(politicians)

    #The dataframes
    df_traditional = twitter_swiper.add_data_together(traditional_tweet_list, 'traditional')
    df_alternative = twitter_swiper.add_data_together(alternative_tweet_list, 'alternative')
    df_politician = twitter_swiper.add_data_together(politician_tweet_list, 'politician')

    #Combine dataframes
    df = twitter_swiper.combine_dataframes(df_politician, df_alternative, df_traditional)

    #Clean Data
    clean_df1 = twitter_swiper.make_clean_dataframe(df)
    final_df = twitter_swiper.clean_time(clean_df1)
    final_df.to_csv('twitter_data.csv')

    sql_name = input('What would you like to name you SQL table?')
    ibm_storage.make_query(f'''CREATE TABLE {sql_name} (index INT NOT NULL, tweet_id BIGINT NOT NULL PRIMARY KEY,
                                    username VARCHAR(20), content VARCHAR(1000), political_alignment VARCHAR(15), 
                                    news_sources_type VARCHAR(15), cleaned_tweets VARCHAR (1000), datetime TIMESTAMP)''')

elif operation == 'PRE SQL':
    #Start SQL queries
    pd.set_option('display.max_columns', 15)
    sql_table = input('Which SQL table would you like to modify?')

    ibm_storage.make_query(f'''ALTER TABLE {sql_table}
                                ADD length_of_tweet INT''')
    ibm_storage.make_query(f'''UPDATE {sql_table}
                                SET length_of_tweet = CAST((LENGTH(content) - LENGTH(REPLACE(content, ' ',
                                '')))+1 as INT) ''')
    ibm_storage.make_query(f'''ALTER TABLE {sql_table}
                                ADD day_name VARCHAR(10)''')
    ibm_storage.make_query(f'''UPDATE {sql_table}
                                SET day_name = CAST(DAYNAME(datetime) as VARCHAR(10))''')
    ibm_storage.close_connection()

elif operation == 'NLP':
    #Pulling table from SQL
    nlp_sql_table = input('Which sql table would you like to use for NLP operations? ')
    sql_df = pd.read_sql(f'SELECT * from {nlp_sql_table}', pconn)

    #Running NLP analysis
    nlp_analysis = Nlp_analysis()
    nlp_df = nlp_analysis.full_analysis(sql_df)

    #Data formatting
    nlp_df = nlp_df.drop(columns=['INDEX'])

    print(nlp_df.head(10))

    #Preparing data storage
    nlp_df.to_csv('nlp_df.csv')
    nlp_sql_table_name = input('What would you like to name this SQL table (NLP)? ')
    ibm_storage.make_query(f'''CREATE TABLE {nlp_sql_table_name} (index INT NOT NULL, tweet_id BIGINT NOT NULL PRIMARY KEY,
                                username VARCHAR(20), content VARCHAR(1000), political_alignment VARCHAR(15),
                                news_sources_type VARCHAR(15), cleaned_tweets VARCHAR(1000), datetime TIMESTAMP,
                                length_of_tweet INT, day_of_week VARCHAR(10), overall_sentiment DECIMAL (5,4),
                                Subjectivity DECIMAL (4,3), named_entities VARCHAR(500), named_sentiment VARCHAR(500)) ''')

