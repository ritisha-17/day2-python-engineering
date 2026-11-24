
from tickets.loader import load_tickets

valid, invalid = load_tickets("tickets.csv")

print("\n----- TICKET VALIDATION REPORT -----")

print("Valid tickets:", len(valid))
print("Invalid tickets:", len(invalid))

print("\nValid Ticket Details:")

for ticket in valid:
    print(ticket)

print("\nInvalid Ticket Details:")

for ticket in invalid:
    print(ticket)
