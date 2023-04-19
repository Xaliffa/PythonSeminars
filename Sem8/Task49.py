
def console_menu():
    pass

def read_file():
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(file_path, 'a', encoding='utf-8') as f:
        f. writelines('\n' + input())

def find_file():
    find_info = input()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)

def change_file():
    find_info = input()
    new_info = input()
    with open(file_path, 'r+', encoding='utf-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                lst = line.split()
                print(lst)                                       # не дописана функция
                                                                 # чтобы что-то изменить, надо выгрузить что-то типа словаря с данными,
                                                                 # поменять там и перезаписать обратно в файл

def main():
    change_file()

    
file_path = r'phonebook.txt' 

if __name__ == '__main__':
    main()
        