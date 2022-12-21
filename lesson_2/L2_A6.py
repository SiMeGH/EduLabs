# A6-Match case
country = input("Enter a country: ")
currency = None

if country in ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia', 'Denmark',
               'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland',
               'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands',
               'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']:
    currency = "Euro"
else:
    match country:
        case "USA":
            currency = "US dollar"
        case "Israel":
            currency = "New Israel Shekel (NIS)"
        case "UK":
            currency = "Pound"
        case _:
            currency = "I don't know"

print(f"This country's currency is {currency}")
