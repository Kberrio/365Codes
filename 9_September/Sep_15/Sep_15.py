class RentTracker:
    def __init__(self, monthly_rent):
        self.monthly_rent = monthly_rent
        self.balance = 0
        self.payments = []

    def add_month(self):
        self.balance += self.monthly_rent

    def make_payment(self, amount):
        if amount <= 0:
            return "Le paiement doit être supérieur à 0."
        if amount > self.balance:
            return "Le paiement ne peut pas être supérieur au solde dû."
        self.balance -= amount
        self.payments.append(amount)
        return f"Paiement de {amount}€ effectué. Nouveau solde: {self.balance}€"

    def get_balance(self):
        return f"Solde actuel: {self.balance}€"

    def get_payment_history(self):
        return self.payments

def main():
    loyer_mensuel = float(input("Entrez le montant du loyer mensuel: "))
    tracker = RentTracker(loyer_mensuel)

    while True:
        print("\n1. Ajouter un mois de loyer")
        print("2. Effectuer un paiement")
        print("3. Vérifier le solde")
        print("4. Voir l'historique des paiements")
        print("5. Quitter")

        choix = input("Choisissez une option (1-5): ")

        if choix == "1":
            tracker.add_month()
            print(f"Un mois de loyer ajouté. {tracker.get_balance()}")
        elif choix == "2":
            montant = float(input("Entrez le montant du paiement: "))
            print(tracker.make_payment(montant))
        elif choix == "3":
            print(tracker.get_balance())
        elif choix == "4":
            historique = tracker.get_payment_history()
            if historique:
                print("Historique des paiements:")
                for i, paiement in enumerate(historique, 1):
                    print(f"  {i}. {paiement}€")
            else:
                print("Aucun paiement effectué pour le moment.")
        elif choix == "5":
            print("Merci d'avoir utilisé le programme de suivi des loyers. Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir entre 1 et 5.")

if __name__ == "__main__":
    main()