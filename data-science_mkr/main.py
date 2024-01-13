import matplotlib.pyplot as plt
import re


def read_text_from_file(file_path):
    with open(file_path) as file:
        return file.read()


def calculate_word_frequencies(text, case_sensitive=False):
    words = re.findall(r'\b\w+\b', text)

    word_freq = {}
    for word in words:
        key = word if case_sensitive else word.lower()
        if key in word_freq:
            word_freq[key] += 1
        else:
            word_freq[key] = 1

    return word_freq


def plot_word_histogram(word_freq):
    words = list(word_freq.keys())
    frequencies = list(word_freq.values())

    plt.figure(figsize=(10, 5))
    plt.bar(words, frequencies)
    plt.xlabel('Слова')
    plt.ylabel('Частота')
    plt.title('Гістограма частоти слів')
    plt.show()


if __name__ == "__main__":
    file_path = "input.txt"
    input_text = read_text_from_file(file_path)

    if input_text:

        print('Оберіть як визначити частоту слів:\n')
        print('1 - Не розрізняючи регістр')
        print('2 - Розрізняючи регістр\n')
        mode = int(input('Режим:'))

        if mode == 1:
            word_freq = calculate_word_frequencies(input_text)

            for word, freq in word_freq.items():
                print(f'{word}: {freq} разів')

            plot_word_histogram(word_freq)
        else:
            word_freq = calculate_word_frequencies(input_text, case_sensitive=True)

            for word, freq in word_freq.items():
                print(f'{word}: {freq} разів')

            plot_word_histogram(word_freq)
