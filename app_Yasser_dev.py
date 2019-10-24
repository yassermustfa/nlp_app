import pandas as pd
import pandas_profiling as pp
import matplotlib.pyplot as plt
#import newspaper
#from newspaper import Article
#import googlesearch
##from newspaper import fulltext
##import requests
##import nltk
##nltk.download('punkt')
#from newspaper.configuration import Configuration
#from fastai import *
#from fastai.text import *
#from fastai.core import *
import streamlit as st

import plotly.graph_objects as go
import plotly.express as px

fig1 = go.Figure(data=go.Bar(y=[2, 3, 1]))
labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig2 = go.Figure(data=[go.Pie(labels=labels, values=values)])
dataset = pd.DataFrame({'x':[0, 1, 2, 3, 4], 'y':[0, 1, 4, 9, 16]})
fig3 = px.scatter(x='x', y='y', data_frame = dataset )

iris = px.data.iris() # iris is a pandas DataFrame
fig4 = px.scatter(iris, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
#fig.show()
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
#
#path = r'C:\Users\yasse\OneDrive\Desktop\fakeNews\IF Chris\df_text_cat.csv'
#df1 = pd.read_csv(path)
##ppp = pp.ProfileReport(df1)
##
##st.markdown(r'C:\Users\yasse\Downloads\Intl_SOS_Full_CSV_011019_Yasser_notReady-Copy1.html', unsafe_allow_html=True)
#
#user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
#config = Configuration()
#config.browser_user_agent = user_agent
##config.get_parser
#
#path = r'C:\Users\yasse\OneDrive\Desktop\fakeNews\IF Chris'
#data_lm = load_data(path, 'data_lm_export.pkl')
#data_clas = load_data(path, 'data_clas_export.pkl', bs=32)
#learn_m = text_classifier_learner(data_clas, AWD_LSTM, drop_mult=0.5)
#learn_m = learn_m.load(path + '\\' + "model_021019")
#
#st.sidebar.title('Intelligence Fusion App')
#st.sidebar.info(''' 
#This application gathers the latest news from the **BBC News**, **The Guardian** and
# **CNN** newspapers , and predicts their categories: **Small Arms Fire 
# (Direct Weapons)**, **Arrest (Criminality)**, **Murder (Criminality)**, 
# **Close Quarter Assassination (Direct Weapons)** and **Burglary/Theft (Criminality)**.
#''')
#parsing_options = st.sidebar.radio('Select Parsing Method: ', ['Newspaper', 'Query']) #, default = [options[0]])
#
#data = {"BBC": "https://www.bbc.co.uk/news", "CNN": "http://edition.cnn.com", "The Guardian": "https://www.theguardian.com/international"}
#options = list(data.keys())
##url_ = st.text_input('Enter URL')
##try:
##@st.cache
#articles_url = []
#if parsing_options == 'Newspaper':
#    newsp_select = st.sidebar.radio('Select a Newspaper: ', options) 
#    news_paper = newspaper.build(data[newsp_select], memoize_articles=False)
#    for article in news_paper.articles:
#        articles_url.append(article.url)
#else:    
#    query = st.sidebar.text_input('Enter your Query ', 'arrest') #'burglary theft'  #"trump"    
#    for articl in googlesearch.search_news(query, tld="com", num=500, stop=200, pause=.01):
#        articles_url.append(articl)
#
#
#    #print(article.url)
#
#
#articles_url_df = pd.DataFrame(articles_url, columns = ['articles'])
##articles_url_df
#
##@st.cache
#def articles_scraping(articles_url_df):
#    link = []
#    summ = []
#    txt = []
#    titl = []
#    
#    m = int(st.sidebar.text_input('Enter Number of Articles ', 5))
#    if m >= len(articles_url_df):
#        m = len(articles_url_df)     
#    for i in range(1,  m+1):   # len(articles_url_df)): n+1):
#        url = articles_url_df['articles'][i]
#        link.append(url)
#        article = Article(url, config = config)
#        # Try-Except-Continue will skip to the next article in the For loop if there is an exception
#    
#    #    try:
#    #        article.download()
#    #        article.parse()
#    #        #article.nlp()
#    #    except:
#    #        print('Exception Error....!')
#    #        continue
#        article.download()
#        article.parse()
#    #     print(article.authors)
#    #     print("Article Publication Date:")
#    #     print(article.publish_date)
#    #     print("Major Image in the article:")
#    #     print(article.top_image)
#        article.nlp()
#    #     print ("Keywords in the article")
#    #     print(article.keywords)
#    #     print("Article Summary")
#        summ.append(article.summary)
#        txt.append(article.text)
#        titl.append(article.title)
#        
#    d = {'link': link, 'title': titl, 'summary': summ, 'text': txt}
#    articles_full = pd.DataFrame(d)
#    return articles_full
#
#df = articles_scraping(articles_url_df)
#
#n = len(df)
##n = int(st.text_input('Number of Predicted Articles ', 5))
##if n >= len(df):
##    n = len(df)
#    
#for i in range(n): # len(df)):
#    df['predicted'] = learn_m.predict(df['text'][i])[0]
#    print(learn_m.predict(df['text'][i])[0])
#
#def make_clickabe(val):
#    return '<a target="_blank" href = "{}">{}</a> '.format(val, val)
#df1 = df.style.format({'link': make_clickabe}) 
#
#if st.checkbox('Show dataframe', True):
#    st.write(df)  #, unsafe_allow_html = True)
#
##def write():
##    st.markdown(
##        """
##        ## APP NAME
##
##        DESCRIPTION
##
##        Author: [YOUR NAME](https://URL_TO_YOU))\n
##        Source: [Github](https://github.com/URL_TO_CODE)
##        """
##    )
##    # Your code goes below
##
##if __name__ == "__main__":
##    write()
#
##st.write(dir(st))