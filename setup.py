# from distutils.core import setup
from setuptools import setup

setup(
    name='SdCalculator',
    version='0.1',
    packages=['calculator'],
    url='',
    license='GNU GPLv3',
    author='Youssef Seddik',
    author_email='yseddik94@gmail.com',
    description='A simple UI calculator written in Tkinter',
    long_description='This is a basic calculator supporting basic mathematic'
                     'operations(addition, product, substraction and division)'
                     ' the User Interface was made with Tkinter(a GUI binding '
                     'distributed with the standard library of Python) and'
                     ' Python version 3.4.',
   classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: All',
        'License :: OSI Approved :: GNU GPLv3',
        'Programming Language :: Python :: 3.4',
   ],
    keywords='calculator math basic_operations gui tkinter',
)
