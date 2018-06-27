from ..geoparse import Geoparser
import pytest

@pytest.fixture(scope='session', autouse=True)
def geo():
    return Geoparser()

@pytest.fixture(scope='session', autouse=True)
def geo_thread():
    return Geoparser(n_threads = 4)
