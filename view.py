import proc

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Добавить заметку\n"
          "2. Отобразить все заметки\n"
          "3. Редактировать заметку\n"
          "4. Сохранить справочник в текстовом формате\n"
          "5. Удалить заметку\n"
          "6. Закончить работу")
    choice = int(input('что Вас интересует? '))
    if choice == 1:
        proc.add_note()
        show_menu()
    elif choice == 2:
        proc.read_csv()
        show_menu()
    elif choice == 3:
        proc.edit_note()
        show_menu()
    elif choice == 4:
        proc.save_txt()
        show_menu()
    elif choice == 5:
        proc.remove_note()
        show_menu()
    elif choice == 6:
        print('работа звершена')

























