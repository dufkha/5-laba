import re

def sort_words(text):
    """
    Сортує слова за алфавітом, спочатку українські, потім англійські.
    """
    # Видаляємо знаки пунктуації
    words = re.findall(r'\b[а-яА-ЯїЇєЄґҐіІa-zA-Z]+\b', text)
    # Розділяємо слова на українські та англійські
    ukrainian_words = sorted([word for word in words if re.match(r'[а-яА-ЯїЇєЄґҐіІ]', word)], key=str.casefold)
    english_words = sorted([word for word in words if re.match(r'[a-zA-Z]', word)], key=str.casefold)
    return ukrainian_words, english_words

try:
    # Зчитуємо текст з файлу
    with open("input.txt", "r", encoding="utf-8") as file:
        text = file.read()
        # Виділяємо перше речення
        first_sentence = text.split('.')[0] + '.'
        print("Перше речення:")
        print(first_sentence)

        # Сортуємо слова
        ukrainian_words, english_words = sort_words(text)
        print("\nСлова (українські):", ukrainian_words)
        print("Слова (англійські):", english_words)
        print("\nЗагальна кількість слів:", len(ukrainian_words) + len(english_words))

except FileNotFoundError:
    print("Помилка: файл 'input.txt' не знайдено.")
except Exception as e:
    print(f"Виникла помилка: {e}")
