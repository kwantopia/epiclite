import types

dict_var = {'a': 1, 'c': {'d': {'e': 4}}, 'b': {'a': 2, 'b': 3}}

output = []
def decompose(dict_var, output):
  for key, val in dict_var.iteritems():
    if type(val) == types.DictType:
      decompose(val, output)

    else:
      output.append((key, val))
  return output

print decompose(dict_var, output)
