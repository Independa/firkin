# -*- coding: utf-8 -*-

from decimal import Decimal


import firkin

def test_convert():
    fam=firkin.SIFamily('m')
    assert fam.convert(1, 'm', 'mm')==(1000, 'mm')
    assert fam.convert(5.2, 'km', 'm')==(5200, 'm')


def test_autoconvert():
    fam=firkin.SIFamily('m')
    assert fam.autoconvert(2e-8, 'm')==(20, 'nm')
    assert fam.autoconvert(2e8, 'm')==(200, 'Mm')
    assert fam.autoconvert(2e7, 'mm')==(20, 'km')


def test_convert_to_unit():
    um=firkin.UnitManager()
    um.add(firkin.SIFamily(base='l', name='liter'))

    f=firkin.Family(name='brit', base='gallon')
    f.add('barrel', 36, 'gallon')
    f.add('kilderkin', 0.5, 'barrel')
    f.add('firkin', 0.5, 'kilderkin')
    um.add(f, other='liter',  factor=4.54609)
    um.add(firkin.Family(base='°C'))
    um.add(firkin.Family(base='°F'), other='°C', offset=(-32/1.8), factor=5.0/9) 

    assert um.convert_to_unit(1e4, 'ml', 'l')==(10, 'l')
    assert um.convert_to_unit(1, 'firkin', 'gallon')==(9, 'gallon')
    assert um.convert_to_unit(1, 'firkin', 'ml')==(Decimal("40914.81"), 'ml')

    assert um.convert_to_unit(32, '°F', '°C')==(Decimal("-8E-12"), '°C')
    assert um.convert_to_unit(100, '°C', '°F')== (Decimal("212.0"), '°F')
    assert um.convert_to_unit(1, '°C', 'ml')== (None, None)
    

def test_convert_to_family():
    um=firkin.UnitManager()
    um.add(firkin.SIFamily(base='l', name='liter'))

    f=firkin.Family(name='brit', base='gallon')
    f.add('barrel', 36, 'gallon')
    f.add('kilderkin', 0.5, 'barrel')
    f.add('firkin', 0.5, 'kilderkin')
    um.add(f, other='liter',  factor=4.54609)
    um.add(firkin.Family(base='°C'))
    um.add(firkin.Family(base='°F'), other='°C', offset=(-32/1.8), factor=5.0/9)

    assert um.convert_to_family(1, 'firkin',
                                'liter')==(Decimal("40.91481"), 'l')
    assert um.convert_to_family(0.01, 'firkin',
                                'liter')==(Decimal("409.1481"), 'ml')
    assert um.convert_to_family(1e-5, 'gallon',
                                'liter')==(Decimal("45.4609"), 'µl')

    assert um.convert_to_family(1, 'l',
                                'brit')==(Decimal("0.219969248299"), 'gallon')

    assert um.convert_to_family(50, 'l',
                                'brit')==(Decimal("1.222051379438888888888888889"), 'firkin')

    assert um.convert_to_family(1, 'barrel', 'brit')==(1, 'barrel')
    assert um.convert_to_family(32, '°F', '°C')==(Decimal("-8E-12"), '°C')
    assert um.convert_to_family(100, '°C', '°F')== (Decimal("212.0"), '°F')
    assert um.convert_to_family(1, '°C', 'brit')== (None, None)
    

           
    
