import unittest
import index

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.app = index.app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
	    rv = self.app.get('/')
        assert b'Rock Climbing' in rv.data
        
    def test_link_to_my_page(self):
        rv = self.app.get('/Gear')  
        assert b'Shoes' in rv.data 

    def test_my_topic(self):
        rv = self.app.get('/Gear/Shoes')  
        assert b'La Sportiva' in rv.data 

if __name__ == '__main__':

    unittest.main()
