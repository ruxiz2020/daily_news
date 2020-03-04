import pandas as pd
import requests
from config import dict_all_news_url, dict_all_cn_news_url

#### start: generate new df
# API Requests for news div
def gen_df_news_title(request_news):
    try:
        json_data = request_news.json()["articles"]
    except:
        json_data = request_news.json()["results"]
    df = pd.DataFrame(json_data)
    df = pd.DataFrame(df[["title", "url"]])

    return df

dfs = []
for key in dict_all_news_url.keys():
    #print(key)
    news_requests = requests.get(dict_all_news_url[key])
    df = gen_df_news_title(news_requests)
    df["type"] = key
    dfs.append(df)

all_df_news = pd.concat(dfs)

dfs = []
for key in dict_all_cn_news_url.keys():
    #print(key)
    news_requests = requests.get(dict_all_cn_news_url[key])
    df = gen_df_news_title(news_requests)
    df["type"] = key
    dfs.append(df)

all_df_cn_news = pd.concat(dfs)
#### end: generate new df
