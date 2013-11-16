# -*- coding: utf-8 -
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.
import os

version_info = (18, 0)
__version__ = ".".join([str(v) for v in version_info])
SERVER_SOFTWARE = os.getenv("SERVER_SOFTWARE", "gunicorn/%s" % __version__)
