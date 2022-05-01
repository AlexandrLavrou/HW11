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


def get_candidate_by_id(candidate_id):
    """
    Функция загружает из файла список сущностей класса Candidates
     и возвращает данные кандидата по ID
    :param candidate_id: Входящий ID
    :return: возвращает данные кандидата с запрашиваемым ID в рекомендуемой форме
    """
    candidates = load_candidates_from_json(path)
    for _c in candidates:
        if int(candidate_id) == _c.ident:
            return _c
    return None


path = 'https://jsonkeeper.com/b/DYDL'


# def get_candidate_by_name(candidate_name):
#     """
#     Функция загружает из файла список сущностей класса Candidates
#      и возвращает данные кандидата по ID
#     :param candidate_name: Входящий ID
#     :return: возвращает данные кандидата с запрашиваемым ID в рекомендуемой форме
#     """
#     candidates = load_candidates_from_json(path)
#     for _c in candidates:
#         if candidate_name in _c.name.split(", "):
#             return _c


def get_candidates_by_skill(skill_name):
    """
    Функция загружает из файла список сущностей класса Candidates
    и формирует список кандидатов с запрашиваемыми навыками в заданном формате
    :param skill_name: входящий навык
    :return: возвращает список кандидатов с запрашиваемым навыком
    """

    _candidates = load_candidates_from_json(path)
    candidates_with_skill = []

    for _c in _candidates:
        list_skill = _c.skills.split(", ")
        for _skill in list_skill:
            if skill_name.lower() == _skill.lower():
                candidates_with_skill.append(_c)
            else:
                continue

    candidates_with_skill = list(set(candidates_with_skill))

    return candidates_with_skill


# path = 'https://jsonkeeper.com/b/DYDL'
# print(get_candidates_by_skill("spam"))
#
# for candidate in get_candidates_by_skill("spam"):
#
#     print(candidate.name)

def get_candidates_by_name(candidate_name):
    """
    Функция загружает из файла список сущностей класса Candidates
     и возвращает данные кандидатов по имени или его части
    :param candidate_name: имя кандидата введенного пользователем
    :return: возвращает список кандидатов по имени или его части
    """
    _candidates = load_candidates_from_json(path)
    candidates_name = []
    for _c in _candidates:
        list_name = _c.name.split(", ")
        for _name in list_name:
            if candidate_name.lower() in _name.lower():
                candidates_name.append(_c)
            else:
                continue

    candidates_name = list(set(candidates_name))

    return candidates_name
