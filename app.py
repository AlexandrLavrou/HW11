from flask import Flask

import utils

app = Flask(__name__)

path = 'https://jsonkeeper.com/b/DYDL'


@app.route("/")
def main():
    return utils.load_candidates_names(path)


@app.route("/skills/<skill_name>/")
def skills(skill_name):
    return f"<h3>{utils.get_candidates_by_skill(path, skill_name)}</h3>"


@app.route("/candidate/<candidate_id>/")
def identification(candidate_id):
    return f"<h3>{utils.get_candidate_by_id(candidate_id, path)}"


@app.route("/names/<candidate_name>/")
def names(candidate_name):
    return f"<h3>{utils.get_candidates_by_name(path, candidate_name)}"


app.run()
