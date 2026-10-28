from backend.app import hello


def test_hello() -> None:
    assert hello() == "Hello, World!"
    assert hello("Ada") == "Hello, Ada!"
