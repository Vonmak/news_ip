import unittest
from app.models import News, Source

class SourceTest(unittest.TestCase):
    '''
    Test class to test the behavior of the source class.
    '''

    def setUp(self):
        '''
        set up method that will run before every test 
        '''
        self.new_source=Source("abc","Abc news","https://www.aljazeera.com/news/")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Ryan Hog','Millions of bee die!','The $48,000 shipment carrying 800 pounds.','Millions of bees bound for Alaska died on a Delta Air Lines flight after the plane was left on the tarmac in Atlanta.','https://www.businessinsider.com/millions-bees-died-atlanta-after-delta-rerouted-alaska-bound-jet-2022-4','https://i.insider.com/626cf67986fa90001905ed1f?width=1200&format=jpeg','2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()