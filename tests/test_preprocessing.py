import pytest
from your_module import preprocess_documents

def test_preprocess_empty_documents():
    documents = []
    processed = preprocess_documents(documents)
    assert processed == []

def test_preprocess_only_stop_words():
    documents = ["the", "is", "at", "which", "on"]
    processed = preprocess_documents(documents)
    assert processed == []

def test_preprocess_valid_documents():
    documents = ["This is a test document.", "Another document for testing."]
    processed = preprocess_documents(documents)
    assert len(processed) > 0
    assert all(len(doc) > 0 for doc in processed)