from flask import Flask, render_template

import utils

# app = Flask(__name__,template_folder='./', static_folder='./')
app = Flask(__name__)

path = 'https://jsonkeeper.com/b/DYDL'


@app.route("/")
def main():
    candidates = utils.load_candidates_from_json(path)
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<candidate_id>")
def identification(candidate_id):
    candidate_info = utils.get_candidate_by_id(candidate_id)
    return render_template("single.html", candidate_info=candidate_info)


@app.route("/skills/<skill_name>/")
def skills(skill_name):
    candidates_with_skill = utils.get_candidates_by_skill(skill_name)

    return render_template("skill.html", candidates_with_skill=candidates_with_skill,
                           count_candidates=len(candidates_with_skill))


@app.route("/search/<candidate_name>")
def search(candidate_name):
    candidates_name = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates_name=candidates_name, candidates_with_name=len(candidates_name))


app.run()
