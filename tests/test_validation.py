# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import unittest

from idx_normalizator import normalize_idx


class TestValidation(unittest.TestCase):
    def test_normalize_idx(self):
        names = {
            "Example Cammel Name": "example-cammel-name",
        }
        for name, idx in names.items():
            nornalized = normalize_idx(name)
            self.assertEqual(nornalized, idx)


if __name__ == "__main__":
    unittest.main()
