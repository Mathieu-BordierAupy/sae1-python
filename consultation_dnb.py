# pyright: ignore[reportAttributeAccessIssue]

from html import escape
import os
from pprint import pprint

# from explore_dnb import Resultat, charger_resultats
import explore_dnb as dnb
from flask import Flask, flash, redirect, render_template, request, session, url_for

# Ici vos fonctions dédiées aux interactions
ALLOWED_EXTENSIONS = {"csv"}
UPLOAD_FOLDER = os.path.join("staticFiles", "uploads")

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.secret_key = "12345"

table: list[dnb.Resultat] = []


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
    session["csv_name"] = None
    if os.path.exists(session["csv_path"]):
        os.remove(session["csv_path"])
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
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

        results = dnb.filtre_session(table, session_act)
        total = dnb.taux_reussite_global(table, session_act)
        if total is not None:
            total = round(total, 2)

        info = {
            "taux_reussite_global": total or "N/A",
            "meilleur_college": dnb.meilleur_college(table, session_act),
            "total": dnb.total_admis_presents(results) or ["N/A"],
        }

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
        results = dnb.filtre_college_non_dep(table, nom) if len(nom) > 0 else []
    else:
        results = dnb.filtre_college(table, nom, dep)

    return render_template("index.html", results=results, information=information)


@app.route("/success/<file>")
def success(file: str):
    global table
    flash(f"Opened {escape(file)}!")
    return redirect(url_for("index"))


@app.route("/open", methods=["POST", "GET"])
def open_file():
    global table
    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file part")
            return redirect("/")

        session["csv_name"] = ""

        for file in request.files.getlist("file"):
            print(file.filename)
            if file.filename == "":
                flash("No selected file")
                return redirect("/")

            if file is not None:
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], "table.csv"))
                session["csv_name"] = f"{session["csv_name"]} {file.filename}"
                session["csv_path"] = os.path.join(
                    app.config["UPLOAD_FOLDER"], "table.csv"
                )
                new_table = dnb.charger_resultats(session["csv_path"])

                if new_table is None:
                    flash("Can't load file")
                    return redirect("/")

                table = dnb.fusionner_resultats(table, new_table)
                print(len(table))

        return redirect(url_for("success", file=session["csv_name"]))
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
    app.run()
    # Cleanup before exiting...
    if os.path.exists(os.path.join(UPLOAD_FOLDER, "table.csv")):
        os.remove(os.path.join(UPLOAD_FOLDER, "table.csv"))
    if os.path.exists(UPLOAD_FOLDER):
        os.removedirs(UPLOAD_FOLDER)


if __name__ == "__main__":
    programme_principal()
