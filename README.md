# pylibui

Python3 wrapper for [libui](https://github.com/andlabs/libui/). It uses ctypes 
to interface with the libui shared library.


## Usage

```python    
from pylibui.core import App
from pylibui.controls import Window


class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()


app = App()

window = MyWindow('Window', 800, 600)
window.setMargined(True)
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
