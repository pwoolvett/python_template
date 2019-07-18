# -*- coding: utf-8 -*-
"""Several path-related utilities."""

from pathlib import Path
from typing import Union


def nth_parent(src: Union[str, Path], n_times: int = 1) -> Path:
    """Ascend in the `src` path, `n_times`

    Args:
        src ( Union[str, Path]): Original path.
        n_times (int, optional): How many parents to walkt to. Defaults to 1.

    Returns:
        The n-th ancestor to path (or the root folder if the hierarchy
            tree is smaller than `n_times`).

    """
    if n_times == 0:
        return src.resolve()  # type: ignore

    try:
        parent = src.parent  # type: ignore
    except AttributeError:
        parent = Path(src).parent

    return nth_parent(parent, n_times - 1)
