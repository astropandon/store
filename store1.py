import csv
from tkinter import *

com = Tk()
com.title("Store")
com.geometry("500x400")


# ajouter
def ajouter_product():
    pr = Tk()
    pr.title("Ajouter un produit")
    pr.geometry("500x300")

    label_nom = Label(pr, text="Nom de produit:", font="HoboStd 10 bold", fg="#de7457")
    label_nom.pack(pady=3)
    nom_produit = Entry(pr)
    nom_produit.pack(ipadx=3, ipady=3)

    label_prix = Label(pr, text="Prix de produit:", font="HoboStd 10 bold", fg="#de7457")
    label_prix.pack(pady=1)
    prix_produit = Entry(pr)
    prix_produit.pack(pady=3)

    label_quantite = Label(pr, text="Quantité de produit:", font="HoboStd 10 bold", fg="#de7457")
    label_quantite.pack(pady=3)
    quantite_produit = Entry(pr)
    quantite_produit.pack(ipadx=3, ipady=3)

    def ajoute():
        produit = nom_produit.get()
        prix = prix_produit.get()
        quantite = quantite_produit.get()
        if produit and prix and quantite: 
            try:
                with open('products.csv', mode='a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([produit, prix, quantite])
                print(f"Produit ajouté : {produit} avec un prix de {prix} et une quantité de {quantite}")
                pr.destroy()  # cls
            except Exception as e:
                print("Erreur lors de l'écriture du fichier:", e)
        else:
            print("Veuillez remplir tous les champs.")
    
    ajouter = Button(pr, text="Ajouter", fg="gray", bg="#f0a962", font="HoboStd 13 bold", width=20, command=ajoute)
    ajouter.pack(pady=10)
    pr.mainloop()


com1 = Button(com, text="Ajouter un produit!", fg="green", bg="#f0a962", font="HoboStd 13 bold", width=20, pady=3, padx=3, command=ajouter_product)
com1.pack()


# afficher
def afficher_produits():
    aff = Tk()
    aff.title("Afficher les produits")
    aff.geometry("500x300")
    try:
        with open("products.csv", "r", encoding="utf-8") as file:
            cnt = csv.reader(file, delimiter=',')  
            for row in cnt:
                if row:  
                    les_produits = Label(aff, text=f"Produit: {row[0]}? Prix: {row[1]}, Quantité: {row[2]}", font="HoboStd 10 bold", fg="#de7457")
                    les_produits.pack()  
    except Exception as e:
        print("Erreur lors de l'ouverture du fichier:", e)


com2 = Button(com, text="Afficher les produits!", fg="green", bg="#f0a962", font="HoboStd 13 bold", width=20, pady=3, padx=3, command=afficher_produits)
com2.pack(pady=5)


# acheter
def acheter():
    ach = Tk()
    ach.title("Acheter un produit")
    ach.geometry("500x300")

    label_nom = Label(ach, text="Nom de produit à acheter:", font="HoboStd 10 bold", fg="#de7457")
    label_nom.pack(pady=3)
    nom_produit = Entry(ach)
    nom_produit.pack(ipadx=3, ipady=3)

    label_quantite = Label(ach, text="Quantité de produit à acheter:", font="HoboStd 10 bold", fg="#de7457")
    label_quantite.pack(pady=3)
    quantite_produit = Entry(ach)
    quantite_produit.pack(ipadx=3, ipady=3)

    def update_stock():
        nom = nom_produit.get()
        quantite = int(quantite_produit.get())
        total = 0
        found = False  

        try:
            with open("products.csv", "r", encoding="utf-8") as file:
                products = list(csv.reader(file))
            
            for row in products:
                if row[0] == nom:
                    stock = int(row[2])
                    if stock >= quantite:
                        row[2] = str(stock - quantite)  
                        total += int(row[1]) * quantite  
                        found = True
                    else:
                        Label(ach, text="Stock insuffisant!", font="HoboStd 10 bold", fg="#de7457").pack(pady=3)
                    break

            if found:
          
                with open("products.csv", "w", newline='', encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerows(products)
                Label(ach, text=f"Achat réussi! Total: {total} dh", font="HoboStd 10 bold", fg="#de7457").pack(pady=3)
            else:
                Label(ach, text="Produit non trouvé!", font="HoboStd 10 bold", fg="#de7457").pack(pady=3)

        except Exception as e:
            print("Erreur lors de l'ouverture du fichier:", e)

    acheter_button = Button(ach, text="Acheter", fg="gray", bg="#f0a962", font="HoboStd 13 bold", width=20, command=update_stock)
    acheter_button.pack(pady=10)

    ach.mainloop()


com3 = Button(com, text="Acheter un produit!", fg="green", bg="#f0a962", font="HoboStd 13 bold", width=20, pady=3, padx=3, command=acheter)
com3.pack(pady=5)

com3 = Button(com, text="Qutter!", fg="green", bg="#f0a962", font="HoboStd 13 bold", width=20, pady=3, padx=3, command=exit)
com3.pack(pady=5)

com.mainloop()
