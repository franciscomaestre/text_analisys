#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.cache.aerospike_factory import AerospikeFactory
import json

aerospike = AerospikeFactory.getInstance(space='response_terms')

# aerospike.set('yyyy', {'data': 'datat'})

jsonResult = aerospike.get('th245yuradaererwerqwerj234234')

print jsonResult

# print json.dumps(json.loads(jsonResult['message']), sort_keys=True, indent=4, separators=(',', ': '))

# Close the connection to the Aerospike cluster
