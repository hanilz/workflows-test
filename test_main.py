import pytest
from main import fetch_url

def test_fetch_url():
    status, _ = fetch_url("https://httpbin.org/get")
    assert status == 200

