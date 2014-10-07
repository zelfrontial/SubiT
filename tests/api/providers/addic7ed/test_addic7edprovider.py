import sys
sys.path.append("..\\..")
import os

from api.providers.addic7ed import provider as addic7edprovider
Addic7edProvider = addic7edprovider.Addic7edProvider
from api.requestsmanager import get_manager_instance
from api.languages import Languages
from api.title import MovieTitle
from api.title import SeriesTitle
from api.version import ProviderVersion
from api.version import Version

import unittest
import doctest

class TestAddic7edProvider(unittest.TestCase):
    def setUp(self):
        self.provider = Addic7edProvider(
            [Languages.ENGLISH], get_manager_instance("test_addic7ed_provider"))

    def test_get_titles_versions_series(self):
        """ Simple test to verify that we get version for series. """
        raise NotImplementedError()

    def test_get_titles_versions_movie_exact(self):
        """
        Simple test to verify that we get versions for movie. The query
        returns a single movie in the site.
        """
        title = MovieTitle("Godzilla", 2014, "tt0831387")
        fake_version = Version(["identifier"], title)

        titles_versions = self.provider.get_title_versions(title, fake_version)

        # Only single title is expected
        self.assertEqual(len(titles_versions), 1)
        # Only single language
        self.assertEqual(len(titles_versions[0][1]), 1)
        # Two versions (At rank group 1)
        versions = titles_versions[0][1][Languages.ENGLISH][1]
        self.assertEqual(len(versions), 2)

        self.assertEquals(versions[0].version_string, "BluRay_BRrip_BDrip")
        self.assertEquals(versions[1].version_string, "WEBRiP-VAiN")

        self.assertEquals(versions[0].addributes["movie_code"], "/movie/89128")
        self.assertEquals(versions[1].addributes["movie_code"], "/movie/89128")

        self.assertEquals(versions[0].addributes["version_code"], "/original/89128/4")
        self.assertEquals(versions[1].addributes["version_code"], "/original/89128/2")

    def test_get_subtitle_buffer(self):
        """
        Test that given some ProviderVersion, we manage to get the buffer of
        the subtitle.
        """
        raise NotImplementedError()


def run_tests():
    test_runner = unittest.TextTestRunner(verbosity=0)
    tests = doctest.DocTestSuite(
        addic7edprovider,
        optionflags=doctest.NORMALIZE_WHITESPACE)
    tests.addTests(
        unittest.defaultTestLoader.loadTestsFromTestCase(
            TestAddic7edProvider))
    test_runner.run(tests)