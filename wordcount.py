#omyaasree balaji
#files and dictionaries


def create_word_frequency_dict(file_name):
    word_freq_dict = {}
    
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                # Remove punctuation and convert to lowercase
                word = word.strip('.,?!":;()[]{}').lower()
                if word in word_freq_dict:
                    word_freq_dict[word] += 1
                else:
                    word_freq_dict[word] = 1

    return word_freq_dict

def print_lines_with_word(file_name, user_word, word_freq_dict):
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if user_word in line.lower():
                print(line)

def main():
    file_name = 'Alice-in-wonderland.txt'
    word_freq_dict = create_word_frequency_dict(file_name)

    user_word = input("Enter the word you are looking for: ").lower()

    if user_word in word_freq_dict:
        print(f"The word '{user_word}' was found {word_freq_dict[user_word]} times in the file.")
        print(f"Lines containing the word '{user_word}':")
        print_lines_with_word(file_name, user_word, word_freq_dict)
    else:
        print(f"The word '{user_word}' was not found in the file.")

if __name__ == '__main__':
    main()
