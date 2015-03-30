from __future__ import unicode_literals

from .split import urisplit


def urijoin(base, ref, strict=False):
    """Convert a URI reference relative to a base URI to its target URI
    string.

    If `strict` is :const:`False`, a scheme in the reference is
    ignored if it is identical to the base URI's scheme.

    """
    if isinstance(base, type(ref)):
        return urisplit(base).transform(ref, strict).geturi()
    elif isinstance(base, bytes):
        return urisplit(base.decode()).transform(ref, strict).geturi()
    else:
        return urisplit(base).transform(ref.decode(), strict).geturi()
