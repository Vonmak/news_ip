class Source:
    '''
    Class that defines sources objects
    '''
    def __init__(self,id,name,url):
        self.id=id
        self.name=name
        self.url=url
      

class News:
    '''
    News class to define News Objects
    '''
    all_news = []

    def __init__(self,title, author, description, content, url, urlToImage, publishedAt):
        
        self.title = title
        self.author = author
        self.description =description
        self.content = content
        self.url = url
        self.urlToImage =urlToImage
        self.publishedAt = publishedAt
        