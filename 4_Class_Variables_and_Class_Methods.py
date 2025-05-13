class Bank:
    bank_name = "Meezan"

    @classmethod
    def change_bank_name(cls,name):
        cls.bank_name = name

if __name__ == "__main__":
    bank1 = Bank()
    print(f"\nBefore change the Bankname: {bank1.bank_name}.")
    bank1.change_bank_name("JS BANK")
    print(f"After change the Bankname: {bank1.bank_name}.\n")
