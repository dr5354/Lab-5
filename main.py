import re
import csv


def extract_words_after_comma(text):
  return re.findall(r'\b\w+(?=,)', text)

def extract_info_in_square_brackets(text):
  return re.findall(r"\[[^\]]*\]", text)

def extract_colors_from_html(filename):
    with open(filename, "r", encoding='utf-8') as file:
        html_content = file.read()

    colors = re.findall(r'#[0-9a-fA-F]{6}', html_content)
    return colors

def extract_data_for_csv(filename):
    with open(filename, 'r') as file:
        file = file.read()

    website = re.findall(r'https?://[a-zA-Z0-9.-]+/', file)
    date = re.findall(r'\d{4}-\d{2}-\d{2}', file)
    surname = re.findall(r'[A-Z][a-z]+(?!\d\d@|@)', file)
    email = re.findall(r'[a-z][a-z0-9-]*@[a-z0-9-]+\.[a-z]{3}', file)
    id = [int(x)+1 for x in range(len(email))]
    data_for_csv = zip(id, surname, email, date, website)
    return data_for_csv

file_name1 = "task1-ru.txt"
file_name2 = "task2.html"
file_name3 = "task3.txt"


if __name__ == '__main__':
    #ЗАДАНИЕ 1
    with open(file_name1, "r", encoding="utf-8") as file:
      text = file.read()

    words_after_comma = extract_words_after_comma(text)
    info_in_square_brackets = extract_info_in_square_brackets(text)

    print("Слова, после которых стоит запятая:")
    print(words_after_comma)
    print("Информация в квадратных скобках:")
    print(info_in_square_brackets)

    #ЗАДАНИЕ 2
    found_colors = extract_colors_from_html(file_name2)
    print(f"Найденные цвета: {', '.join(found_colors)}\n")

    #ЗАДАНИЕ 4
    data_for_csv = extract_data_for_csv(file_name3)
    with open('my_data.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # Записываем каждую строку данных
        for row in data_for_csv:
            csvwriter.writerow(row)
    print("Данные успешно записаны в файл 'my_data.csv'")