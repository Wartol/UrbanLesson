import io
def custom_write(file_name, strings):
    with open('file_name', 'w', encoding='utf-8') as text:
        for i in strings:
            text.write(str(i) + "\n")


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
with open('file_name', 'r', encoding='utf-8') as text:
    text.seek(0)
    for i in range(4):
        print(i +1 ,text.tell(),text.readline())