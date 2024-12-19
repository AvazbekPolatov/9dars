# # 1-masala
# def sum_digits(number):
#     total = 0
#     while number > 0:
#         total += number % 10
#         number //= 10
#     return total

# print(sum_digits(108))  

# # -------------------------------------------------------------

# # 2-masala
# def convert_seconds(seconds):
#     days = seconds // (24 * 3600)
#     seconds %= (24 * 3600)
#     hours = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
#     return f"{days} kun, {hours} soat, {minutes} minut, {seconds} sekund"


# print(convert_seconds(91000))  

# # ------------------------------------------------------------------------

# def capitalize_names(names):
#     return [name.capitalize() for name in names]


# names = ['alfred', 'tabitha', 'william', 'arla']
# print(capitalize_names(names))  

# # ------------------------------------------------------------------------

# # 4-masala
# def high_scores(scores):
#     return [score for score in scores if score > 75]


# scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(high_scores(scores))  

# # ------------------------------------------------------------------------- 

# # 5-masala
# def get_palindromes(words):
#     return [word for word in words if word.lower() == word.lower()[::-1]]

# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# print(get_palindromes(words))  

# # --------------------------------------------------------------------------
# # 6-masala
# def replace_e(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i].lower() == 'e':
#             result += '3'
#         else:
#             result += text[i]
#         i += 1
#     return result


# text = input("Matn kiriting: ")
# print(replace_e(text))

# # --------------------------------------------------------------------------

# # 7-masala
# def remove_spaces(text):
#     result = ""
#     i = 0
#     while i < len(text):
#         if text[i] != ' ':
#             result += text[i]
#         i += 1
#     return result


# text = input("Matn kiriting: ")
# print(remove_spaces(text))

# # --------------------------------------------------------------------------

# # 8-masala
# import threading

# def multiply_element(number):
#     result = number * 2
#     print(f"{number} * 2 = {result}")

# numbers = list(range(1, 11))
# threads = []

# for num in numbers:
#     thread = threading.Thread(target=multiply_element, args=(num,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# # --------------------------------------------------------------------------

# # 9-masala
# import threading
# import random
# import time

# def generate_random():
#     number = random.randint(1, 100)
#     time.sleep(0.1)  
#     print(f"Thread {threading.current_thread().name}: {number}")

# threads = []
# for i in range(10):
#     thread = threading.Thread(target=generate_random)
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()
