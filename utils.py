
# - `load_candidates_from_json(path)` – возвращает список всех кандидатов
# - `get_candidate(candidate_id)` – возвращает одного кандидата по его id
# - `get_candidates_by_name(candidate_name)` – возвращает кандидатов по имени
# - `get_candidates_by_skill(skill_name)` – возвращает кандидатов по навыку
import requests


def load_candidates_from_json(path):
    _candidates = requests.get(path).json()
    candydates_inclass = []
    for _ in _candidates:


