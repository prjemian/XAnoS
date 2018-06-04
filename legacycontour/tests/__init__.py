from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six

import difflib
import os

from matplotlib.testing import setup


# Check that the test directories exist
if not os.path.exists(os.path.join(
        os.path.dirname(__file__), 'baseline_images')):
    raise IOError(
        'The baseline image directory does not exist. '
        'This is most likely because the test data is not installed. '
        'You may need to install legacycontour from source to get the '
        'test data.')


