"""
Converts Microchip's 32/24-bit float formats as described in Application Note AN575.

See: https://github.com/latchdevel/AN575

Copyright (c) 2023 Jorge Rivera. All right reserved.
License GNU Lesser General Public License v3.0.
"""

from struct import pack as _pack, unpack as _unpack

def FloatToAN575(number):
    """
    Convert a number to Microchip's 32/24-bit float format described in AN575.

    Param is an any format number.
    Returns a bytes object (4 bytes big endian) or an error string on failure.
    """

    # Check for a valid input
    try:
        f = float(number)
    except Exception as err: 
        return "Error: {}.".format(err)

    # Extract IEEE-754 bytes (32 bits, big endian)
    try:
        IEEE_bytes = _pack("!f",f)
    except Exception as err:
        return "Error: {}.".format(err)

    # Convert from IEEE-754 to Microchip AN575 float format:
    AN575_bytes = bytearray(IEEE_bytes)

    sign_bit = AN575_bytes[0] & 0x80            # get IEEE sign bit -- resides in bit 31 
    AN575_bytes[0] = AN575_bytes[0]<<1 & 0xFF   # one shift left (drags in a zero on the right)

    if ( AN575_bytes[1] & 0x80 ):               # if bit 23 is set,
         AN575_bytes[0] |= 0x01                 # set bit 24 (else it will remain cleared)
         AN575_bytes[1] &= 0x7F                 # clear bit 23
    
    if ( sign_bit ):                            # if IEEE sign bit was set,
        AN575_bytes[1]  |= 0x80                 # set bit 23 (else, leave it cleared)

    return bytes(AN575_bytes)


def AN575ToFloat(byte0, byte1, byte2, byte3 = 0):
    """
    Convert a Microchip's 32/24 bits float format to standard IEEE-754 32-bit float number.

    Params are three or four bytes (big endian) of AN575 float format number.
    Returns a standard float number or an error string on failure.
    """

    # Get Microchip AN575 bytes (32/24 bits, big endian)
    try:
        AN575_bytes = bytearray([byte0, byte1, byte2, byte3])
    except Exception as err:
        return "Error: {}.".format(err)

    # Convert from Microchip AN575 float format to IEEE-754:
    sign_bit = AN575_bytes[1] & 0x80                 # get Microchip sign bit -- resides in bit 23
    AN575_bytes[1] &= 0x7F                           # clear bit 23
    
    if ( AN575_bytes[0] &  0x01 ):                   # if bit 24 is set,
         AN575_bytes[1] |= 0x80                      # set bit 23 (else, leave it cleared)
    
    AN575_bytes[0] = AN575_bytes[0] >> 1 & 0xFF      # one shift right (drags in a zero on the left)
            
    if ( sign_bit ):                                 # if Microchip sign bit was set,
        AN575_bytes[0] |= 0x80                       # set bit 31 (else, leave it cleared)

    # Make IEEE-754 float (32 bits)
    try:
        IEEE_754 = _unpack("!f",AN575_bytes)[0]
    except Exception as err:
        return "Error: {}.".format(err)

    return float(IEEE_754)
