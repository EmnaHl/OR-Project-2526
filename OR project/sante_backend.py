# sante_backend.py
import json
import random


def generate_infirmieres(n):
    """Génère automatiquement N employés (hommes + femmes) avec données réalistes et CIN unique"""

    prenoms_femmes = [
        "Sarah", "Lina", "Nadia", "Amel", "Meriem", "Sana", "Nesrine", "Souha", "Wafa",
        "Yasmine", "Amina", "Farah", "Rania", "Imen", "Salma", "Mouna", "Hiba",
        "Dorra", "Asma", "Ines", "Leila", "Maya", "Rim", "Sabrine", "Sonia"
    ]

    prenoms_hommes = [
        "Ahmed", "Mehdi", "Omar", "Hatem", "Rami", "Nader", "Youssef", "Walid",
        "Firas", "Anis", "Bilel", "Majdi", "Skander", "Mohamed", "Aymen", "Karim",
        "Seif", "Rayen", "Saber", "Foued", "Tarek", "Zouheir", "Khalil", "Nassim"
    ]

    noms = [
        "Ben Ali", "Kacem", "Trabelsi", "Hammami", "Jlassi", "Mokni", "Ayari", "Bouzid",
        "Gharbi", "Zribi", "Mansour", "Chouikha", "Fakhfakh", "Khalfi",
        "Mahjoub", "Sassi", "Toumi", "Zouari", "Riahi", "Dahmani", "Bouazizi",  "Saidi" , "Hamrouni", "Jemai"
        , "Khaled", "Laaribi", "Miled", "Najar", "Oueslati", "Rafrafi", "Sfar", "Tounsi"
        , "Zidi", "Bennour", "Chebbi", "Dakhlaoui", "Fendri", "Guesmi", "Hajji", "Ismail", "Jaballah", "Kefi", 
        "Masmoudi", "Nejib", "Othmani", "Rekik", "Sbai", "Touati" ,"Ajili"
    ]

    specialites = [
        "Urgences", "Pédiatrie", "Chirurgie", "Oncologie",
        "Cardiologie", "Réanimation", "Soins intensifs"
    ]

    employees = []
    used_cin = set()  # garantir l'unicité des CIN

    for i in range(n):

        # Sexe aléatoire
        sexe = random.choice(["Homme", "Femme"])

        if sexe == "Femme":
            prenom = random.choice(prenoms_femmes)
        else:
            prenom = random.choice(prenoms_hommes)

        nom = random.choice(noms)

        # Génération d’un CIN unique (8 chiffres en Tunisie)
        cin = str(random.randint(10000000, 99999999))
        while cin in used_cin:
            cin = str(random.randint(10000000, 99999999))

        used_cin.add(cin)

        employees.append({
            "id": f"INF-{i+1}",
            "prenom": prenom,
            "nom": nom,
            "sexe": sexe,
            "cin": cin,
            "age": random.randint(23, 55),
            "specialite": random.choice(specialites),
        })

    return employees


def save_sante_data(x, y, infirmieres):
    """Enregistre toutes les données dans un fichier JSON"""

    data = {
        "siege": {"x": x, "y": y},
        "nb_infirmieres": len(infirmieres),
        "infirmieres": infirmieres
    }

    with open("sante_data.json", "w") as f:
        json.dump(data, f, indent=4)
