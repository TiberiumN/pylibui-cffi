# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses ctypes 
to interface with the libui shared library.

## Usage

```python    
from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):

    def on_close(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.margined = True
window.show()

app.start()
app.close()
```


## Build instructions

Clone pylibui:

    $ git clone https://github.com/joaoventura/pylibui

Clone [libui](https://github.com/andlabs/libui/) and build the shared library: 

    $ git clone https://github.com/andlabs/libui/
    $ cd libui
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make

The libui shared library will be inside libui/build/out. Copy the contents of out/ 
to pylibui/libui. Now, you can use pylibui:

    $ python3
    >>> import pylibui
## Binding generation
If you want to re-generate bindings for your platform or for newer version of libui,
you need to install 'pycparser'.

1. Pre-compile ui.h header to ui_compiled.h. For example: 

  ```gcc -E ui.h -o ui_compiled.h```

2. Run scripts/bindings.py. If there's any failures, send me an e-mail or fill an issue. For example:

  ```python3 bindings.py > lib.py```
  
  By default bindings.py prints Python code to stdout

3. Copy contents of cffi_header.h into ffi.cdef('''<paste into this string>''') (you can find it at the top of lib.py file)

4. Copy generated lib.py to pylibui/libui. I strongly recommend checking lib.py with any good IDE (PyCharm), because there's still some issues with auto binding generation - duplicate structs, uiInitOptions tries to convert char NULL to string, uiAllocControl is not needed, some structs may be missing (fill an issue if any).

## Run Tests

The tests are located in the `tests` folder. To run the entire test suite 
execute the following in the outer pylibui directory: 

    $ python3 -m unittest
    ..
    ----------------------------------------------------------------------
    Ran 39 tests in 0.195s
    
    Ok

To execute a single test file:
 
    $ python3 -m unittest tests/test_window.py
    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.058s
    
    Ok
    

## Contributing

The project is divided in two major sections:

* pylibui.libui: a cffi auto-generated wrapper around the libui C shared library. 
* pylibui: an object oriented pythonic wrapper that makes calls to pylibui.libui.
 
If you want to contribute, these are the two places that you can implement some
code and make a pull request. 

I'm accepting pull requests if the code is clean and it comes with a working example.
