# -*- coding: utf-8 -*-
"""Allow to be executable through `python -m ctdata_sots_cli`."""
from __future__ import absolute_import

from .cli import main

if __name__ == "__main__":  # pragma: no cover
        main(prog_name="sots")