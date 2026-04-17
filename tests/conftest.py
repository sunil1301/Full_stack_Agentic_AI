import pytest

@pytest.fixture
def sample_documents():
    return [
        "This is a sample document.",
        "Another document with some text.",
        ""
    ]

@pytest.fixture
def stop_word_documents():
    return [
        "the",
        "is",
        "at",
        "which",
        "on"
    ]