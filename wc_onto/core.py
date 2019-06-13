""" wc_onto

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

import os
import pkg_resources
import pronto
import requests

DEPENDENT_ONTOLOGIES = {
    'BFO': {
        'url': 'http://purl.obolibrary.org/obo/bfo.owl',
        'format': 'owl',
    },
    'BRO': {
        'url': 'http://purl.obolibrary.org/obo/bro.owl',
        'format': 'owl'
    },
    'COMODI': {
        'url': 'http://purl.obolibrary.org/obo/comodi.owl',
        'format': 'owl',
    },
    'FOAF': {
        'url': 'http://purl.obolibrary.org/obo/foaf.rdf',
        'format': 'owl',
    },
    'IAO': {
        'url': 'http://purl.obolibrary.org/obo/iao.owl',
        'format': 'owl',
    },
    'KISAO': {
        'url': 'http://purl.obolibrary.org/obo/kisao.owl',
        'format': 'owl',
    },
    'MATR': {
        'url': 'http://purl.obolibrary.org/obo/matr.owl',
        'format': 'owl',
    },
    'SBO': {
        'url': 'http://purl.obolibrary.org/obo/sbo.obo',
        'format': 'obo',
    },
    'SEPIO': {
        'url': 'http://purl.obolibrary.org/obo/sepio.owl',
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
