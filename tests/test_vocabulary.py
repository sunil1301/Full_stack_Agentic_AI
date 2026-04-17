def test_empty_vocabulary():
    from your_module import create_vocabulary
    with pytest.raises(ValueError, match="empty vocabulary; perhaps the documents only contain stop words"):
        create_vocabulary([])

def test_vocabulary_with_stop_words():
    from your_module import create_vocabulary
    stop_words_docs = ["the", "is", "at", "which", "on"]
    with pytest.raises(ValueError, match="empty vocabulary; perhaps the documents only contain stop words"):
        create_vocabulary(stop_words_docs)