from multiprocessing import Process, Pool, Manager, Array
import time


def counter(separated_words, return_dict):
    for i in separated_words:
        # print(str(i) + " represent!")
        if i not in return_dict:
            # time.sleep(.001)
            # words_count_dict.update({i: 1})
            return_dict[i] = 1
        if i in return_dict:
            # words_num = return_dict[i]
            return_dict[i] += 1
    # return words_count_dict


def main():
    file = open(file_name, 'r')
    file_text = file.read()
    words_array = file_text.split()

    step = int(len(words_array) / 4)
    separated_words_array = [words_array[pos: pos + step] for pos in range(0, len(words_array), step)]
    manager = Manager()
    return_dict = manager.dict()
    processes_array = []
    for separated_words in separated_words_array:
        p = Process(target=counter, args=(separated_words, return_dict))
        processes_array.append(p)
        p.start()

    for process in processes_array:
        process.join()
    print(return_dict)
    max_key = max(return_dict, key=return_dict.get)
    max_value = max(return_dict.values())
    print({max_key: max_value})


if __name__ == '__main__':
    start_time = time.time()
    file_name = 'sampleFICT.txt'

    main()

    duration = time.time() - start_time
    print(f"Operation took {duration} seconds")
