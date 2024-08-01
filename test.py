import pytest
from main import count_vowels  # Замените 'your_module' на имя вашего файла

def test_count_vowels_only_vowels():
    assert count_vowels("аеиоуюя") == 7  # В строке только гласные

def test_count_vowels_no_vowels():
    assert count_vowels("бкфц") == 0  # В строке нет гласных

def test_count_vowels_mixed_case():
    assert count_vowels("Привет, как дела?") == 5  # Смешанные строки

def test_count_vowels_empty_string():
    assert count_vowels("") == 0  # Пустая строка

