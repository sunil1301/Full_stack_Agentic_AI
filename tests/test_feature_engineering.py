import pytest

def test_empty_vocabulary():
    with pytest.raises(ValueError, match="empty vocabulary"):
        # Call the function that creates vocabulary with empty input
        create_vocabulary([])

def test_vocabulary_with_stop_words():
    stop_words_documents = ["the", "is", "at", "which", "on"]
    with pytest.raises(ValueError, match="empty vocabulary"):
        # Call the function that creates vocabulary with stop words only
        create_vocabulary(stop_words_documents)