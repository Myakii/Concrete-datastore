import requests

#Création d'un compte
url = "https://hire-game.netsach.dev/api/v1.1/auth/register/"
data = {
    "email": "lili_yang@hotmail.fr",
    "password1": "12345678910ABCD",
    "password2": "12345678910ABCD",
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print('Inscription réussie !')
    print('Informations :', response.json())
else:
    print('Erreur', response.text)

#Identification d'un compte
url = "https://hire-game.netsach.dev/api/v1.1/auth/login/"
data = {
    "email": "lili_yang@hotmail.fr",
    "password": "12345678910ABCD",
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('Connexion réussie !')
    print('Informations :', response.json())
else:
    print('Erreur', response.text)

#Utilisation de la méthode "GET" pour récupérer les informations du compte avec le token
url = "https://hire-game.netsach.dev/api/v1.1/account/me/"
headers = {
    "Authorization": "Token 17e2379dea8f6c980ae8e8888cb3e3e11513dcbd"
    }
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print('Connexion réussie !')
    print('Informations :', response.json())
else:
    print('Erreur', response.text)

#Création d'application, effectuer des requête POST sur https://hire-game.netsach.dev/api/v1.1/job-application-request/
#Ajout de l'email, first_name, last_name
url = "https://hire-game.netsach.dev/api/v1.1/job-application-request/"
data = {
    "email": "lili_yang@hotmail.fr",
    "first_name" : "Rosine",
    "last_name" : "YANG",
    }

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print('Connexion réussie !')
    print('Informations :', response.json())
else:
    print('Erreur', response.text)

#Effectuer des méthodes get jusqu'à que le "status" soit "COMPLETED"
#+ confirmation_url : https://hire-game.netsach.dev/api/v1.1/job-application-confirmation-request/8d9a3e87-37d9-49f0-9afa-360b173a4c05/
url = "https://hire-game.netsach.dev/api/v1.1/job-application-request/ac614b7e-5a89-43b4-868f-fcb9c46aaa8b/"

while True:
    response = requests.get(url, headers=headers)
    data = response.json()
    status = data.get("status")
    if status == "COMPLETED":
        confirmation_url = data.get('confirmation_url')
        if confirmation_url:
            print('DONE')
            print('confirmation_url :', confirmation_url)
            break

#Confirmation Application
url = "https://hire-game.netsach.dev:443/api/v1.1/job-application-confirmation-request/5929f1b3-e6b5-4e91-a707-964c86c365d9/"

patch_data = {
    "confirmed": True
}

response = requests.patch(url, headers=headers, json=patch_data)

if response.status_code == 200:
    print("Mise à jour réussie !")
    updated_data = response.json()
    print("Données mises à jour :", updated_data)
else:
    print("Erreur lors de la mise à jour :", response.text)