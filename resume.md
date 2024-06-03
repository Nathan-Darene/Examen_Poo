# Détails sur le programmme de jeu de bataille navale
## Le constructeur __init__
__init__:La méthode __init__ en Python est un constructeur spécial utilisé pour initialiser les nouveaux
objets créés à partir d'une classe. 
        Elle est automatiquement appelée chaque fois qu'une nouvelle instance de la classe est créée.
        Son but est d'initialiser les attributs de l'objet avec les valeurs fournies ou par défaut.
        
__self__: Le paramètre self en Python permet à une méthode de faire référence à l'instance courante de la classe, 
     lui permettant ainsi d'accéder à ses attributs et méthodes.


self en Python permet à une méthode d'accéder aux attributs et méthodes de l'instance de la classe à laquelle elle est associée.
C'est pourquoi on utilise self pour définir les attributs de l'objet et
pour accéder à ces attributs dans les méthodes de la classe.


Imaginons que nous voulions créer une classe Personne qui représente une personne avec un nom et un âge, 
et nous voulons également avoir une méthode pour afficher les détails de cette personne.

Voici comment cela pourrait être implémenté :

class Personne :
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def afficher_details(self):
        print(f"Nom: {self.nom}, Âge: {self.age}")


#Maintenant, examinons en détail ce qui se passe ici :

Dans la méthode __init__, self est utilisé pour faire référence à l'instance actuelle de la classe Personne. 
Lorsque vous créez une nouvelle instance de Personne, 
par exemple:
personne1 = Personne("Alice", 30)

self représente personne1 dans cette méthode. Ainsi, 
self.nom et self.age se réfèrent respectivement aux attributs nom et age 
de cette instance spécifique.

#Dans la méthode afficher_details, self est à nouveau utilisé pour faire référence à l'instance actuelle de la classe Personne. 
Lorsque vous appelez personne1.afficher_details(), self représente personne1. Cela permet d'accéder à ses attributs nom et age 
pour afficher les détails de cette personne spécifique.

Voici comment nous pouvons utiliser cette classe :
Création d'une instance de la classe Personne
personne1 = Personne("Alice", 30)

Appel de la méthode afficher_details pour afficher les détails de la personne
personne1.afficher_details()  Output: Nom: Alice, Âge: 30

Dans cet exemple, self joue un rôle crucial pour permettre à nos méthodes d'interagir avec les attributs de 
l'instance actuelle de la classe Personne.
    
instance: Une instance en programmation orientée objet (POO) est un objet spécifique créé à partir d'une classe. 
            Lorsque vous instanciez une classe, vous créez un nouvel objet qui possède ses propres attributs et méthodes, 
            distincts des autres instances de la même classe.
            Une instance en POO n'est tout simplement que le création d'un ou plusieur objets
exemple:
class Voiture: 
    def __init__(self, marque, couleur):
        self.marque = marque
        self.couleur = couleur

voiture1 = Voiture("Toyota", "Rouge")
voiture2 = Voiture("Ford", "Bleu")

voiture1 et voiture2 sont des instances de la classe Voiture.


Un Objet : Un objet est une instance spécifique d'une classe. 
           Une classe est un modèle ou un plan utilisé pour créer des objets. 
           Les objets sont des entités qui regroupent des données (sous forme d'attributs) 
           et des comportements (sous forme de méthodes) qui agissent sur ces données.

exemple:
 
class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}")

Nous pouvons créer des objets à partir de cette classe :

voiture1 = Voiture("Toyota", "Corolla")
voiture2 = Voiture("Honda", "Civic")


voiture1.afficher_details()
Dans cet exemple, voiture1 et voiture2 sont des objets de la classe Voiture. 
Chaque objet a ses propres attributs (marque et modele) qui sont définis lors 
de la création de l'objet à l'aide de la méthode __init__. De plus, chaque objet 
peut appeler les méthodes de la classe, comme afficher_details(), qui agissent 
sur les données spécifiques de l'objet.

En résumé, un objet est une instance spécifique d'une classe qui possède ses propres données 
et peut exécuter les méthodes définies dans la classe. Les objets permettent de représenter 
des entités du monde réel ou des concepts abstraits de manière modulaire et réutilisable dans le code.