#!/usr/bin/env python


hexstr="636861726c6579206c6f766573206865696469"
print ''.join(chr(int(hexstr[i:i+2],16)) for i in range(0,len(hexstr),2))
