import timeit
from boyer_moore_search import boyer_moore_search as bm_search
from kmp_search import kmp_search
from rabina_karpa_search import rabin_karp_search as rk_search

algorithms = {
    'Boyer-Moore': bm_search,
    'KMP': kmp_search,
    'Rabin-Karp': rk_search
}   

def measure_time(algorithm, text, pattern, iterations=1000):
    timer = timeit.Timer(lambda: algorithm(text, pattern))
    time_taken = timer.timeit(number=iterations)
    avg_time = time_taken / iterations
    return avg_time

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
    
article1 = load_text('Exercise03/article1.txt')
article2 = load_text('Exercise03/article2.txt')

# Паттерни:
pattern_found_1 = "алгоритми та структури даних"
pattern_not_found_1 = "неіснуючий вигаданий текст"
pattern_found_2 = "рекомендаційної системи"
pattern_not_found_2 = "інтерполяційний пошук"


results = {}

# --- Test for Article 1 ---
for name, func in algorithms.items():
    # 1. Found
    time_found = measure_time(func, article1, pattern_found_1)
    results[f"Article 1, Found, {name}"] = time_found

    # 2. Not Found
    time_not_found = measure_time(func, article1, pattern_not_found_1)
    results[f"Article 1, Not Found, {name}"] = time_not_found

# --- Test for Article 2 ---
for name, func in algorithms.items():
    # 3. Found
    time_found = measure_time(func, article2, pattern_found_2)
    results[f"Article 2, Found, {name}"] = time_found

    # 4. Not Found
    time_not_found = measure_time(func, article2, pattern_not_found_2)
    results[f"Article 2, Not Found, {name}"] = time_not_found

# Виведення результатів
for test_case, time_taken in results.items():
    print(f"{test_case}: {time_taken:.10f} секунд")
