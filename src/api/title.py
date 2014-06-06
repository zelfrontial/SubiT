class Title(object):
    """ The base Title object. """
    def __init__(self, name, year = 0, imdb_id = ""):
        self.name       = name
        self.year       = year
        self.imdb_id    = imdb_id
        from namenormalization import normalize_name
        self.normalized_names = normalize_name(self.name)
        self.normalized_names_set = set(self.normalized_names)

    def __eq__(self, other):
        # When imdb_id is not empty, and equals.
        if self.imdb_id and self.imdb_id == other.imdb_id:
            return True
        # Even if the year is empty.
        elif self.year == other.year:
            intersection = self.normalized_names_set.intersection(
                other.normalized_names_set)
            if intersection:
                return True
        return False
        
class MovieTitle(Title):
    """ Title object for movies. """
    def __init__(self, name, year = 0, imdb_id = ""):
        Title.__init__(self, name, year, imdb_id)

class SeriesTitle(Title):
    """ Title object for series. """
    def __init__(self, name, season_number, episode_number, year = 0, 
                 imdb_id = "", episode_name = ""):

        Title.__init__(self, name, yaer, imdb_id)
        self.episode_name   = episode_name
        self.season_number  = season_number
        self.episode_number = episode_number
        from namenormalization import normalize_name
        self.episode_normalized_names = normalize_name(self.episode_name)
        self.episode_normalized_names_set = set(self.episode_normalized_names)
