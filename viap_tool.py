#!/usr/bin/python

import sys
import viap_svcomp



if sys.argv[1:] is ['-version']:
	print "1.0"

if sys.argv[1:] != [] and sys.argv[-1] is not None:
	filename=sys.argv[-1]	
	if len(sys.argv[1:])==1: 
		viap_svcomp.prove_auto(filename)
	elif len(sys.argv[1:])==2: 
		propertfile=sys.argv[-2]
		if '.prp' in property:
			viap_svcomp.prove_auto(filename,property)
		else:
			viap_svcomp.prove_auto(filename)	
	else:
		viap_svcomp.prove_auto(filename)

