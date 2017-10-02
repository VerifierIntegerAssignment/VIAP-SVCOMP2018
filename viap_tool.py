#!/usr/bin/python

import sys
import viap_svcomp

for filename in sys.argv[1:]:
	viap_svcomp.prove_auto(filename)
