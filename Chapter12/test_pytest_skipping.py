import sys
import pytest


def test_simple_skip():
    if sys.platform != "fakeos":
        pytest.skip("Test works only on fakeOS")

    fakeos.do_something_fake()
    assert fakeos.did_not_happen


@pytest.mark.skipif("sys.version_info <= (3,0)")
def test_python3():
    assert b"hello".decode() == "hello"
