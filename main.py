import time

start_time = time.time()

file = open('sampleFICT.txt', 'r')
file_text = file.read()
words_array = file_text.split()

words_count_dict = {}

for i in words_array:
    if i not in words_count_dict:
        # time.sleep(.001)
        words_count_dict.update({i: 1})
    if i in words_count_dict:
        words_num = words_count_dict.get(i)
        words_count_dict.update({i: words_num + 1})

print(words_count_dict)
max_key = max(words_count_dict, key=words_count_dict.get)
max_value = max(words_count_dict.values())
print({max_key: max_value})

duration = time.time() - start_time
print(f"Operation took {duration} seconds")
