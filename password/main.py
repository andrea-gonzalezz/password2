import hashlib
import string
import json


try:
    with open("mdp.json", "a+") as f:
        hache_mdp = json.load(f)

except:
    hache_mdp = {}




#-------FONCTION POUR VERIFIER LES CARACTERES EXIGES PAR LE MDP


def verifier(mdp):
    caractere_speciaux = ["!","@","#", "$", "%", "^", "&", "*"]
    val = True

    if len(mdp) < 8:
        print("Le mot de passe doit contenir au moins 8 caractères")
        val = False
    if not any (char.isdigit() for char in mdp):
        print("Le mot de passe doit comporter au moins un chiffre")
    if not any(char.isupper() for char in mdp):
        print("Le mot de passe doit comporter au moins une minuscule")
        val = False
    if not any(char.islower() for char in mdp):
        print("Le mot de passe doit comporter au moins une majuscule")
        val = False
    if not any(char in caractere_speciaux for char in mdp):
        print("Le mot de passe doit comporter au moins un caractère spécial")
    if val:
        return val


def hashpasswrd(mot_de_passe):
    mdp_hache = hashlib.sha256(mot_de_passe.encode()).hexdigest()
    return mdp_hache

def print_mdp_hache(mot_de_passe):
    print("le mot de passe haché est : ", hashpasswrd(mot_de_passe))

#--------- FONCTION QUI AFFICHE SI LE MOT DE PASSE EST VALIDE OU PAS
def printverif(mdp):
    if verifier(mdp) == False:
        print("Le mot de passe n'est pas valide")
    elif verifier(mdp) == True:
        print("Le mot de passe est valide")
# if __name__ == '__main__':
#     main()


#-------FONCTION POUR REDEMANDER LE MDP SIL NE REMPLI PAS LES CONDITIONS EXIGEES

def saisi_mdp():
    while True:
        mdp = input("Entrez votre mot de passe: ")
        verif = verifier(mdp)
        if verif != True:
            print(verif)
        else:
            print("le mot de pass est valide ")
            mot_de_passe = hashpasswrd(mdp)
            return mot_de_passe

# RECUPERATION DU NOM DE L'UTILISATEUR + VERIFICATION ET AJOUT DANS LE DOSSIER JSON

nom = input("Quel est votre nom d'utilisateur ?: ")
mot_de_passe = saisi_mdp()
if nom in hache_mdp:
    if mot_de_passe in hache_mdp[nom]:
        print("Mot de passe déjà utilisé.")
    elif mot_de_passe not in hache_mdp[nom]:
        hache_mdp[nom] += [mot_de_passe]
        print("mot de passe ajouté")
else:
    hache_mdp[nom] = [mot_de_passe]
    print("mot de passe ajouté dans l'historique")

affich_mot_de_passe = input("Souhaitez-vous afficher l'ensemble de vos mots de passe ? (oui ou non) ")
if affich_mot_de_passe.lower() == "oui":
    print(hache_mdp[nom])

with open("user-mdp.json", "a+") as f:
    json.dump(hache_mdp, f, separators=(",", " : "), indent=4)


def convert_data_to_json(user, hex_hash):
    try:
        with open("data.json", "a+", encoding='utf-8') as fichier:
            dic = json.load(fichier)
    except:
        dic = {}
    if user in dic:
        if hex_hash not in dic[user]:
            dic[user] += [hex_hash]
    elif user not in dic:
        dic[user] = [hex_hash]
    with open("data.json", "a+", encoding='utf-8') as fichier:
        json.dump(dic, fichier, indent=2, separators=(',', ': '), ensure_ascii=False)