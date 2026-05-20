from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Reponses(BaseModel):
    q1: str
    q2: str
    q3: str
    q4: str
    q5: str
    q6: str

formations = {
    "menuiserie": [
        "Formation menuiserie",
        "CAP Menuisier",
        "Formation fabrication de meubles"
    ],
    "decoration": [
        "Formation décoration d’intérieur",
        "Formation design d’espace",
        "Formation home staging"
    ],
    "reparation": [
        "Formation réparation d’objets",
        "Formation maintenance",
        "Formation bricolage pratique"
    ],
    "batiment": [
        "Formation métiers du bâtiment",
        "Formation rénovation",
        "Formation chantier et travaux"
    ],
    "artisanat": [
        "Formation artisanat créatif",
        "Formation fabrication d’objets",
        "Formation création manuelle"
    ]
}

@app.get("/")
def accueil():
    return {"message": "API de recommandation active"}

@app.post("/recommendations")
def recommander(reponses: Reponses):
    scores = {
        "menuiserie": 0,
        "decoration": 0,
        "reparation": 0,
        "batiment": 0,
        "artisanat": 0
    }

    texte = " ".join(reponses.dict().values()).lower()

    if "construire" in texte or "meuble" in texte or "bois" in texte or "atelier" in texte:
        scores["menuiserie"] += 2

    if "décorer" in texte or "design" in texte or "créatif" in texte or "couleur" in texte:
        scores["decoration"] += 2

    if "réparer" in texte or "panne" in texte or "cassé" in texte or "outil" in texte:
        scores["reparation"] += 2

    if "chantier" in texte or "extérieur" in texte or "travaux" in texte or "rénovation" in texte:
        scores["batiment"] += 2

    if "fabriquer" in texte or "objet" in texte or "manuel" in texte or "personnaliser" in texte:
        scores["artisanat"] += 2

    meilleur_profil = max(scores, key=scores.get)

    return {
        "profil": meilleur_profil,
        "formations_recommandees": formations[meilleur_profil],
        "scores": scores
    }