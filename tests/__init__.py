def test_empty_vocabulary():
    with pytest.raises(ValueError, match="empty vocabulary; perhaps the documents only contain stop words"):
        # Call the function that creates vocabulary with empty input
        create_vocabulary([])  # Assuming create_vocabulary is the function to test

def test_only_stop_words():
    stop_words_documents = ["the", "is", "at", "which", "on"]
    with pytest.raises(ValueError, match="empty vocabulary; perhaps the documents only contain stop words"):
        create_vocabulary(stop_words_documents)  # Assuming create_vocabulary is the function to test