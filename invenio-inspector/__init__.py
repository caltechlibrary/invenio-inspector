'''
__init__.py for invenio-inspector

Copyright
---------

Copyright (c) 2022 by the California Institute of Technology.  This code
is open-source software released under a BSD-type license.  Please see the
file "LICENSE" for more information.
'''

# Package metadata
# .............................................................................
#
#  ╭────────────────────── Notice ── Notice ── Notice ─────────────────────╮
#  |    The following values are automatically updated at every release    |
#  |    by the Makefile. Manual changes to these values will be lost.      |
#  ╰────────────────────── Notice ── Notice ── Notice ─────────────────────╯

__version__     = '0.0.0'
__description__ = 'CLI tool to list stuff about an invenio installation'
__url__         = 'https://github.com/caltechlibrary/invenio-inspector'
__author__      = 'Mike Hucka'
__email__       = 'helpdesk@library.caltech.edu'
__license__     = 'https://data.caltech.edu/license'


# Miscellaneous utilities.
# .............................................................................

def print_version():
    print(f'{__name__} version {__version__}')
    print(f'Authors: {__author__}')
    print(f'URL: {__url__}')
    print(f'License: {__license__}')
