class News_source:
    def __init__(self,id,name):
        self.id =id
        self.name =name
        


class Article:
    """
    News class to define News objects
    """
    
    def __init__(self,title,urlToImage,description,publishedAt,url):
        self.title =title
        self.urlToImage =urlToImage
        self.description =description
        self.publishedAt =publishedAt
        self.url =url
        