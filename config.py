# API Requests for news div

api_key_newsapi = "3cdcafec00bc4906a79f6f98df73125c"
api_key_nyt = "oWjYqEZKfWHgBTwEyQlLVU4dOO7mCLcl"

dict_all_news_url = {
    "bbc_news": "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=" + api_key_newsapi,
    "us_news": "http://newsapi.org/v2/top-headlines?country=us&apiKey=" + api_key_newsapi,
    "wsj_nyt_news": "http://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&apiKey=" + api_key_newsapi,
    "nyt_news": "https://api.nytimes.com/svc/topstories/v2/home.json?api-key=" + api_key_nyt,
    "yahoo_news": "http://newsapi.org/v2/everything?domains=yahoo.com&apiKey=" + api_key_newsapi,
    "us_business_news": "http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=" + api_key_newsapi,
    "us_tech_news": "http://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=" + api_key_newsapi,
    "us_health_news": "http://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=" + api_key_newsapi,
    "us_science_news": "http://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=" + api_key_newsapi,
    "us_entertainment_news": "http://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=" + \
                            api_key_newsapi,
    "us_sports_news": "http://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=" + \
                            api_key_newsapi,
    "pet_news": "http://newsapi.org/v2/everything?q=pet&apiKey="+ api_key_newsapi,
    "dog_news": "http://newsapi.org/v2/everything?q=dog&apiKey="+ api_key_newsapi,
    "cat_news": "http://newsapi.org/v2/everything?q=cat&apiKey="+ api_key_newsapi,
}


dict_all_cn_news_url = {
    "头条": "http://newsapi.org/v2/top-headlines?country=cn&apiKey=" + api_key_newsapi,
    "商业": "http://newsapi.org/v2/top-headlines?country=cn&category=business&apiKey=" + api_key_newsapi,
    "技术": "http://newsapi.org/v2/top-headlines?country=cn&category=technology&apiKey=" + api_key_newsapi,
    "健康": "http://newsapi.org/v2/top-headlines?country=cn&category=health&apiKey=" + api_key_newsapi,
    "科学": "http://newsapi.org/v2/top-headlines?country=cn&category=science&apiKey=" + api_key_newsapi,
    "娱乐": "http://newsapi.org/v2/top-headlines?country=cn&category=entertainment&apiKey=" + \
                            api_key_newsapi,
    "运动": "http://newsapi.org/v2/top-headlines?country=cn&category=sports&apiKey=" + \
                            api_key_newsapi
}

stock_data_url = "https://stooq.com/db/h/"
dict_stock_data_url = {
    "stock_data_5min_url": stock_data_url + "5_us_txt.zip"
}
