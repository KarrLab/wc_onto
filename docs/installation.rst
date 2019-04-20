Installation
============

Prerequisites
--------------------------

* Python
* Pip

Installing the ontology for use in Python
-----------------------------------------
1. Install this Python package with pip::

    pip install git+https://github.com/KarrLab/wc_onto.git#egg=wc_onto[all]

  This command will install this Python package, including the ontology (in OBO format) and the Python code for using the ontology. Once installed, the ontology will be located at ``pkg_resources.resource_filename('wc_onto', 'onto.obo')``.

2. Obtain a `BioPortal API key <http://bioportal.bioontology.org/>`_
3. Save your BioPortal API key to a configuration file (``~/.wc/wc_onto.cfg``)::

    [wc_onto]
        [[bioportal]]
            key = <BioPortal API key>
        
4. Import the package. The other ontologies which wc_onto references will automatically be downloaded the first time that the package is imported.::

    from wc_onto import onto

Downloading the ontology 
------------------------
Alternatively, the ontology can be downloaded (in OBO format) from GitHub or BioPortal

* Download `latest revision <https://raw.githubusercontent.com/KarrLab/wc_onto/master/wc_onto/onto.obo>`_ from GitHub
* Download `latest snapshot <https://bioportal.bioontology.org/ontologies/WC>`_ from BioPortal
