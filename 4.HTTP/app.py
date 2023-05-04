import requests
import json

url = "https://localhost:44370/api/Category/categories/"
urll = "https://localhost:44370/api/Category/"

while True:
    print("\nMeniu:")
    print("1. Afiseaza lista de categorii")
    print("2. Afiseaza detalii despre o categorie")
    print("3. Creaza o categorie nou")
    print("4. Sterge o categorie")
    print("5. Redenumeste o categorie")
    print("6. Adauga un produs intro categorie")
    print("7. Afiseaza produsele dintro categorie")
    print("8. Exit")
    optiune = input("\nIntroduceti numarul optiunii: ")

    if optiune == "1":
        response = requests.get(url)

        if response.status_code == 200:
            categorii = json.loads(response.text)

            print("Lista de categorii:")
            for categorie in categorii:
                print(f"ID: {categorie['id']} - Name: {categorie['name']}")
        else:
            print(f"Nu sa putut obtine lista.")

    elif optiune == "2":
        categorie_id = input("\nIntrodu ID-ul categoriei pentru a vedea detalii: ")

        response_categorie = requests.get(url + categorie_id)

        if response_categorie.status_code == 200:
            categorie = json.loads(response_categorie.text)

            print("\nDetalii despre categoria:")
            print(f"ID: {categorie[0]['id']}")
            print(f"Nume: {categorie[0]['name']}")
            print(f"Numar de produse: {categorie[0]['itemsCount']}")
        else:
            print(f"Nu sa putut obtine informatii despre categorie")

    elif optiune == "3":
        nume_categorie = input("\nIntroduceti numele noii categorii: ")

        categorie_noua = {
            "title": nume_categorie,
        }

        response_categorie_noua = requests.post(url, json=categorie_noua)

        if response_categorie_noua.status_code == 200:
            categoria_noua = json.loads(response_categorie_noua.text)
            print(f"\nCategoria {categoria_noua['name']} a fost creata")
        else:
            print(f"Nu sa putut crea categoria {categorie_noua['name']}")

    elif optiune == "4":
        categorie_id = input("\nIntroduceti ID-ul categoriei pe care doriti sa o stergeti: ")

        response_stergere_categorie = requests.delete(url + categorie_id)

        if response_stergere_categorie.status_code == 200:
            print(f"\nCategoria cu ID-ul {categorie_id} a fost ștearsa")
        else:
            print(f"Nu sa putut sterge categoria cu ID-ul {categorie_id}.")

    elif optiune == "5":
        categorie_id = input("\nIntrodu ID-ul categoriei pe care doriti sa o modificati")
        nume_nou = input("\nIntroduceti noul nume pentru categoria selectata: ")

        categorie_modificata = {
            "title": nume_nou,
        }

        response_categorie_modificata = requests.put(urll + categorie_id, json=categorie_modificata)

        if response_categorie_modificata.status_code == 200:
            categoria_modificata = json.loads(response_categorie_modificata.text)
            print(f"\nCategoria cu ID-ul {categorie_id} a fost modificata cu succes!")
            print(f"Noul nume al categoriei este {categoria_modificata['name']}")
        else:
            print(f"Nu sa putut modifica categoria cu ID-ul {categorie_id}.")

    elif optiune == "6":
        categoria_id = input("\nIntroduceți ID-ul categoriei in care doriti sa adaugati un produs ")
        titlu_produs = input("\nIntroduceti titlul produsului: ")
        pret_produs = input("\nIntroduceti pretul produsului: ")

        produs_nou = {
            "title": titlu_produs,
            "price": int(pret_produs),
            "categoryId": int(categoria_id)
        }

        response_produs_nou = requests.post(f"{url}{categoria_id}/products", json=produs_nou)

        if response_produs_nou.status_code == 200:
            produs = json.loads(response_produs_nou.text)
            print(f"\nProdusul cu titlul {produs['title']} a fost adaugat cu succes")
        else:
            print(f"Nu sa putut adauga produsul in categoria cu ID-ul {categoria_id}.")

    elif optiune == "7":
        categorie_id = input("\nIntroduceți ID-ul categoriei pentru a afisa lista de produse: ")
        response_categorie_produse = requests.get(f"{url}{categorie_id}/products")

        if response_categorie_produse.status_code == 200:
            produse = json.loads(response_categorie_produse.text)

            print(f"Lista de produse din categoria cu ID-ul {categorie_id}:")
            for produs in produse:
                print(f"Nume: {produs['title']} - Price: {produs['price']} Lei")
        else:
            print(f"Nu sa putut obtine lista de produse pentru categoria cu ID-ul {categorie_id}")

    elif optiune == "8":
        print("Program incheiat.")
        break

    else:
        print("Optiune invalida. Incearca din nou")
