from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

PATH_CANDIDATES = 'candidates.json'
candidates = load_candidates_from_json(PATH_CANDIDATES)


app = Flask(__name__)


@app.route('/')
def get_all_user():
    return render_template('list.html', candidates=candidates)

@app.route('/candidate/<int:x>')
def get_one_user(x):
    item = get_candidate(x, candidates)
    if item:
        return render_template('single.html', item=item)
    return "Not Found"

@app.route('/search/<candidate_name>')
def get_user_by_name(candidate_name):
    items = get_candidates_by_name(candidate_name, candidates)
    if items:
        return render_template('single.html', candidates=items)
    return "Not Found"

@app.route('/skill/<skill_name>')
def get_user_by_skill(skill_name):
    items = get_candidates_by_skill(skill_name, candidates)
    if items:
        return render_template('skill.html', skill=skill_name, candidates=items)
    return "Not Found"

app.run()