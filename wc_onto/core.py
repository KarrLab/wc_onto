""" wc_onto

:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2019-03-26
:Copyright: 2019, Karr Lab
:License: MIT
"""

import io
import os
import pkg_resources
import pronto
import pronto.utils.warnings
import requests
import urllib
import warnings
import wc_onto.config.core

config = wc_onto.config.core.get_config()['wc_onto']
BIO_PORTAL_API_KEY = config['bioportal']['key']
if 0 == len(BIO_PORTAL_API_KEY):
    raise ValueError(f"BIO_PORTAL_API_KEY not initialized")

DEPENDENT_ONTOLOGIES = {
    'BFO': {
        'url': 'http://purl.obolibrary.org/obo/bfo.owl',
        'format': 'owl',
    },
    'BRO': {
        'url': 'http://data.bioontology.org/ontologies/BRO/submissions/14/download',
        'params': {
            'headers': {'Authorization': 'apikey token=' + BIO_PORTAL_API_KEY},
        },
        'format': 'owl'
    },
    'COMODI': {
        'url': 'https://comodi.bio.informatik.uni-rostock.de/latest/comodi.owl',
        'format': 'owl',
    },
    'FOAF': {
        'url': 'http://data.bioontology.org/ontologies/FOAF/download?download_format=rdf',
        'params': {
            'headers': {'Authorization': 'apikey token=' + BIO_PORTAL_API_KEY},
        },
        'format': 'rdf',
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
        'url': 'http://data.bioontology.org/ontologies/MATR/submissions/1/download?download_format=rdf',
        'params': {
            'headers': {'Authorization': 'apikey token=' + BIO_PORTAL_API_KEY},
        },
        'format': 'rdf',
    },
    'SBO': {
        'url': 'http://purl.obolibrary.org/obo/sbo.owl',
        'format': 'owl',
    },
    'SEPIO': {
        'url': 'http://purl.obolibrary.org/obo/sepio.owl',
        'format': 'owl',
    },
}
DEPENDENT_ONTOLOGIES_DIR = config['cache_dir']


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

    session = requests.Session()
    parsed_url = urllib.parse.urlparse(source['url'])
    session.mount(parsed_url.scheme + '://' + parsed_url.netloc, requests.adapters.HTTPAdapter(max_retries=5))
    params = source.get('params', {})
    try:
        response = session.get(source['url'], **params)
    except requests.exceptions.ConnectionError:
        raise Exception('Unable to download dependent ontology {}'.format(id), UserWarning)

    if response.status_code >= 200 and response.status_code < 300:
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        raise Exception('Unable to download dependent ontology {}: {}: {}'.format(id, response.status_code, response.reason), UserWarning)


get_dependent_ontologies()

with warnings.catch_warnings():
    warnings.filterwarnings('ignore', message=r'unknown element in `owl:Class`', category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r'unknown element in `owl:ObjectProperty`', category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r'`owl:disjointWith` element without', category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r'cannot process plain `owl:AnnotationProperty`',
                            category=pronto.utils.warnings.NotImplementedWarning)
    warnings.filterwarnings('ignore', message=r'.*? no `xsd:datatype`', category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r'several names found', category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r"unknown axiom property: 'http:\/\/www\.w3\.org\/2000\/01\/rdf-schema#",
                            category=pronto.utils.warnings.SyntaxWarning)
    warnings.filterwarnings('ignore', message=r'unsound encoding', category=UnicodeWarning)

    filename = pkg_resources.resource_filename(
        'wc_onto', os.path.join('onto.obo'))

    cleaned_file = io.BytesIO()
    with open(filename, 'rb') as file:
        for line in file:
            cleaned_file.write(line.replace(b'\r', b'\n'))
    cleaned_file.seek(0)

    onto = pronto.Ontology(cleaned_file)
    # :obj:`pronto.Ontology`: whole-cell modeling ontology
