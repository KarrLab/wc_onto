""" wc_onto

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

import os
import pkg_resources
import pronto

onto = pronto.Ontology(pkg_resources.resource_filename(
    'wc_onto', os.path.join('onto.obo')))
# :obj:`pronto.Ontology`: whole-cell modeling ontology
