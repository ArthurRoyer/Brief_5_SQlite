import sqlite3
import csv
import os


# Connexion à une base de données SQLite
conn = sqlite3.connect('clients.db')


# Création d'un curseur pour exécuter des commandes SQL
cursor = conn.cursor()


# Supprimer les tables Clients et Commandes si elles existent déjà
cursor.execute("DROP TABLE IF EXISTS Commandes;")
cursor.execute("DROP TABLE IF EXISTS Clients;")


# Création de la table Clients
cursor.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    date_inscription DATE NOT NULL
)
''')

# Inserer des données dans la table Clients
cursor.execute('''
INSERT INTO Clients (nom, prenom, email, date_inscription) VALUES
('LEMARRANT', 'Bob', 'bob.lemarrant@gmail.com', '2024-01-15'),
('GOKU', 'Son', 'ssj.goku@gmail.com', '2024-02-10')
''')


# Création de la table Commandes
cursor.execute('''
CREATE TABLE IF NOT EXISTS Commandes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    produit TEXT NOT NULL,
    date_commande DATE NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients(id)
)
''')

# Inserer des données dans la table Commandes
cursor.execute('''
INSERT INTO Commandes (client_id, produit, date_commande) VALUES
(1, 'Martini 5L', '2024-03-01'),
(2, 'Nyoi-bo V4000XL', '2024-03-05')
''')


# Sélectionner tous les clients
cursor.execute("SELECT * FROM Clients")
clients = cursor.fetchall()

# Afficher les clients
print("Liste des clients :")
for client in clients:
    print(client)


# Récupérer les commandes d'un client spécifique
cursor.execute("SELECT * FROM Commandes WHERE client_id = 1")
commandes = cursor.fetchall()

# Afficher les commandes
print(f"Commandes du client avec id 1 :")
for commande in commandes:
    print(commande)


# Mettre à jour l'adresse e-mail d’un client
cursor.execute("UPDATE Clients SET email = 'bob.pas-ci-marrant@gmail.com' WHERE id = 1")

print(f"L'adresse e-mail du client avec id 1 a été mise à jour.")


cursor.execute("DELETE FROM Commandes WHERE id = 1")

print(f"La commande id 1 a été supprimée.")


# Valider les modifications (enregistrer dans la base de données)
conn.commit()


# Récupération des données de la table Clients
cursor.execute('SELECT * FROM Clients')
clients = cursor.fetchall()

# Écriture des données dans le fichier CSV
with open('Clients.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Écriture des lignes de données
    writer.writerows(clients)


# Récupération des données de la table Clients
cursor.execute('SELECT * FROM Commandes')
commandes = cursor.fetchall()

# Écriture des données dans le fichier CSV
with open('Commandes.csv', mode='w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Écriture des lignes de données
    writer.writerows(commandes)


print('Données exportées avec succès dans Clients.csv et Commandes.csv')


# Fermeture de la connexion
conn.close()



