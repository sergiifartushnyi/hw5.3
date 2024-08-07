
import string
def create_hashtag(input_string):

    clean_string = ''.join(char for char in input_string if char not in string.punctuation)

    words = clean_string.split()

    hashtag = '#' + ''.join(word.capitalize() for word in words)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag

input_string = input("Введіть рядок для перетворення в хештек:")
result = create_hashtag(input_string)
print(result)