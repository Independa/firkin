from nose.tools import *
from decimal import Decimal
import firkin


def test_convert_to_group():
    um=firkin.UnitManager()    
    um.add(firkin.SIFamily(base='l', name='liter'), groups='metric')
    f=firkin.Family(name='brit', base='gallon')
    f.add('barrel', 36, 'gallon')
    f.add('kilderkin', 0.5, 'barrel')
    f.add('firkin', 0.5, 'kilderkin')
    um.add(f, other='liter',  factor=4.54609, groups='brit')

    assert um.convert_to_group(1, 'firkin', 'metric') == (Decimal("40.9148100"),
                                                         'l')

def test_convert_to_group_extened_SI_family():
    um=firkin.UnitManager()    
    um.add(firkin.SIFamily(base='l', name='liter', extended=True),
           groups='metric')
    f=firkin.Family(name='brit', base='gallon')
    f.add('barrel', 36, 'gallon')
    f.add('kilderkin', 0.5, 'barrel')
    f.add('firkin', 0.5, 'kilderkin')
    um.add(f, other='liter',  factor=4.54609, groups='brit')

    assert um.convert_to_group(1, 'firkin', 'metric') == (Decimal("4.09148100"),
                                                         'dal')



    

    
