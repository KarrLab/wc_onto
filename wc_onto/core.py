""" wc_onto

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

import wc_onto.config.core
import os
import pkg_resources
import pronto
import requests

bio_portal_api_key = wc_onto.config.core.get_config()['wc_onto']['bioportal']['key']

DEPENDENT_ONTOLOGIES = {
    'BRO': {
        'url': 'http://data.bioontology.org/ontologies/BRO/download',
        'format': 'owl',
        'params': {
            'headers': {'Authorization': 'apikey token=' + bio_portal_api_key},
        },
    },
    'COMODI': {
        'url': 'https://raw.githubusercontent.com/binfalse/COMODI/master/ontology/comodi.owl',
        'format': 'owl',
    },
    'KISAO': {
        'url': 'http://svn.code.sf.net/p/kisao/code/tags/kisao-owl-latest/kisao_full.owl',
        'format': 'owl',
    },
    'MATR': {
        'url': 'http://data.bioontology.org/ontologies/MATR/download',
        'format': 'owl',
        'params': {
            'headers': {'Authorization': 'apikey token=' + bio_portal_api_key},
        },
    },
    'SBO': {
        'url': 'http://www.ebi.ac.uk/sbo/exports/Main/SBO_OBO.obo',
        'format': 'obo',
    },
    'SEPIO': {
        'url': 'https://raw.githubusercontent.com/monarch-initiative/SEPIO-ontology/master/src/ontology/sepio.owl',
        'format': 'owl',
    },
}
DEPENDENT_ONTOLOGIES_DIR = pkg_resources.resource_filename('wc_onto', 'ontologies')


def get_dependent_ontologies(ontologies=DEPENDENT_ONTOLOGIES, dir=DEPENDENT_ONTOLOGIES_DIR):
    """ Download dependent ontologies 

    Args:
        ontologies (:obj:`dict`, optional): dictionary that maps ids of ontologies to information about where to obtain them
        dir (:obj:`str`, optional): directory to save ontology
    """
    if not os.path.isdir(dir):
        os.makedirs(dir)

    for id, source in ontologies.items():
        get_ontology(id, source, dir=dir)


def get_ontology(id, source, dir=DEPENDENT_ONTOLOGIES_DIR):
    """ Download ontology to disk

    Args:
        id (:obj:`str`): id of ontology
        source (:obj:`dict`): information about source (URL, format) of ontology
        dir (:obj:`str`, optional): directory to save ontology
    """
    path = os.path.join(dir, id + '.' + source['format'])
    if os.path.isfile(path):
        return

    params = source.get('params', {})
    response = requests.get(source['url'], **params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


get_dependent_ontologies()

onto = pronto.Ontology(pkg_resources.resource_filename(
    'wc_onto', os.path.join('onto.obo')))
# :obj:`pronto.Ontology`: whole-cell modeling ontology
