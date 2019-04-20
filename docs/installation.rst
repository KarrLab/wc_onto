Installation
============

Prerequisites
--------------------------

* Python
* Pip


Installing the ontology for use in Python
-----------------------------------------
This Python package can be installed with pip::

    pip install git+https://github.com/KarrLab/wc_onto.git#egg=wc_onto[all]

This command will install this Python package, including the ontology (in OBO format) and the Python code for using the ontology. Once installed, the ontology will be located at ``pkg_resources.resource_filename('wc_onto', 'onto.obo')``.

Downloading the ontology 
------------------------
Alternatively, the ontology can be downloaded (in OBO format) from GitHub or BioPortal

* Download `latest revision <https://raw.githubusercontent.com/KarrLab/wc_onto/master/wc_onto/onto.obo>`_ from GitHub
* Download `latest snapshot <https://bioportal.bioontology.org/ontologies/WC>`_ from BioPortal
