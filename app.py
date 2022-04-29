from flask import Flask, render_template

import utils

app = Flask(__name__)

path = 'https://jsonkeeper.com/b/DYDL'


@app.route("/")
def main():
    candidates = utils.load_candidates_from_json(path)
    return render_template("list.html", candidates=candidates)

@app.route("/candidate/<ident>/")
def identification(ident):
    candidates = utils.load_candidates_from_json(path)
    for _ in candidates:
        if int(input_id) == int(_.ident):
            return
th)
    return render_template()


@app.route("/skills/<skill_name>/")
def skills(skill_name):
    candidates = utils.load_candidates_from_json(path)

    return f"<h3>{utils.get_candidates_by_skill(path, skill_name)}</h3>"





@app.route("/names/<candidate_name>/")
def names(candidate_name):
    candidate_name_ = utils.get_candidates_by_name(path, candidate_name)
    return candidate_name_


app.run()
