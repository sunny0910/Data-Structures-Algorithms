#FunctionManagerHashMapx
class Function:
    def __init__(self, name, argumentTypes, isVariadic) -> None:
        self.name = name
        self.argumentTypes = argumentTypes
        self.isVariadic = isVariadic
    
    def __repr__(self) -> str:
        return self.name

import collections
class FunctionLibrary:
    def __init__(self) -> None:
        self.variadic_map = collections.defaultdict(list)
        self.non_variadic_map = collections.defaultdict(list)
    
    def register(self, functions):
        for function in functions:
            if function.isVariadic:
                self.variadic_map[tuple(function.argumentTypes)].append(function)
            else:
                self.non_variadic_map[tuple(function.argumentTypes)].append(function)
    
    def find_matches(self, argument_types):
        non_variadic_matches = self.non_variadic_map.get(tuple(argument_types), [])
        variadic_matches = self._get_variadic_matches(argument_types)
        
        return non_variadic_matches + variadic_matches
    
    def _get_variadic_matches(self, argument_types):
        matches = []
        for i in range(len(argument_types)-1, -1, -1):
            matches.extend(self.variadic_map.get(tuple(argument_types[:i+1]), []))
        
        return matches

fl = FunctionLibrary()
func_a = Function("func_a", ["String", "Integer", "Integer"], False)
func_b = Function("func_b", ["String", "Integer"], True)
func_c = Function("func_c", ["Integer"], True)
func_d = Function("func_d", ["Integer", "Integer"], True)
func_e = Function("func_e", ["Integer", "Integer", "Integer"], False)
func_f = Function("func_f", ["String"], False)
func_g = Function("func_g", ["Integer"], False)

fl.register([func_a, func_b, func_c, func_d, func_e, func_f, func_g])
print(fl.find_matches(["String"]))
print(fl.find_matches(["Integer"]))
print(fl.find_matches(["Integer", "Integer", "Integer", "Integer"]))
print(fl.find_matches(["Integer", "Integer", "Integer"]))
print(fl.find_matches(["String", "Integer", "Integer", "Integer"]))
print(fl.find_matches(["String", "Integer", "Integer"]))