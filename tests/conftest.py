from typing import Generator

import pytest
from fastapi.testclient import TestClient

from ..app.main import app


@pytest.fixture(scope='function')
def call_client() -> Generator:
    with TestClient(app) as cli:
        yield cli


@pytest.fixture(scope='function')
def list_client() -> Generator:
    with TestClient(app) as list_users:
        yield list_users


@pytest.fixture(scope='function')
def list_user_by_id() -> Generator:
    with TestClient(app) as get_by_id:
        yield get_by_id


@pytest.fixture(scope='function')
def creating_new_user() -> Generator:
    with TestClient(app) as new_user:
        yield new_user


@pytest.fixture(scope='function')
def edit_user() -> Generator:
    with TestClient(app) as user_has_edit:
        yield user_has_edit


@pytest.fixture(scope='function')
def delete_user() -> Generator:
    with TestClient(app) as user_has_removed:
        yield user_has_removed


# Fixtures de resultados negativos tratados

@pytest.fixture(scope='function')
def url_error_list_client() -> Generator:
    with TestClient(app) as wrong_url_list:
        yield wrong_url_list


@pytest.fixture(scope='function')
def user_not_id() -> Generator:
    with TestClient(app) as not_exist_id:
        yield not_exist_id


@pytest.fixture(scope='function')
def fail_new_user() -> Generator:
    with TestClient(app) as new_user_fail:
        yield new_user_fail


@pytest.fixture(scope='function')
def edit_user_fail() -> Generator:
    with TestClient(app) as user_fail_edit:
        yield user_fail_edit


@pytest.fixture(scope='function')
def delete_user_fail() -> Generator:
    with TestClient(app) as user_remove_fail:
        yield user_remove_fail
