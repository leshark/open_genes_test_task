import pytest
from fastapi.testclient import TestClient

from src.bio_stats_service.create_app import create_app

app = create_app()


# Incremental test marker
# https://docs.pytest.org/en/latest/example/simple.html#incremental-testing-test-steps
def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item  # pylint: disable=W0212


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" % previousfailed.name)


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as c:
        yield c
