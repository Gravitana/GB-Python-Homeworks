# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (здесь только буквы).
# Входные и выходные данные хранятся в отдельных текстовых файлах.


def compress_line(input_str):
    compressed_line = ''
    prev_ch = input_str[0]
    count_chars = 0
    for ch in input_str:
        if ch == prev_ch:
            count_chars += 1
        else:
            compressed_line += str(count_chars) + prev_ch
            prev_ch = ch
            count_chars = 1
    compressed_line += str(count_chars) + prev_ch
    return compressed_line


def decompress_line(input_str):
    decompressed_line = ''
    number = ''
    for ch in input_str:
        if ch.isdigit():
            number += ch
        else:
            decompressed_line += (int(number) * ch)
            number = ''
    return decompressed_line


try:
    output_list = []

    with open("source.txt", "r") as file_source:
        for line in file_source:
            output_list.append(compress_line(line.strip()))

    with open("compressed.txt", "w") as file:
        for line in output_list:
            file.write(line + '\n')

    with open("compressed.txt", "r") as file_source:
        for line in file_source:
            print(decompress_line(line.strip()))

except:
    print("Введены некоректные данные!")