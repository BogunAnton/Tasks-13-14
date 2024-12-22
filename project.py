import threading
import random

def perform_calculation(full_text, anagrams):
    words = full_text.split()
    anagrams_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]
    result = [group for group in anagrams_dict.values() if len(group) > 1]
    anagrams.extend(result)
    print("Алгоритм выполнен")

def is_int(choice):
    """ Проверка на то, что s - целое число"""
    try:
        if type(choice) is int:
            return True
        if choice is None:
            return False
        if not choice.isdecimal():
            return False
        int(choice)
        return True
    except (Exception, ValueError, TypeError):
        return False

def self_input_text(user_id):
    # Функция, которая позволяет пользователю самостоятельно ввести текст
    print(f"Пользователь {user_id}: Введите текст (для завершения ввода введите пустую строку):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    # Объединяем все строки в один текст
    return " ".join(lines)

def random_input_text(min_length=10, max_length=1000):
    # Генерация случайного текста на русском языке
    letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ ' + ' ' * 7
    length = random.randint(min_length, max_length)  # Генерация случайной длины
    return ''.join(random.choice(letters) for _ in range(length))

def f1(full_text, user_id):
    """Функция меню для ввода текста текст"""
    print(f"Пользователь {user_id}: Выберите опцию 1-2:\n"
          "1. Ввести текст самостоятельно\n"
          "2. Сгенерировать случайный текст\n")
    option = input()
    if is_int(option):
        option = int(option)
    if option == 1:
        full_text.append(self_input_text(user_id))
        print(f"Пользователь {user_id}: Вы ввели следующий текст:")
        print(full_text[0])
    elif option == 2:
        full_text.append(random_input_text())
        print(f"Пользователь {user_id}: Сгенерированный случайный текст:")
        print(full_text[0])
    else:
        print('error')
    return True  # Возвращаем True, чтобы указать, что текст был введен

def f3(anagrams, user_id):
    """ Вывод результата """
    if len(anagrams) == 0:
        print(f"Пользователь {user_id}: Анаграмм в тексте нет!!!")
    else:
        for group in anagrams:
            print(f"Пользователь {user_id}: Анаграммы:", group)

def run_menu(user_id):
    full_text = []
    anagrams = []
    text_entered = False  # Флаг для отслеживания ввода текста
    algorithm_executed = False  # Флаг для отслеживания выполнения алгоритма

    while True:
        print(f"Пользователь {user_id}: Выберите пункт меню:\n"
              "1. Ввод исходного текста, вручную или сгенерированного случайным образом\n"
              "2. Выполнение алгоритма по поиску анаграмм в исходном тексте\n"
              "3. Вывод результата алгоритма\n"
              "0. Выход из цикла")
        choice = input()
        if is_int(choice):
            choice = int(choice)
        if choice == 1:
            text_entered = f1(full_text, user_id)
        elif choice == 2:
            if text_entered:
                thread = threading.Thread(target=perform_calculation, args=(full_text[0], anagrams))
                thread.start()
                thread.join()
                algorithm_executed = True
            else:
                print("Сначала введите текст (пункт 1).")
        elif choice == 3:
            if text_entered and algorithm_executed:
                f3(anagrams, user_id)
            else:
                print("Сначала выполните пункты 1 и 2.")
        elif choice == 0:
            break
        else:
            print('error')

def menu():
    # Создаем два потока для двух пользователей
    user1_thread = threading.Thread(target=run_menu, args=(1,))
    user2_thread = threading.Thread(target=run_menu, args=(2,))

    # Запускаем потоки
    user1_thread.start()
    user2_thread.start()

    # Ждем завершения потоков
    user1_thread.join()
    user2_thread.join()

if __name__ == "__main__":
    menu()
