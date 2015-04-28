import click, urllib2, json

class Movie:
    @classmethod
    def Load_JSON(Movie, data, get_plot):
        movie = Movie()
        if data[u'Response'] == 'True':
            movie.title = data[u'Title']
            if get_plot:
                movie.plot = data[u'Plot']
            movie.runtime = int(data[u'Runtime'].split()[0])
            movie.metascore = data[u'Metascore']
            movie.imdb_rating = data[u'imdbRating']
            movie.imdb_votes = data[u'imdbVotes']
            return movie

        return None

    def __str__(self):
        string = ''
        string += 'Title: {0}\n\n'.format(self.title)

        if hasattr(self, 'plot'):
            string += 'Plot: {0}\n\n'.format(self.plot)

        string += 'Runtime: {0}hrs {1}mins\n'.format(self.runtime//60, self.runtime%60)
        string += 'Metascore: {0}\n'.format(self.metascore)
        string += 'imdb rating: {0}\n'.format(self.imdb_rating)
        string += 'imdb votes: {0}\n'.format(self.imdb_votes)
        return string

@click.command()
@click.argument('search', metavar='movie_name')
@click.option('--plot', is_flag=True, help='show plot')
def smibbler(search, plot):
    """ Print info fetched from omdbapi.com """

    # generate search string and fetch data
    query = search.replace(' ', '+')
    request = 'http://www.omdbapi.com/?t={0}&y=&plot=short&r=json'.format(query)
    res = urllib2.urlopen(request)
    data = json.load(res)

    movie = Movie.Load_JSON(data, plot)
    if movie is None:
        click.echo('Movie not found')
    else:
        click.echo(movie)

