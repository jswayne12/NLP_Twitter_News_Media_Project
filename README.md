# USA News Media Analysis Through the Political Spectrum

### Description
This is meant to be an end-to-end project whose goal is to create a machine learning based
application that is able to predict where on the political spectrum lies a particular news outlet.
It starts through data collection from twitter. Before the actual data collection, the choice of independent variables was needed.
These variables were based on common political alignments and news outlet types. From there came the 
designations of who would represent these features in the datasets. Upon acquiring the who, the 'how many' of each
was loosely based on the overall popularity of the account as well as activity. From here, I commenced the data collection portion
through snscrape. After collecting the data through snscrape and formatting the data with pandas, I did a bit of data cleaning (mostly text  pre-processing), 
which was then followed by feature engineering. The primary features pulled were sentiments, subjectivity, day of week,
and length. These features were extracted using nlp applications as well as SQL. With the data being collected, cleaned, 
formatted, and having all relevant features extracted, came the use of Jupyter Notebooks to engage in Exploratory Data 
Analysis (mostly statistical analysis and visualizations) to get a better understanding of the dataset. I hope to be able
to use what was learned from the EDA to be able to create a machine learning model and hopefully put it into production.


### How to Install plus additional info

- Access to the code used for data collection, pre-processing, nlp processes, and data storage is availible through github. 
It would only need to be cloned. 
- Portions of the code relating to data storage will need to be updated for your specific use cases (My code uses ibm_db).

### How to use the Project
- As stated earlier, some changes to sql_storage.py will be needed in order to engage in the sql processes.
- After code has been cloned, check to make sure all necessary library installations are done.
- Then simply run the program and follow the instructions as given. The options are given in the order of a usual data project, 
starting with data collection up to NLP processes, but one can simply choose the process as they need them.
- When transferring over into a jupyter notebook, one can use a modified version of the code given in data_viz.py. The 
modification would revolve around eliminating the OOP aspects and setting the methods as simply functions within the notebook
