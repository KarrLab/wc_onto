[//]: # ( [![PyPI package](https://img.shields.io/pypi/v/wc_onto.svg)](https://pypi.python.org/pypi/wc_onto) )
[![Documentation](https://readthedocs.org/projects/wc-onto/badge/?version=latest)](https://docs.karrlab.org/wc_onto)
[![Test results](https://circleci.com/gh/KarrLab/wc_onto.svg?style=shield)](https://circleci.com/gh/KarrLab/wc_onto)
[![Test coverage](https://coveralls.io/repos/github/KarrLab/wc_onto/badge.svg)](https://coveralls.io/github/KarrLab/wc_onto)
[![Code analysis](https://api.codeclimate.com/v1/badges/e7b017f281d0905620de/maintainability)](https://codeclimate.com/github/KarrLab/wc_onto)
[![License](https://img.shields.io/github/license/KarrLab/wc_onto.svg)](LICENSE)
![Analytics](https://ga-beacon.appspot.com/UA-86759801-1/wc_onto/README.md?pixel)

# WC-Onto

Ontology for whole-cell modeling

## Installation

### Installing the ontology for use in Python
This Python package can be installed with pip:
```
pip install git+https://github.com/KarrLab/wc_onto.git#egg=wc_onto[all]
```

This command will install this Python package, including the ontology (in OBO format) and the Python code for using the ontology. Once installed, the ontology will be located at ``pkg_resources.resource_filename('wc_onto', 'onto.obo')``.

### Downloading the ontology 
Alternatively, the ontology can be downloaded (in OBO format) from GitHub or BioPortal

* Download [latest revision](https://raw.githubusercontent.com/KarrLab/wc_onto/master/wc_onto/onto.obo) from GitHub
* Download [latest snapshot](https://bioportal.bioontology.org/ontologies/WC) from BioPortal

## Documentation
Please see the [API documentation](https://docs.karrlab.org/wc_onto).

## License
The package is released under the [MIT license](LICENSE).

## Development team
This package was developed by the [Karr Lab](https://www.karrlab.org) at the Icahn School of Medicine at Mount Sinai in New York, USA.

## Questions and comments
Please contact the [Karr Lab](https://www.karrlab.org) with any questions or comments.
