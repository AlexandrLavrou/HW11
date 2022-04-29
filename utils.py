
import requests

import candidat


def load_candidates_from_json(path):
    """
    Функция загружает из файла JSON список из
    экземпляров класса Candidates
    :return:
    """
    _candidates = requests.get(path).json()
    candidates_in_class = []
    for _ in _candidates:
        ident = _.get("id")
        name = _.get("name")
        picture = _.get("picture")
        position = _.get("position")
        skills = _.get("skills")

        candidate = candidat.Candidates(ident, name, picture, position, skills)
        candidates_in_class.append(candidate)

    return candidates_in_class

path = 'https://jsonkeeper.com/b/DYDL'

candys = load_candidates_from_json(path)
for candy in candys:
    print(candy.ident)

def load_candidates_names(path):
    """
    Функция загружает из файла JSON список имена кандидатов
    """
    _candidates = load_candidates_from_json(path)
    name_ = []
    for _c in _candidates:
        name_.append(_c.get_candy_name())
    return name_

# path = 'https://jsonkeeper.com/b/DYDL'
# print(load_candidates_names(path))

def get_candidate_by_id(candidate_id):
    """
    Функция загружает из файла список сущностей класса Candidates
     и возвращает данные кандидата по ID
    :param candidate_id: Входящий ID
    :return: возвращает данные кандидата с запрашиваемым ID в рекомендуемой форме
    """
    candidates = load_candidates_from_json(path)
    for _c in candidates:
        if _c.chek_candy_by_id(candidate_id):
            return _c.chek_candy_by_id(candidate_id)


def get_candidates_by_name(path, candidate_name):
    """
    Функция загружает из файла список сущностей класса Candidates
     и возвращает данные кандидатов по имени или его части
    :param path: путь к файлу Json
    :param candidate_name: имя кандидата введенного пользователем
    :return: возвращает список кандидатов по имени или его части
    """
    _candidates = load_candidates_from_json(path)
    candy_with_name = []
    for _c in _candidates:
        if _c.check_candy_name(candidate_name):
            candy_with_name.append(_c.check_candy_name(candidate_name))
    return candy_with_name


def get_candidates_by_skill(path, skill_name):
    """
    Функция загружает из файла список сущностей класса Candidates
    и формирует список кандидатов с запрашиваемыми навыками в заданном формате
    :param path: путь к файлу Json
    :param skill_name: входящий навык
    :return: возвращает список кандидатов с запрашиваемым навыком
    """
    _candidates = load_candidates_from_json(path)
    candy_with_skill = ""
    for _c in _candidates:
        if _c.check_candy_skill(skill_name):
            candy_with_skill += _c.check_candy_skill(skill_name)
    return candy_with_skill
