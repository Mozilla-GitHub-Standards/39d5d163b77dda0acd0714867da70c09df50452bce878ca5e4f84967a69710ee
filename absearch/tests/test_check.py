from absearch.tests.support import runServers, stopServers, capture
from absearch.check import main


def setUp():
    runServers()


def tearDown():
    stopServers()


def test_check():

    with capture() as out:
        res = main([])

    stdout, stderr = out
    assert stderr == '', stderr
    assert 'OK' in stdout
    assert res == 0
