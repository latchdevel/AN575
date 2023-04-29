/* ===========================================================================
IEEE-754 to Microchip AN575 Float conversion
Robert (RKnapp) 2008
https://www.ccsinfo.com/forum/viewtopic.php?p=95055
============================================================================*/

#define uchar unsigned char
#include <stdio.h>

int main(void)
{
    // Local data:
    union
    {
        float IEEE_Float;
        uchar uBytes[4];
    } uF;

    float infloat;
    uchar tempchar_sbit;

    // Procedure:
    printf("\n test_1: Test IEEE to Microchip Float conversion: \n");

    while (1)
    {

        printf("\n Enter a float >>");
        scanf("%f", &infloat);

        uF.IEEE_Float = infloat;

        printf("\nFloat %f IEEE-754 bytes  [3..0] are %X %X %X %X ", infloat,
               uF.uBytes[3], uF.uBytes[2], uF.uBytes[1], uF.uBytes[0]);

        // CONVERT IEEE-754 to Microchip:
        tempchar_sbit = uF.uBytes[3] & 0x80; // get IEEE sign bit -- resides in bit 31
        uF.uBytes[3] *= 2;                   // one shift left (drags in a zero on the right)
        if (uF.uBytes[2] & 0x80)             // if bit 23 is set,
        {
            uF.uBytes[3] |= 0x01;           // set bit 24 (else it will remain cleared)
            uF.uBytes[2] &= 0x7F;           // clear bit 23
        };
        if (tempchar_sbit)                  // if IEEE sign bit was set,
            uF.uBytes[2] |= 0x80;           // set bit 23 (else, leave it cleared)

        printf("\nFloat %f Microchip bytes [3..0] are %X %X %X %X ", infloat,
               uF.uBytes[3], uF.uBytes[2], uF.uBytes[1], uF.uBytes[0]);

        // CONVERT Microchip to IEEE-754:
        tempchar_sbit = uF.uBytes[2] & 0x80; // get Microchip sign bit -- resides in bit 23
        uF.uBytes[2] &= 0x7F;                // clear bit 23
        if (uF.uBytes[3] & 0x01)             // if bit 24 is set,
            uF.uBytes[2] |= 0x80;            // set bit 23 (else, leave it cleared)
        uF.uBytes[3] /= 2;                   // one shift right (drags in a zero on the left)
        if (tempchar_sbit)                   // if Microchip sign bit was set,
            uF.uBytes[3] |= 0x80;            // set bit 31 (else, leave it cleared)

        printf("\nFloat %f Microchip bytes [3..0] --> %X %X %X %X (converted BACK to IEEE-754)", infloat,
               uF.uBytes[3], uF.uBytes[2], uF.uBytes[1], uF.uBytes[0]);
    }
}
