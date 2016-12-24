from pycparser import c_ast, parse_file

c_to_python = {
    "double": "float",
    "void": "ffi.NULL",
    "char": "str",

}

HEADER = """from cffi import FFI
import os
# DO NOT EDIT THIS FILE
# AUTO-GENERATED BY scripts/bindings.py
ffi = FFI()
ffi.cdef('''
// paste actual header here''')
current = os.path.dirname(os.path.realpath(__file__))
if platform.system() == 'Linux':
    library = os.path.join(current, 'libui.so')
elif platform.system() == 'Darwin':
    library = os.path.join(current, 'libui.dylib')
elif platform.system() == 'Windows':
    library = os.path.join(current, 'libui.dll')
else:
    raise RuntimeError('Unsupported platform')
lib = ffi.dlopen(library)
callbacks = []
"""

FUNCTION_TEMPLATE = '''
def {fname}({args}):
    {extra}
    return lib.{fname}({pure_args})
'''

CHAR_TYPE_FUNCTION_TEMPLATE = '''
def {fname}({args}):
    {extra}
    return ffi.string(lib.{fname}({pure_args})).decode('utf-8')
'''
EXTRA_CALLBACK_TEMPLATE = '''ffi_callback = ffi.callback("{data}", callback)
    callbacks.append(ffi_callback) # make sure our ffi callback will be alive
'''

EXTRA_STR_TO_BYTES_TEMPLATE = '{name} = {name}.encode()\n    '

STRUCT_TEMPLATE = '''
def {sname}(*args):
    return ffi.new("{sname} *", args)
'''
import linecache


class PythonFunction:
    def __init__(self, args):
        self.rtype, self.name, self.params = args

    def generate_python(self):
        pure_arguments = []
        arguments = []
        extra = ''
        for param in self.params:
            name, type = param
            pure_name = name
            if pure_name in pure_arguments:
                # This is used to fix multiple arguments
                # With one name
                addit_info = str(pure_arguments.count(pure_name))
                pure_name = pure_name + addit_info
                name = name.replace(name, name + addit_info)
            if type == 'char':
                # We need to convert Python 3 str to bytes
                # In order to pass it to libui
                extra += EXTRA_STR_TO_BYTES_TEMPLATE.format(name=name)

            if 'callback' in name:
                coord = name.split(",")[1]
                filename, lineno = coord.split(":")
                line = linecache.getline(filename, int(lineno))
                line = line.split(',', 1)[1].rsplit(',', 1)[0].strip()
                pure_name = 'ffi_callback'
                name = 'callback'
                extra += EXTRA_CALLBACK_TEMPLATE.format(data=line)
                type = 'void'
            if pure_name == "data":
                pure_name = 'ffi.NULL'
            # Get python type corresponding to C type
            py_type = c_to_python.get(type, type)
            # Pure arguments - for calling C library via CFFI
            pure_arguments.append(pure_name)
            # Arguments contain type hints
            arguments.append(name + ": " + py_type)
        pure_args = ', '.join(pure_arguments)
        args = ', '.join(arguments)
        # We need convert C char to Python str if lib returns it
        # Otherwise it won't work
        if self.rtype == 'char':
            print(CHAR_TYPE_FUNCTION_TEMPLATE.format(fname=self.name,
                                                     args=args,
                                                     extra=extra,
                                                     pure_args=pure_args))
        else:
            print(FUNCTION_TEMPLATE.format(fname=self.name,
                                           args=args,
                                           extra=extra,
                                           pure_args=pure_args))


class StructVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.structs = []

    def visit_Struct(self, struct: c_ast.Struct):
        name = struct.name
        print(STRUCT_TEMPLATE.format(sname=name))


class FuncDeclVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def traverse_callback(self, callback: c_ast.FuncDecl):
        params = self.traverse_params(callback.args)
        type = callback.type.type.names[0]
        return type, params

    def traverse_params(self, params_list: c_ast.ParamList):
        # List containing all params in a tuple : (arg name, type)
        all_params = []
        for param in params_list.params:
            callback = None
            if isinstance(param, c_ast.Typename):
                if isinstance(param.type.type, c_ast.IdentifierType):
                    continue
                arg = param.type.type
                arg.declname = str(param.type.type.type.names[0])
            # If it's a type declaration
            elif isinstance(param.type, c_ast.TypeDecl):
                arg = param.type
            # If it's a callback
            elif isinstance(param.type.type, c_ast.FuncDecl):
                # Traverse our callback
                arg = param.type.type.type
                callback = self.traverse_callback(param.type.type)

            # PtrDecl or TypeDecl are the same when you're creating
            # an ABI wrapper using CFFI
            elif isinstance(param.type, c_ast.PtrDecl):
                arg = param.type.type
            else:
                raise TypeError()
            # Only for debug (never happened to me)
            if not hasattr(arg, 'declname'):
                arg.show()
            # Append argument name and it's type
            if callback:
                # Append callback's params and types of them
                # We need coord to generate cdef for CFFI later
                all_params.append(("callback," + str(arg.coord), callback))
            else:
                all_params.append((arg.declname, arg.type.names[0]))
        return all_params

    def visit_FuncDecl(self, node: c_ast.FuncDecl):

        if isinstance(node.type, c_ast.TypeDecl):
            type_obj = node.type

        elif isinstance(node.type.type, c_ast.TypeDecl):
            type_obj = node.type.type

        else:
            # Just in case
            raise TypeError()

        func_name = type_obj.declname

        type = type_obj.type.names[0]
        all_params = self.traverse_params(node.args)
        self.functions.append((type, func_name, all_params))


def show_func_defs(filename):
    ast = parse_file(filename)
    funcs_visitor = FuncDeclVisitor()
    funcs_visitor.visit(ast)
    structs_visitor = StructVisitor()
    structs_visitor.visit(ast)
    funcs = funcs_visitor.functions
    for func in funcs:
        f = PythonFunction(func)
        f.generate_python()


# You MUST precompile ui.h header in order to parse it
# Because otherwise it will contain includes, those are not
# always can be parsed by pycparser
# for example : gcc -E ui.h > ui_compiled.h
if __name__ == "__main__":
    filename = 'ui_compiled.h'
    print(HEADER)
    show_func_defs(filename)
