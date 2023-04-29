"""
Unit tests for AN575 Python module

See: https://github.com/latchdevel/AN575

Copyright (c) 2023 Jorge Rivera. All right reserved.
License GNU Lesser General Public License v3.0.
"""

import unittest

from AN575 import FloatToAN575, AN575ToFloat

testNumbers = [
    ( 0.0,                      [ 0x00, 0x00, 0x00, 0x00 ] ),
    ( 1.0,                      [ 0x7F, 0x00, 0x00, 0x00 ] ),
    ( 0.0,                      [ 0x00, 0x00, 0x00, 0x00 ] ),
    ( 1.0,                      [ 0x7F, 0x00, 0x00, 0x00 ] ),
    (-1.0,                      [ 0x7F, 0x80, 0x00, 0x00 ] ),
    ( 0.875,                    [ 0x7E, 0x60, 0x00, 0x00 ] ),
    ( 1.75,                     [ 0x7F, 0x60, 0x00, 0x00 ] ),
    ( 1.999969482421875,        [ 0x7F, 0x7F, 0xFF, 0x00 ] ),
    ( 1.9999998807907104,       [ 0x7F, 0x7F, 0xFF, 0xFF ] ),
    ( 1.1754943508222875e-38,   [ 0x01, 0x00, 0x00, 0x00 ] ), # smallest number above zero
    ( 3.4027717462407993e+38,   [ 0xFE, 0x7F, 0xFF, 0x00 ] ), # largest number 24-bit
    ( 3.4028234663852886e+38,   [ 0xFE, 0x7F, 0xFF, 0xFF ] ), # largest number 32-bit
    ( float('+inf'),            [ 0xFF, 0x00, 0x00, 0x00 ] ), # positive infinity
    ( float('-inf'),            [ 0xFF, 0x80, 0x00, 0x00 ] )  # negative infinity
]

class TestAN575Conversion(unittest.TestCase):

    def test_FloatToAN575(self):
        for testNumber in testNumbers:
            IEEE_float = testNumber[0]
            AN575_bytes = testNumber[1]
            with self.subTest("FloatToAN575({})".format(IEEE_float)):
                result = FloatToAN575(IEEE_float)
                self.assertEqual(result,bytes(AN575_bytes))

    def test_AN575ToFloat(self):
        for testNumber in testNumbers:
            IEEE_float = testNumber[0]
            AN575_bytes = testNumber[1]
            with self.subTest("AN575ToFloat({})".format(', '.join("0x{:02X}".format(byte) for byte in AN575_bytes))):
                result = AN575ToFloat(*AN575_bytes)
                self.assertEqual(result,IEEE_float)

if __name__ == '__main__':
    unittest.main()
