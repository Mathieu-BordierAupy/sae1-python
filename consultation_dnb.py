# pyright: ignore[reportAttributeAccessIssue]

from html import escape
import os

# from explore_dnb import Resultat, charger_resultats
import explore_dnb as dnb
from flask import Flask, flash, redirect, render_template, request, session, url_for

# Ici vos fonctions dédiées aux interactions
ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = os.path.join("staticFiles", "uploads")
app.secret_key = "12345"

table: list[dnb.Resultat] = []

BASE_HTML = """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>DNB Explorer</title>
    <style>
      body { font-family: system-ui, -apple-system, Roboto, 'Helvetica Neue', Arial; padding: 20px; }
      .container { max-width: 900px; margin: 0 auto; }
      header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; }
      table { border-collapse: collapse; width:100%; }
      th, td { border:1px solid #ddd; padding:8px; text-align:left; }
      th { background:#f4f4f4; }
      .card { border:1px solid #eee; padding:12px; margin-bottom:12px; border-radius:8px; }
      .compare { display:flex; gap:12px; }
      .col { flex:1; }
      .muted { color:#666; font-size:0.9em }
      .actions { margin-top:12px }
      .btn { background:#0366d6; color:white; padding:8px 12px; border-radius:6px; text-decoration:none }
      input, select { padding:6px; }
    </style>
  </head>
  <body>
    <div class="container">
      <header>
        <h1>DNB Explorer</h1>
        <nav>
          <a href="{{ url_for('index') }}">Recherche</a> |
          <a href="{{ url_for('compare') }}">Comparer</a>
        </nav>
      </header>
      {% block content %}{% endblock %}
    </div>
  </body>
</html>
"""

INDEX_HTML = """{% extends 'base.html' %}
{% block content %}
  <div class="card">
    <form method="get" action="{{ url_for('index') }}">
      <label>Nom (fragment) : <input name="nom" value="{{ request.args.get('nom','') }}"></label>
      <label> Département : <input name="departement" value="{{ request.args.get('departement','') }}" style="width:80px"></label>
      <button class="btn" type="submit">Rechercher</button>
    </form>
  </div>

  {% if results is not none %}
    <h2>Résultats ({{ results|length }})</h2>
    {% if results %}
      <table>
        <thead><tr><th>Année</th><th>Nom</th><th>Dépt</th><th>Présents</th><th>Admis</th><th>Taux</th><th>Actions</th></tr></thead>
        <tbody>
          {% for r in results %}
            <tr>
              <td>{{ r[0] }}</td>
              <td>{{ r[1] }}</td>
              <td>{{ r[2] }}</td>
              <td>{{ r[3] }}</td>
              <td>{{ r[4] }}</td>
              <td>{% if r[3] > 0 %}{{ ('%.2f' % ((r[4]/r[3])*100)) }} %{% else %}N/A{% endif %}</td>
              <td>
                <a href="{{ url_for('college', nom=r[1], departement=r[2]) }}">Voir</a>
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    {% else %}
      <p class="muted">Aucun résultat.</p>
    {% endif %}
  {% endif %}
{% endblock %}
"""

COLLEGE_HTML = """{% extends 'base.html' %}
{% block content %}
  <a href="{{ url_for('index') }}">← Retour</a>
  <h2>Détails du collège: {{ nom }} ({{ departement }})</h2>

  <div class="card">
    <p><strong>Moyenne des taux :</strong> {% if moyenne is not none %}{{ '%.2f' % moyenne }} %{% else %}N/A{% endif %}</p>
    <p><strong>Total admis / présents (toutes sessions) :</strong> {{ totals[0] if totals else 'N/A' }} / {{ totals[1] if totals else 'N/A' }}</p>
    <p><strong>Années disponibles :</strong> {{ annees|join(', ') }}</p>
  </div>

  <h3>Par session</h3>
  <table>
    <thead><tr><th>Année</th><th>Présents</th><th>Admis</th><th>Taux</th></tr></thead>
    <tbody>
      {% for r in sessions %}
        <tr>
          <td>{{ r[0] }}</td>
          <td>{{ r[3] }}</td>
          <td>{{ r[4] }}</td>
          <td>{% if r[3] > 0 %}{{ ('%.2f' % ((r[4]/r[3])*100)) }} %{% else %}N/A{% endif %}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
"""

COMPARE_HTML = """{% extends 'base.html' %}
{% block content %}
  <h2>Comparer deux collèges</h2>
  <form method="get" action="{{ url_for('compare') }}">
    <label>Nom 1: <input name="nom1" value="{{ request.args.get('nom1','') }}"></label>
    <label>Dépt 1: <input name="dep1" value="{{ request.args.get('dep1','') }}" style="width:80px"></label>
    <br>
    <label>Nom 2: <input name="nom2" value="{{ request.args.get('nom2','') }}"></label>
    <label>Dépt 2: <input name="dep2" value="{{ request.args.get('dep2','') }}" style="width:80px"></label>
    <div class="actions"><button class="btn" type="submit">Comparer</button></div>
  </form>

  {% if left or right %}
    <div class="compare">
      <div class="col card">
        <h3>{{ left_name or 'Aucun' }}</h3>
        {% if left %}
          <p><strong>Moyenne:</strong> {{ '%.2f' % left.moyenne }} %</p>
          <p><strong>Totals:</strong> {{ left.totals[0] }} / {{ left.totals[1] }}</p>
          <p><strong>Années:</strong> {{ left.annees|join(', ') }}</p>
        {% else %}
          <p class="muted">Aucun collège trouvé</p>
        {% endif %}
      </div>

      <div class="col card">
        <h3>{{ right_name or 'Aucun' }}</h3>
        {% if right %}
          <p><strong>Moyenne:</strong> {{ '%.2f' % right.moyenne }} %</p>
          <p><strong>Totals:</strong> {{ right.totals[0] }} / {{ right.totals[1] }}</p>
          <p><strong>Années:</strong> {{ right.annees|join(', ') }}</p>
        {% else %}
          <p class="muted">Aucun collège trouvé</p>
        {% endif %}
      </div>
    </div>
  {% endif %}
{% endblock %}
"""


def ensure_templates():
    os.makedirs("templates", exist_ok=True)
    paths = {
        "templates/base.html": BASE_HTML,
        "templates/index.html": INDEX_HTML,
        "templates/college.html": COLLEGE_HTML,
        "templates/compare.html": COMPARE_HTML,
    }
    for p, content in paths.items():
        if not os.path.exists(p):
            with open(p, "w", encoding="utf-8") as f:
                f.write(content)


def info_college(nom: str, departement: int):
    """Rassemble toute les information d'un college dans un seul objet"""

    sessions = dnb.filtre_college(table, nom, departement)
    if not sessions:
        return None
    totals = dnb.total_admis_presents(sessions)
    moyenne = dnb.moyenne_taux_reussite_college(table, nom, departement)
    annees = sorted(set(r[0] for r in sessions))
    # sort sessions by year for display
    sessions_sorted = sorted(sessions, key=lambda r: r[0])

    class C:
        pass

    obj = C()
    obj.sessions = sessions_sorted
    obj.totals = totals
    obj.moyenne = moyenne
    obj.annees = annees
    return obj


@app.route("/")
def home():
    return render_template("file.html")


@app.route("/sessions", methods=["POST", "GET"])
def sessions():
    global table

    if table == []:
        return redirect("/")

    sessions_list = dnb.liste_sessions(table)
    info, results = None, None

    if request.method == "POST":
        session_act = request.form.get("session")
        try:
            if session_act is None:
                raise ValueError
            session_act = int(session_act)
        except ValueError:
            return redirect(url_for("sessions"))

        if session_act not in sessions_list:
            return redirect(url_for("sessions"))

        info = {
            "taux_reussite_global": dnb.taux_reussite_global(table, session_act),
            "meilleur_college": dnb.meilleur_college(table, session_act),
        }
        results = dnb.filtre_session(table, session_act)

    return render_template(
        "session.html", sessions_list=sessions_list, results=results, info=info
    )


@app.route("/index", methods=["POST", "GET"])
def index():
    global table

    if table == []:
        return redirect("/")

    information = {
        "periode_amelioration": dnb.plus_longue_periode_amelioration(table) or "N/A",
        "meilleur_taux_reussite": dnb.meilleur_taux_reussite(table),
        "pire_taux_reussite": dnb.pire_taux_reussite(table),
        "total_admis_presents": dnb.total_admis_presents(table),
    }

    nom = request.form.get("nom", "").strip()
    departement = request.form.get("departement", "").strip()

    try:
        dep = int(departement)
    except ValueError:
        return render_template("index.html", results=[], information=information)

    results = dnb.filtre_college(table, nom, dep)
    return render_template("index.html", results=results, information=information)


@app.route("/success/<file>")
def success(file: str):
    global table
    flash(f"Opened {escape(file)}!")
    print(len(table))
    return redirect(url_for("index"))


@app.route("/open", methods=["POST", "GET"])
def open_file():
    global table
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect("/")

        file = request.files["file"]

        if file.filename == "":
            flash("No selected file")
            return redirect("/")

        if file is not None:
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], "table.csv"))
            session["csv_name"] = file.filename
            session["csv_path"] = os.path.join(app.config["UPLOAD_FOLDER"], "table.csv")
            new_table = dnb.charger_resultats(session["csv_path"])

            if new_table is None:
                flash("Can't load file")
                return redirect("/")
            table = new_table
            return redirect(url_for("success", file=file.filename))
    return redirect("/")


@app.route("/college")
def college():
    if table == []:
        return redirect("/")

    nom = request.args.get("nom", "")
    try:
        dep = int(request.args.get("departement", ""))
    except Exception:
        return redirect(url_for("index"))
    data = info_college(nom, dep)
    sessions = data.sessions if data else []
    return render_template(
        "college.html",
        nom=nom,
        departement=dep,
        moyenne=(data.moyenne if data else None),
        totals=(data.totals if data else None),
        annees=(data.annees if data else []),
        sessions=sessions,
    )


@app.route("/compare")
def compare():
    if table == []:
        return redirect("/")

    nom1 = request.args.get("nom1", "").strip()
    nom2 = request.args.get("nom2", "").strip()
    dep1 = request.args.get("dep1", "").strip()
    dep2 = request.args.get("dep2", "").strip()
    left = right = None
    left_name = right_name = None
    if nom1 and dep1:
        try:
            d1 = int(dep1)
            left = info_college(nom1, d1)
            left_name = f"{nom1} ({d1})"
        except ValueError:
            left = None
    if nom2 and dep2:
        try:
            d2 = int(dep2)
            right = info_college(nom2, d2)
            right_name = f"{nom2} ({d2})"
        except ValueError:
            right = None
    return render_template(
        "compare.html",
        left=left,
        right=right,
        left_name=left_name,
        right_name=right_name,
    )


# ici votre programme principal
def programme_principal():
    # ensure_templates()
    app.run(debug=True)


if __name__ == "__main__":
    programme_principal()
