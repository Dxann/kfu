import os
p_pwd = os.getcwd()
p_directory = p_pwd
while True:
    choice = input("\nВыберите команду:\npwd - осмотр текущей папки\ncd (dirname) - переход в другую папку\ntouch (filename) - создание пустого файла\ncat (filename) - вывод содержимого файла\nls - вывод списка файлов в папке\nrm (filename) - удаление файла\nexit - Выход\n").split()
    try:
        if choice[0] == "pwd":
            print("\nТекущая папка: " + p_pwd)
        elif choice[0] == "cd":
            if choice[1] in os.listdir(p_pwd):
                p_pwd = os.path.join(p_pwd, choice[1])
                print("\nВы перешли в папку: " + p_pwd)
            elif choice[1] == "..":
                if p_pwd != p_directory:
                    p_pwd = p_directory
                    print("\nВы перешли в папку: " + p_pwd)
                elif p_pwd == p_directory: print("\nВы находитесь в родительской папке")
            else:
                print("\nТакой папки не существует")
        elif choice[0] == "touch":
            file_path = os.path.join(p_pwd, choice[1])
            f = open(file_path, 'w')
            print(f"\nФайл {choice[1]} успешно создан!")
            f.close()
        elif choice[0] == "cat":
            file_path = os.path.join(p_pwd, choice[1])
            with open(file_path) as f:
                print("\n" + f.read())
        elif choice[0] == "ls":
            ls = "\n"
            for i in os.listdir(p_pwd):
                if "." not in i:
                    ls += str(i) + "/  "
                else: ls += str(i) + "  "
            print(ls)
        elif choice[0] == "rm":
            file_path = os.path.join(p_pwd, choice[1])
            os.remove(file_path)
            print(f"\nФайл {choice[1]} успешно удален!")
        elif choice[0] == "exit":
            exit()
        else:
            print("\nВведена несуществующая команда!")
            continue
    except FileNotFoundError:
        print("\nФайл не найден")
        continue
    except PermissionError:
        print("\nНедопустимое значение")
        continue
    except IndexError:
        print("\nНедопустимое значение")
        continue