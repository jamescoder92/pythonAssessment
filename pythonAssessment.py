import re  

with open("news_article.txt", "r") as file:
    article = file.read()  

def count_specific_word(text, word):

    
    if not text.strip(): 
        return 0

    words = text.lower().split()

    return words.count(word.lower())


def identify_most_common_word(text):

    if not text.strip():
        return ""

    words = text.lower().split()

    word_counts = {}

    for word in words:
    
        word_counts[word] = word_counts.get(word, 0) + 1

    return max(word_counts, key=word_counts.get)

def average_word_length(text):
    if not text.strip():
        return 0

    words = text.split()

    total_chars = sum(len(word) for word in words)

    return total_chars / len(words)


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

print("===== News Article Analysis =====\n")  

print(f"Word count for 'the': {count_specific_word(article, 'the')}")

print(f"Most common word: {identify_most_common_word(article)}")

print(f"Average word length: {average_word_length(article):.2f} characters")

print(f"Number of paragraphs: {count_paragraphs(article)}")

print(f"Number of sentences: {count_sentences(article)}")

print("\n===== Analysis Complete =====") 