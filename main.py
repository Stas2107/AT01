def count_vowels(s):
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = sum(1 for char in s if char in vowels)
    return count