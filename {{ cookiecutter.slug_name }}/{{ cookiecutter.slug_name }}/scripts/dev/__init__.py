# -*- coding: utf-8 -*-
"""Development entrypoints"""

import {{ cookiecutter.slug_name }}

def ipython():
    from IPython import embed

    print(globals())

    embed()
