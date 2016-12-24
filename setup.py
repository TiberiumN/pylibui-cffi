from setuptools import setup
from setuptools import find_packages
setup(
    name='pylibui',
    version='0.0.1',
    description='Python wrapper for libui',
    packages=find_packages(),
    install_requires=['cffi'],
    package_data={'pylibui.libui': ['libui.so']}
)
