from unittest import result


def vowel_counter(sentence):
    vowels = 'aeiou'
    result = {}

    for vowel in vowels:
        result[vowel] = sentence.count(vowel)
    return result

if __name__ == "__main__":
    msg = "This is a test"
    print(vowel_counter(msg))        