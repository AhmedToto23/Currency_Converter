from app.services import convert_currency

def main():
    print("💱 Currency Converter CLI")

    try:
        amount = float(input("Amount: "))
        from_currency = input("From: ").upper()
        to_currency = input("To: ").upper()

        result = convert_currency(amount, from_currency, to_currency)
        print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")

    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
