# -*- coding: utf-8 -*-
"""Development entrypoints"""

import {{ cookiecutter.slug_name }} # noqa: F401


def ipython():
    """Enter IPython console"""

    from IPython import embed

    print(globals())

    embed()
