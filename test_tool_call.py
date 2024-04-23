import ast
import json
import sys
import importlib
sys.path.append('tool_calling')

func_name = "get_tariffs"
args = {'customer_postcode': 'W6 8LT', 'energy_supplier': 'Octopus Energy Operations Limited', 'tariff_name': 'Flexible Octopus', 'yearly_spend': 973.21}



func = getattr(importlib.import_module(func_name), func_name)
res = func(**args)
print(res)