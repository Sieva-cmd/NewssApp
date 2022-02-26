class News_source:
    def __init__(self,name,description,url):
    
        self.name =name
        self.description =description
        self.url =url
        


class Articles:
    """
    News class to define News objects
    """
    
    def __init__(self,title,urlToImage,description,publishedAt,url):
        self.title =title
        self.urlToImage =urlToImage
        self.description =description
        self.publishedAt =publishedAt
        self.url =url
        
class Search:
    def __init__(self,title,description,content) -> None:
        pass        
        