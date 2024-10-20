import pytest
import sys

#pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason='Linux only')

const = 9/5
def centigrate_to_fahrenheit(cent = 0):
    fahrenheit = (const * cent) + 32
    return fahrenheit
@pytest.mark.skip(reason="When mentioned reason as 'Skipping without any reason'")
def test_case01():
    assert type(const) == float
#@pytest.mark.skipif(sys.version_info <(3, 13), reason=" required Python 3.12, I know" )
@pytest.mark.skipif(centigrate_to_fahrenheit()==32, reason = 'Skip as fahrenheit is 32 degree')
def test_case02():
    assert centigrate_to_fahrenheit() == 32
@pytest.mark.skipif(pytest.__version__ < '8.3.4', reason = 'Skip as current version is 8.3.3 which is less that 8.3.4')
def test_case03():
    assert centigrate_to_fahrenheit(38) == 100.4

