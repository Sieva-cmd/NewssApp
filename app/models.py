class News_source:
    def __init__(self,name,description,url):
    
        self.name =name
        self.description =description
        self.url =url
        


class Articles:
    """
    News class to define News objects
    """
    
    def __init__(self,title,urlToImage,description,content,publishedAt,url):
        self.title =title
        self.urlToImage =urlToImage
        self.description =description
        self.content=content
        self.publishedAt =publishedAt
        self.url =url
        

        