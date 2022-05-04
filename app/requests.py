import urllib.request,json
from .models import News, Source

# Getting api key
api_key = None
# Getting the sources base url
source_url = None
# Getting the articles base url
base_url = None

def configure_request(app):
    global api_key,source_url, base_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['SOURCE_BASE_URL']
    base_url = app.config['NEWS_API_BASE_URL']
   

def get_sources():
    '''
    Function that gets the json response to our url request
    '''

    get_sourceurl = source_url.format(api_key)
    with urllib.request.urlopen(get_sourceurl) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        source_results=None 

        if get_sources_response['sources']:
            source_result_list=get_sources_response['sources']
            source_results=process_results(source_result_list)



    return source_results


def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects
    Args:
        source_list: A list of dictionaries that contain source details
    Returns :
        source_results: A list of source objects
    '''
    source_results= []

    for source_items in source_list:
        id=source_items.get('id')
        name=source_items.get('name')
        url=source_items.get('url')
        
        new_source=Source(id,name,url)

        source_results.append(new_source)

    return source_results


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_articles = None

        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)

    return news_articles

def process_articles(news_list):
    '''
    Function  that processes the news articles and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_item in news_list:
        
        title = news_item.get('title')
        author = news_item.get('author')
        description = news_item.get('description')
        content = news_item.get('content')
        url = news_item.get('url')
        urlToImage = news_item.get('urlToImage')
        publishedAt = news_item.get("publishedAt")
        

       
        news_object = News(title, author, description, content, url, urlToImage, publishedAt)
        news_articles.append(news_object)

    return news_articles


