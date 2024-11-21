import threading
import time
def write_words(word_count, file_name):
    with open(file_name,'w', encoding='utf-8') as text:
        for i in range(word_count):
            time.sleep(0.1)
            text.write(f"Какое-то слово № {i}\n")
        print(f"Завершилась запись в файл {file_name}")

start_time = time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
tread5 = threading.Thread(target=write_words,args=(10, "example5.txt"))
tread6 = threading.Thread(target=write_words,args=(30, "example6.txt"))
tread7 = threading.Thread(target=write_words,args=(200, "example7.txt"))
tread8 = threading.Thread(target=write_words,args=(100, "example8.txt"))
print(time.time() - start_time)
tread5.start()
tread6.start()
tread7.start()
tread8.start()
tread5.join()
tread6.join()
tread7.join()
tread8.join()
print(time.time() - start_time)