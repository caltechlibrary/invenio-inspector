# =============================================================================
# @file    test_cli.py
# @brief   Py.test cases for module command-line interface
# @created 2022-08-17
# @license Please see the file named LICENSE in the project directory
# @website https://github.com/caltechlibrary/invenio-inspector
# =============================================================================

import plac


def test_usage_help(capsys):
    from invenio-inspector.__main__ import main
    with plac.Interpreter(main) as i:
        i.check('-h', '')
