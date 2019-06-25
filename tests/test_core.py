""" Test of wc_onto.core

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

from wc_onto import core
import mock
import os
import pronto
import requests
import shutil
import tempfile
import unittest
import wc_onto


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        shutil.rmtree(self.tempdir)

    def tearDown(self):
        if os.path.isdir(self.tempdir):
            shutil.rmtree(self.tempdir)

    def test_import(self):
        self.assertIsInstance(core.onto, pronto.Ontology)

    def test_get_dependent_ontologies(self):
        core.get_dependent_ontologies(ontologies={
            'BRO': core.DEPENDENT_ONTOLOGIES['BRO'],
        }, dir=self.tempdir)
        core.get_dependent_ontologies(ontologies={
            'BRO': core.DEPENDENT_ONTOLOGIES['BRO'],
        }, dir=self.tempdir)

    def test_get_dependent_ontologies_warning(self):
        with self.assertWarnsRegex(UserWarning, 'Unable to download dependent ontology'):
            with mock.patch.object(requests.Session, 'get', side_effect=requests.exceptions.ConnectionError):
                core.get_ontology('test', {
                    'url': 'https://test.org/does_not_exist',
                    'format': 'owl',
                }, dir=self.tempdir)

        with self.assertWarnsRegex(UserWarning, 'Not ok'):
            with mock.patch.object(requests.Session, 'get', return_value=mock.Mock(status_code=300, reason='Not ok')):
                core.get_ontology('test', {
                    'url': 'https://test.org/does_not_exist',
                    'format': 'owl',
                }, dir=self.tempdir)
