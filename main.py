import json
import os


rate = [{'name': 'Backend Developer (Python)', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Архитектура и структура проекта: Аутентификация и авторизация: - Работа с системами аутентификации и авторизации в приложениях на <highlighttext>Python</highlighttext>. Оптимизация производительности: - Понимание...', 'url': 'https://hh.ru/vacancy/94290873'}, {'name': 'BackEnd-разработчик/в офисе', 'experience': 'От 1 года до 3 лет', 'salary_from': 80000, 'salary_to': 0, 'snippet': 'Доработка, развитие BackEnd (и/или FrontEnd) ключевого программного продукта. Участие в перспективных разработках ПО.', 'url': 'https://hh.ru/vacancy/94917691'}, {'name': 'Стажер по нагрузочному тестированию', 'experience': 'Нет опыта', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Проводить нагрузочное тестирование систем. Разрабатывать скрипты и эмуляторы работы пользователей. Работать с инструментами нагрузочного тестирования. Работать с базами данных. ', 'url': 'https://hh.ru/vacancy/94761311'}, {'name': 'Специалист по нагрузочному тестированию (Junior, ученик)', 'experience': 'Нет опыта', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Анализ документации и работа со статистикой. Работа с командой разработчиков и аналитиков. Разработка скриптов нагрузочного тестирования. Проведение тестов и анализ...', 'url': 'https://hh.ru/vacancy/95134261'}, {'name': 'Junior QA Automation', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Поддержка и развитие инфраструктуры автоматизированного тестирования. Тестирование веб-приложения: проведение функционального, нефункционального, интеграционного, ручного и автоматизированного тестирования (тестирование front, back...', 'url': 'https://hh.ru/vacancy/93816790'}, {'name': 'IOS developer', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 150000, 'snippet': 'Тебе предстоит создавать новые интересные фичи, оптимизировать и улучшать существующую кодовую базу. Необходимо:', 'url': 'https://hh.ru/vacancy/92031077'}, {'name': 'Системный Администратор (администратор БД)', 'experience': 'От 1 года до 3 лет', 'salary_from': 45000, 'salary_to': 0, 'snippet': None, 'url': 'https://hh.ru/vacancy/94536062'}, {'name': 'QA-специалист', 'experience': 'От 3 до 6 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Функциональное и регрессионное тестирование приложений Web/Mobile-приложений. Фиксирование ошибок в таск-трекер. Автоматизированное тестирования приложений. Подготовка отчетов о тестировании.', 'url': 'https://hh.ru/vacancy/92077169'}, {'name': 'Системный аналитик', 'experience': 'От 1 года до 3 лет', 'salary_from': 140000, 'salary_to': 0, 'snippet': 'Собирать и анализировать поступающие требования внутреннего заказчика. Преобразовывать функциональные требования в постановки конкретных задач для разработчиков. Согласовывать требования и задания...', 'url': 'https://hh.ru/vacancy/91356259'}, {'name': 'Web-разработчик (1 С Битрикс - Управление сайтом)', 'experience': 'От 1 года до 3 лет', 'salary_from': 80000, 'salary_to': 150000, 'snippet': 'Разработка и поддержка мобильных приложений на платформе React Native. Взаимодействие с дизайнерами, аналитиками и командой backend-разработчиков для создания новых...', 'url': 'https://hh.ru/vacancy/94765606'}, {'name': 'Ведущий инженер-программист', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Проектирование и разработка интеграций между системой приема платежей от населения - ПО еКассир и др. системами Банка. - Обновления ПО системы приема...', 'url': 'https://hh.ru/vacancy/94985963'}, {'name': 'Специалист по обработке данных', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Участие в разработках новых процессов, поддерживаемых направлением (SAS EG, опционально Oracle PL/SQL, <highlighttext>Python</highlighttext>, Tableau), доработка по результатам проведенной аналитики. ', 'url': 'https://hh.ru/vacancy/94545725'}, {'name': 'Web-тестировщик (офис)', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Тестирование корректности отображения web-компонентов на web-страницах по требованиям дизайн-системы(шаблонов) на различных ОС и браузерах. ', 'url': 'https://hh.ru/vacancy/94931009'}, {'name': 'Python разработчик', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Проектирование компонентов систем. Организация процесса разработки. Написание и ревью кода. Написание тестов на свой код. Наставление менее опытных коллег.', 'url': 'https://hh.ru/vacancy/89433789'}, {'name': 'Разработчик SQL/DWH (Junior)', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Написание SQL-кода (PL/pgSQL, T-SQL). Создание и отладка ETL-процедур. Документирование выполненных разработок. Анализ источников данных и бизнес...', 'url': 'https://hh.ru/vacancy/93987572'}, {'name': 'Программист (инженер 1-ой категории)', 'experience': 'От 1 года до 3 лет', 'salary_from': 35000, 'salary_to': 0, 'snippet': 'Разработка программного обеспечения для микроконтроллеров, мобильных ОС Android, Аврора, OCLinux: Разработка программной документации и материалов для эксплуатационной документации. ', 'url': 'https://hh.ru/vacancy/95175626'}, {'name': 'Разработчик Python', 'experience': 'От 3 до 6 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Разработка безопасной среды виртуализации. Разработка сервиса для оптимизации развертывания, настройки и управления виртуализированными сетевыми функциями. Разработка интерфейсов и компонентов, реализующих...', 'url': 'https://hh.ru/vacancy/92442575'}, {'name': 'Менеджер направления отчетности и аналитики (SQL)', 'experience': 'Нет опыта', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Автоматизировать процессы и отчетность. Подготавливать аналитические выгрузки по запросу. Разрабатывать и поддерживать отчетность. Разрабатывать аналитические дашборды.', 'url': 'https://hh.ru/vacancy/94634787'}, {'name': 'Python developer (Flask/Fastapi)', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Разработка новых приложений и сервисов, а также доработка и сопровождение существующих. Участие в проектировании архитектуры, выработке решений по отказоустойчивости и...', 'url': 'https://hh.ru/vacancy/93663738'}, {'name': 'Преподаватель робототехники | программирования', 'experience': 'От 1 года до 3 лет', 'salary_from': 0, 'salary_to': 0, 'snippet': 'Вести занятия, согласно утвержденному расписанию. Следить за сохранностью высокотехнологичного оборудования, используемого в учебном процессе. Разрабатывать программы по своему направлению, учитывая...', 'url': 'https://hh.ru/vacancy/95272591'}]


class JsonSaver:
    def __init__(self, file_json, mode="r"):
        self.file_json = file_json
        self.mode = mode

    def add_vacancy(self, data):
        with open(self.file_json, self.mode) as outfile:
            if os.stat(self.file_json).st_size == 0:
                json.dump(data, outfile, ensure_ascii=False, indent=4)
            else:
                load_outfile = json.load(outfile)
                outfile.seek(0)
                [load_outfile.append(item) for item in data]
                json.dump(load_outfile, outfile, ensure_ascii=False, indent=4)

    def delete_vacancy(self, name: str):
        with open(self.file_json, self.mode) as outfile:
            if not os.stat(self.file_json).st_size == 0:
                text = json.load(outfile)
                new_len = []
                for i in range(len(text)):
                    if text[i]['name'] == name:
                        new_len.append(i)
                new_len2 = new_len[::-1]
                print(new_len2)
                for i in new_len2:
                    del text[i]
                print(len(text))
            else:
                print("Файл пустой")
        with open(self.file_json, "w") as outfile:
            json.dump(text, outfile, ensure_ascii=False, indent=4)


# Получаем путь до json файла
path_json = os.path.abspath('data/vacancies.json')
# Создаем экземпляр класса
save_file = JsonSaver(path_json, "r+")
# Сохраняем вакансии
save_file.add_vacancy(rate)
save_file.delete_vacancy("Преподаватель робототехники | программирования")
