class ProgrammingLanguage:
    """Язык программирования"""

    def __init__(self, id, name, ide_id):
        self.id = id
        self.name = name
        self.ide_id = ide_id


class IDE:
    """Средство разработки (IDE)"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class LanguageIDE:
    """'Языки программирования в средах разработки' для реализации связи многие-ко-многим"""

    def __init__(self, ide_id, language_id, users_count):
        self.ide_id = ide_id
        self.language_id = language_id
        self.users_count = users_count


# Список средств разработки (IDE)
ides = [
    IDE(1, 'PyCharm'),
    IDE(2, 'Visual Studio Code'),
    IDE(3, 'IntelliJ IDEA'),
    IDE(4, 'Eclipse'),
    IDE(5, 'Sublime Text'),
    IDE(6, 'Visual Studio')
]

# Список языков программирования
languages = [
    ProgrammingLanguage(1, 'Python', 1),
    ProgrammingLanguage(2, 'Java', 3),
    ProgrammingLanguage(3, 'C++', 4),
    ProgrammingLanguage(4, 'JavaScript', 2),
    ProgrammingLanguage(5, 'C#', 6),
    ProgrammingLanguage(6, 'Go', 2)
]

# Связь языков программирования и средств разработки
languages_ides = [
    LanguageIDE(1, 1, 1000),
    LanguageIDE(2, 4, 2000),
    LanguageIDE(3, 2, 1500),
    LanguageIDE(4, 3, 1600),
    LanguageIDE(2, 6, 200),
    LanguageIDE(5, 5, 800),
    LanguageIDE(6, 5, 1200),
    LanguageIDE(5, 1, 200),
    LanguageIDE(4, 6, 700),
    LanguageIDE(1, 4, 500),
    LanguageIDE(3, 5, 300),
    LanguageIDE(2, 2, 400),
    LanguageIDE(6, 3, 600),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(lang.name, ide.id, ide.name)
                   for ide in ides
                   for lang in languages
                   if lang.ide_id == ide.id]

    # Соединение данных многие-ко-многим
    many_to_many = [(lang.name, ide.name, lid.users_count)
                    for ide in ides
                    for lid in languages_ides
                    for lang in languages if lang.id == lid.language_id and ide.id == lid.ide_id]

    # Г1: Выводим список всех IDE, которые начинаются с буквы «V»
    print('Задание Г1')
    result = filter(lambda x: x[2].startswith('V'), one_to_many)
    for i in result:
        print(f"Средство разработки: {i[2]}, Язык программирования: {i[0]}")

    # Г2: Список средств разработки с максимальным количеством пользователей для каждого языка
    print('\nЗадание Г2')
    max_users = {}
    for lang_name, ide_name, users_count in many_to_many:
        if ide_name not in max_users or max_users[ide_name] < users_count:
            max_users[ide_name] = users_count
    sorted_ides = sorted(max_users.items(), key=lambda x: x[1])
    for ide_name, users_count in sorted_ides:
        print(f"Средство разработки: {ide_name}, Максимальное количество пользователей: {users_count}")

    # Г3: Список всех связанных языков программирования и средств разработки
    print('\nЗадание Г3')
    sorted_languages = sorted(many_to_many, key=lambda x: (x[1], x[0]))
    for lang in sorted_languages:
        print(f"Средство разработки: {lang[1]}, Язык программирования: {lang[0]}")


if __name__ == '__main__':
    main()
