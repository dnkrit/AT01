import pytest
from main1 import count_vowels

@pytest.mark.parametrize("test_input, expected", [
    ("aeiou", 5),          # Только гласные (англ.)
    ("бцжйф", 0),          # Нет гласных (рус.)
    ("Hello World", 3),    # Смешанные буквы
    ("Привет, Мир!", 3),   # Русский текст
    ("AEIOU", 5),          # Заглавные гласные
    ("", 0),               # Пустая строка
    ("123456", 0),         # Только цифры
    ("аЕиОу", 5),          # Смешанные регистры (рус.)
])
def test_count_vowels(test_input, expected):
    assert count_vowels(test_input) == expected
