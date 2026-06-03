import re

def count_specific_word(text, word):
    if not text.strip():
        return 0
    words = text.lower().split()
    return words.count(word.lower())

def identify_most_common_word(text):
    if not text.strip():
        return None          
    words = text.lower().split()
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return max(word_counts, key=word_counts.get)

def calculate_average_word_length(text):
    if not text.strip():
        return 0
    words = text.split()
    cleaned_words = []
    i = 0
   
    while i < len(words):
        clean = re.sub(r'[^a-zA-Z0-9]', '', words[i])
        if clean:
            cleaned_words.append(clean)
        i += 1
    if not cleaned_words:
        return 0
    total_chars = sum(len(word) for word in cleaned_words)
    return total_chars / len(cleaned_words)

def count_paragraphs(text):
    if not text.strip():
        return 1
    paragraphs = text.split("\n\n")
    paragraphs = [p for p in paragraphs if p.strip()]
    return len(paragraphs)

def count_sentences(text):
    if not text.strip():
        return 1
    sentences = re.split(r'[.!?]+', text)
    sentences = [s for s in sentences if s.strip()]
    return len(sentences)
    
if __name__ == "__main__":
    with open("news_article.txt", "r") as file:
        article = file.read()

    print("===== News Article Analysis =====\n")
    print(f"Word count for 'the': {count_specific_word(article, 'the')}")
    print(f"Most common word: {identify_most_common_word(article)}")
    print(f"Average word length: {calculate_average_word_length(article):.2f} characters")
    print(f"Number of paragraphs: {count_paragraphs(article)}")
    print(f"Number of sentences: {count_sentences(article)}")
    print("\n===== Analysis Complete =====")