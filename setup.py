from setuptools import setup, find_packages
setup(
    name = "firkin",
    version = "0.02",
    py_modules = ['firkin'],
    package_data = { '': ['README',  'COPYING']
                     },
    # metadata for upload to PyPI
    author = "Florian Diesch",
    author_email = "devel@florian-diesch.de",
    description = "convert between different measurement units",
    long_description = \
"""
What is firkin?
===============

firkin is a python module to convert between different measurement
units.


Usage
=====

First we create an instance of `UnitManager`::

>>> um=UnitManager()
    
Next we create two families of units. The first one ist ``liter`` and
uses ``SIFamily`` to automatically create units with the SI prefixes::
     
    >>> um.add(SIFamily(base='l', name='liter'))

Now our ``UnitManager`` knows about fl, pl, nl, ..., Ml, Gl, Tl.

How many liters are 10000 ml?::

    >>> um.convert_to_unit(1e4, 'ml', 'l')
    (Decimal("10.0000"), 'l')

Next we create a family by hand::
    
    >>> f=Family(name='f', base='gallon')
    >>> f.add('barrel', 36, 'gallon')
    >>> f.add('kilderkin', 0.5, 'barrel')
    >>> f.add('firkin', 0.5, 'kilderkin')

Now we have a family called ``f`` that used gallon as its base and knows about 
barrel, kilderkin and firkin, too.

How much gallons is one firkin?::

    >>> f.convert(1, 'firkin', 'gallon')
    (Decimal("9.00"), 'gallon')

What's the best way to express 3 kilderkin?::

    >>> f.autoconvert(3, 'kilderkin')
    (Decimal("1.50"), 'barrel')

To convert between family ``f`` and family ``liter`` we need to add ``f`` to
our ``UnitManager`` and tell how much liters (base unit of family ``liter``) a
gallon (base unit of family ``f``) is::

    >>> um.add(f, other='liter',  factor=4.54609)

Of course the ``UnitManger`` can convert firkin to gallon, too::

    >>> um.convert_to_unit(1, 'firkin', 'gallon')
    (Decimal("9.00"), 'gallon')

But it also can convert firkin to liters::

    >>> um.convert_to_unit(1, 'firkin', 'l')
    (Decimal("40.9148100"), 'l')

Or find the best way to express one liter in one of the units from
family ``f``::

   >>> um.convert_to_family(1, 'l', 'f')
   (Decimal("0.219969248299"), 'gallon')

That works with barrels, too::

   >>> um.convert_to_family(1, 'barrel', 'f')
   (Decimal("1.00"), 'barrel')


""",
    license = "GPL",
    keywords = "measurement units convert conversion",
    url = "http://www.florian-diesch.de/software/firkin/",     
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Natural Language :: English',
    'Natural Language :: German',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Software Development :: Libraries'
    ]
    )
