# Signal et Slot

Exemple 1 

## Les signaux (Signals) :

Les signaux  sont les notifications émises par les widgets lors d'évènements. Par exemple, un bouton émet le siganl `clicked` quand on clique dessus. 

*Remarque : Les signaux peuvent transporter des données.* 

## Les slots ( Slots) : 

Les slots sont des fontions qui sont appelées en réponse aux signaux. Cela peut être n'importe qu'elle fonction de python. 
Les slots reçoivent les données transmises par le signal en paramètre.  


## Connection entre un signal et un slot

La méthode `connect()` lie un signal à un slot.

`widget.signal.connect(slot)`

Dans exemple 1 :
`self.bouton_increment.clicked.connect(self.incrementer_compteur)`


## Découplage 

Il est possible de déconnecter les signaux avec `disconnec()`


## Créer un signal personnalisé.

Un signal personnalisé est défini avec la fonction `pyqtSignal(str)`
Dans l'example 2  : 

`nom_change = pyqtSignal(str)`  # Signal qui transportera une chaîne de caractères

`str` indique que le signal transportera une chaine de caractère.  Des signaux peuvent transporter différents types de données (int, str, list, dict, etc.)

### Mécanisme de transmission 

La vue principale émet le signal avec  `self.nom_change.emit(nouveau_nom)`
Les vues secondaires reçoivent la mise à jour via leur slot `mettre_a_jour`

Remarque : Un signal peut être connecté à plusieurs slot.

La communication est asynchrone et découplée.
- Le **découplage** signifie que les composants qui communiquent (l'émetteur du signal et le récepteur) n'ont pas besoin de se connaître mutuellement. 

```python
# L'émetteur émet son signal sans savoir qui va le recevoir
self.nom_change.emit(nouveau_nom)

# Un récepteur peut se connecter plus tard
emetteur.nom_change.connect(recepteur.mon_slot)
```

- L'émetteur ne sait pas combien de recepteurs écoutent son signal
- L'émetteur ne sait pas quels slots seront appelés.
- L'émetteur n'a pas beoin de connaitre l'implémentation des slots

L'**asynchrone** signifie que l'exécution du code n'est pas bloquée lors de l'émission du signal.
Par exemple, si un utilisateur clique sur un bouton qui déclenche un calcul long, l'interface reste réactive pendant que le calcul s'effectue en arrière-plan.


