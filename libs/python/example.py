#!/usr/bin/env python

import postscriptbarcode

c=postscriptbarcode.BWIPP("../../build/monolithic_package/barcode.ps")
print c.get_version()

