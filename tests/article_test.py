
import unittest

from app.models import Articles

class ArticleTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Article class
    """
    def Setup(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('Russia invades Ukraine: Live updates - CNN','https://cdn.cnn.com/cnnnext/dam/assets/220226193325-03-ukraine-kyiv-022622-super-tease.jpg','A battle is underway for control of Ukraine`s capital, Kyiv. The US has warned Russia is seeking to encircle the city, and a Ukrainian official said it has been hit by missiles. Follow here for live news updates from the ground in Ukraine.',
                                    'US Ambassador to the United Nations Linda Thomas-Greenfield said Sunday that sanctions on Russias energy sector are not yet off the table as the US continues to punish the county for its invasion of … [+1324 chars]',
                                    '2022-02-27T16:41:00Z','https://www.reuters.com/world/europe/war-dividing-russian-ukrainian-brothers-billionaire-fridman-says-2022-02-27/')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))    
    
    
    # def test_init(self):
    #     """
    #     Test to check if object has been initialized correctly
    #     """
    #     self.assertEqual(self.new_article.title, 'Russia invades Ukraine: Live updates - CNN')   
    #     self.assertEqual(self.new_article.urlToImage,'https://cdn.cnn.com/cnnnext/dam/assets/220226193325-03-ukraine-kyiv-022622-super-tease.jpg')
    #     self.assertEqual(self.new_article.description, 'A battle is underway for control of Ukraine`s capital, Kyiv. The US has warned Russia is seeking to encircle the city, and a Ukrainian official said it has been hit by missiles. Follow here for live news updates from the ground in Ukraine.')
    #     self.assertEqual(self.new_article.content,'US Ambassador to the United Nations Linda Thomas-Greenfield said Sunday that sanctions on Russias energy sector are not yet off the table as the US continues to punish the county for its invasion of … [+1324 chars]')
    #     self.assertEqual(self.new_article.publishedAt,'2022-02-27T16:41:00Z')
    #     self.assertEqual(self.new_article.url,'https://www.reuters.com/world/europe/war-dividing-russian-ukrainian-brothers-billionaire-fridman-says-2022-02-27/')     
        
             
        