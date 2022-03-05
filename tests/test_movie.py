import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    def setUp(self):
        self.new_movie = Movie(5786, 'Breaking Bad','If bad had a limit, would it break','https://image.tmdb.org/t/p/w500/khsjha27hbs',9.665,15689)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))

if __name__ == '__main__':
    unittest.main()