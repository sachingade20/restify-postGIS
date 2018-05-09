import requests
import pytest

out = None

@pytest.fixture(scope="module")
def get_data():
    global out
    out = requests.get("http://18.204.133.230:32378")

def test_demo_content(get_data):
    assert "Map of Parks and Historic Sites" in out.content


def test_demo_status_code(get_data):
    assert out.status_code == 200
