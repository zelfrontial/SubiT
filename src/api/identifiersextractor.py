__all__ = ['extract_identifiers']


def extract_identifiers(title, query):
    """
    Extracts any string from query that is not part of the title. 

    >>> from title import MovieTitle, SeriesTitle
    >>> title = MovieTitle("The Matrix", 1999)
    >>> extract_identifiers(title, "The.Matrix.1999.720p.HDDVD.DTS.x264-ESiR")
    ['720p', 'hddvd', 'dts', 'x264', 'esir']
    >>> extract_identifiers(title, "The.Matrix.1999")
    []
    >>> extract_identifiers(title, "The.Matrix")
    []
    >>> extract_identifiers(title, "720p.HDDVD.DTS")
    ['720p', 'hddvd', 'dts']
    >>> title = SeriesTitle("The Big Bang Theory", 5, 13, "tt2139151", \
    "The Recombination Hypothesis", 2012, "tt0898266")
    >>> extract_identifiers(\
    title, "the.big.bang.theory.s05e13.720p.hdtv.x264-orenji")
    ['720p', 'hdtv', 'x264', 'orenji']
    >>> title = SeriesTitle("The Big Bang Theory", 1, 4, "tt1091291", \
    "The Luminous Fish Effect", 2007, "tt0898266")
    >>> extract_identifiers(title, \
    "The.Big.Bang.Theory.1x04.The.Luminous.Fish.Effect.720p.HDTV.x264.AC3-CTU")
    ['720p', 'hdtv', 'x264', 'ac3', 'ctu']
    """
    pass