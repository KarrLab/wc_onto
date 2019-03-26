""" Test of wc_onto.core

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

from wc_onto import core
import pronto
import unittest
import wc_onto


class CoreTestCase(unittest.TestCase):

    def test(self):
        self.assertIsInstance(core.onto, pronto.Ontology)
