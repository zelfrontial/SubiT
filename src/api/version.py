""" 
Implementation of the Version classes. This package is not responsible for 
resolving the Version from arbitrary string input and such. It simply the 
implementation of Versions.

Users of this package will implement the methods for extracting the required 
info for the Version.
"""

__all__ = ['Version', 'ProviderVersion', 'UKNOWN_NUM_OF_CDS']

from exceptions import InvalidTitleValue
from exceptions import InvalidNumOfCDs
from exceptions import InvalidProviderValue
from exceptions import InvalidRankValue
from exceptions import InvalidLanguageValue


UKNOWN_NUM_OF_CDS = 0

class Version(object):
    def __init__(self, identifiers, title, num_of_cds = UKNOWN_NUM_OF_CDS):
        """
        A version is instantiated with an identifiers list that can be and 
        empty list, a title that must be valid, and an optional num_of_cds
        value that defaults to unknown, and cannot be lower than 0.

        >>> Version(["720p", "dts", "lol"], None, 1)
        Traceback (most recent call last):
            ...
        InvalidTitleValue: Title instance must be provided.

        >>> from title import MovieTitle
        >>> title = MovieTitle("The Matrix")
        >>> Version(["720p", "dts", "lol"], title, -1)
        Traceback (most recent call last):
            ...
        InvalidNumOfCDs: num_of_cds cannot be lower than 0.

        >>> print Version(["720p", "dts", "lol"], title, 1)
        <Version ...>
        """
        if not title:
            raise InvalidTitleValue("Title instance must be provided.")
        if num_of_cds < 0:
            raise InvalidNumOfCDs("num_of_cds cannot be lower than 0.")

        self.identifiers    = identifiers
        self.title          = title
        self.num_of_cds     = num_of_cds

    def __str__(self):
        return repr(self)

    def __repr__(self):
        """
        >>> from title import MovieTitle
        >>> title = MovieTitle("The Matrix")
        >>> print Version(["720p", "dts", "lol"], title, 0)
        <Version identifiers=['720p', 'dts', 'lol'], num_of_cds=0, \
        title=<MovieTitle ...>>
        >>> print Version([], title, 3)
        <Version identifiers=[], num_of_cds=3, title=<MovieTitle ...>>
        """
        return "<{cls} identifiers={identifiers}, num_of_cds={num_of_cds}, "\
            "title={title}>".format(
                cls='Version',
                identifiers=self.identifiers,
                num_of_cds=self.num_of_cds,
                title=repr(self.title)
            )


class ProviderVersion(Version):
    def __init__(
        self, identifiers, title, language, provider, version_string = "", 
        attributes = {}, is_certain_match = False, rank = 0, num_of_cds = 0):
        """
        Create a new instance of ProviderVersion. The rules includes all the
        Version's rules, and also, a provider instance must be supplied. The 
        rank value should be between 0 to 100. 

        >>> from title import MovieTitle
        >>> title = MovieTitle("The Matrix")

        >>> ProviderVersion([], title, object(), object())
        Traceback (most recent call last):
            ...
        InvalidLanguageValue: language instance must be supplied.

        >>> from languages import Languages
        >>> lang = Languages.HEBREW
        >>> ProviderVersion([], title, lang, None)
        Traceback (most recent call last):
            ...
        InvalidProviderValue: provider instance must be supplied.

        >>> ProviderVersion([], title, lang, object(), rank=-1)
        Traceback (most recent call last):
            ...
        InvalidRankValue: rank value must be between 0 to 100.

        >>> print ProviderVersion([], title, lang, object(), rank=50)
        <ProviderVersion ...>
        """

        Version.__init__(self, identifiers, title, num_of_cds)

        from languages import Languages
        if not isinstance(language, Languages.Language):
            raise InvalidLanguageValue("language instance must be supplied.")
        if not provider:
            raise InvalidProviderValue("provider instance must be supplied.")

        self.rank               = rank
        self.provider           = provider
        self.language           = language
        self.attributes         = attributes
        self.version_string     = version_string
        self.is_certain_match   = is_certain_match
        
    @property
    def rank_group(self):
        """
        >>> from title import MovieTitle
        >>> title = MovieTitle("The Matrix")
        >>> from languages import Languages
        >>> lang = Languages.HEBREW        
        >>> ver = ProviderVersion([], title, lang, object(), rank=0)
        >>> ver.rank_group == 1
        True
        >>> ver.rank = 61
        >>> ver.rank_group == 7
        True
        >>> ver.rank = 100
        >>> ver.rank_group == 10
        True
        """
        return self._rank_group

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        if value < 0 or value > 100:
            raise InvalidRankValue("rank value must be between 0 to 100.")
        self._rank = value
        # Set the group also.
        if value == 0:
            self._rank_group = 1
        else:
            import math
            self._rank_group = int(math.ceil((value/100.0) * 10))


    def __repr__(self):
        """
        >>> from title import MovieTitle
        >>> title = MovieTitle("The Matrix")
        >>> from languages import Languages
        >>> lang = Languages.HEBREW        
        >>> print ProviderVersion([], title, lang, object(), rank=0)
        <ProviderVersion identifiers=[], title=<MovieTitle ...>, \
        language=<...>, provider=<...>, version_string='', attributes={...},  \
        num_of_cds=0, rank=0, rank_group=1, is_certain_match=False>
        """
        return \
            "<{cls} identifiers={identifiers}, title={title}, "\
            "language={language}, provider={provider}, "\
            "version_string='{version_string}', attributes={attributes}, "\
            "num_of_cds={num_of_cds}, rank={rank}, rank_group={rank_group}, "\
            "is_certain_match={is_certain_match}>".format(
                cls='ProviderVersion',
                identifiers=self.identifiers,
                title=repr(self.title),
                language=repr(self.language),
                provider=repr(self.provider),
                version_string=self.version_string,
                attributes=str(self.attributes),
                num_of_cds=self.num_of_cds,
                rank=self.rank,
                rank_group=self.rank_group,
                is_certain_match=self.is_certain_match
            )