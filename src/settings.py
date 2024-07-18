import pathlib
from configparser import ConfigParser


HH_URL = "https://api.hh.ru/vacancies"  # Ссылка для парсинга вакансий

ROOT_PATH = pathlib.Path(__file__).parent.parent  # Корневой путь

DATA_PATH = ROOT_PATH.joinpath("data")  # Путь к папки data

DATABASE_PATH = DATA_PATH.joinpath("database.ini")  # Путь к настройкам базы данных

DB_NAME = 'hh'  # Имя базы данных


def config(filename=DATABASE_PATH, section="postgresql") -> dict:
    # Парсера чтения настроек для базы данных
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(
            "Section {0} is not found in the {1} file.".format(section, filename))
    return db
