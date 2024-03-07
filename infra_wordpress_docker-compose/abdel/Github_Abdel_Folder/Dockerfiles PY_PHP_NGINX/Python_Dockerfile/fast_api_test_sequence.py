#!/usr/bin/env python3

import requests

def main():
    # URL du site WordPress à interroger
    url = 'https://example.com'

    try:
        # Effectuer la requête GET vers le site WordPress
        response = requests.get(url)

        # Vérifier si la requête a réussi (code de statut 200)
        if response.status_code == 200:
            # Récupérer le contenu HTML de la page
            html_content = response.text

            # Chercher une occurence spécifique dans le contenu HTML
            keyword = 'votre_mot_clé'
            if keyword in html_content:
                print(f"L'occurrence '{keyword}' a été trouvée sur le site WordPress.")
            else:
                print(f"L'occurrence '{keyword}' n'a pas été trouvée sur le site WordPress.")
        else:
            print(f"La requête GET vers {url} a échoué avec le code de statut {response.status_code}.")
    
    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête vers {url}: {e}")

if __name__ == "__main__":
    main()
