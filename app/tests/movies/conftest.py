import pytest

from movies.models import Movie

@pytest.fixture(scope='function')
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie
    return _add_movie

@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie_one = add_movie(title='The Big Lebowski', genre='comedy', year='1998')
    movie_two = add_movie(title='No Country for Old Men', genre='thriller', year='2007')
    resp = client.get(f'/api/movies/')
    assert resp.status_code == 200
    assert resp.data[0]['title'] == movie_one.title
    assert resp.data[1]['title'] == movie_two.title