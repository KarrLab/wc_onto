import pkg_resources

# read version
with open(pkg_resources.resource_filename('wc_onto', 'VERSION'), 'r') as file:
    __version__ = file.read().strip()

from .core import onto
from .core import kb_onto
