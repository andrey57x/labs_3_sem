import main
import unittest


class TestMethods(unittest.TestCase):

    def setUp(self):
        self.ides = [
            main.IDE(1, 'PyCharm'),
            main.IDE(2, 'Visual Studio Code'),
            main.IDE(3, 'IntelliJ IDEA'),
            main.IDE(4, 'Eclipse'),
            main.IDE(5, 'Sublime Text'),
            main.IDE(6, 'Visual Studio')
        ]
        self.languages = [
            main.ProgrammingLanguage(1, 'Python', 1),
            main.ProgrammingLanguage(2, 'Java', 3),
            main.ProgrammingLanguage(3, 'C++', 4),
            main.ProgrammingLanguage(4, 'JavaScript', 2),
            main.ProgrammingLanguage(5, 'C#', 6),
            main.ProgrammingLanguage(6, 'Go', 2)
        ]
        self.languages_ides = [
            main.LanguageIDE(1, 1, 1000),
            main.LanguageIDE(2, 4, 2000),
            main.LanguageIDE(3, 2, 1500),
            main.LanguageIDE(4, 3, 1600),
            main.LanguageIDE(2, 6, 200),
            main.LanguageIDE(5, 5, 800),
            main.LanguageIDE(6, 5, 1200),
            main.LanguageIDE(5, 1, 200),
            main.LanguageIDE(4, 6, 700),
            main.LanguageIDE(1, 4, 500),
            main.LanguageIDE(3, 5, 300),
            main.LanguageIDE(2, 2, 400),
            main.LanguageIDE(6, 3, 600),
        ]

        self.one_to_many = main.create_one_to_many(self.ides, self.languages)
        self.many_to_many = main.create_many_to_many(self.languages_ides, self.languages, self.ides)

    def test_first_task_method(self):
        result = [(i[2],i[0]) for i in main.task_1(self.one_to_many, 'V')]
        true_result = [('Visual Studio Code', 'JavaScript'),
                       ('Visual Studio Code', 'Go'),
                       ('Visual Studio', 'C#')]
        self.assertEqual(result, true_result)

    def test_second_task_method(self):
        result = main.task_2(self.many_to_many)
        true_result = [('Sublime Text', 800),
                       ('PyCharm', 1000),
                       ('Visual Studio', 1200),
                       ('IntelliJ IDEA', 1500),
                       ('Eclipse', 1600),
                       ('Visual Studio Code', 2000)]
        self.assertEqual(result, true_result)

    def test_third_task_method(self):
        result = [(i[1], i[0]) for i in main.task_3(self.many_to_many)]
        true_result = [('Eclipse', 'C++'),
                       ('Eclipse', 'Go'),
                       ('IntelliJ IDEA', 'C#'),
                       ('IntelliJ IDEA', 'Java'),
                       ('PyCharm', 'JavaScript'),
                       ('PyCharm', 'Python'),
                       ('Sublime Text', 'C#'),
                       ('Sublime Text', 'Python'),
                       ('Visual Studio', 'C#'),
                       ('Visual Studio', 'C++'),
                       ('Visual Studio Code', 'Go'),
                       ('Visual Studio Code', 'Java'),
                       ('Visual Studio Code', 'JavaScript')]
        self.assertEqual(result, true_result)


if __name__ == '__main__':
    unittest.main()
