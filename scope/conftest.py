import pytest

@pytest.fixture(scope="session")
def set_up():
    print("Вход в тест")
    yield
    print("Выход из теста")