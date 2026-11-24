
import csv

from tickets.loader import load_tickets


def create_csv(tmp_path, headers, rows):
    file_path = tmp_path / "tickets.csv"

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)

    return str(file_path)


headers = [
    "ticket_id",
    "customer_name",
    "service_type",
    "priority",
    "created_date"
]


# Test 1: Valid ticket
def test_valid_row(tmp_path):
    path = create_csv(tmp_path, headers, [
        ["T101", "Rahul", "repair", "high", "2026-11-24"]
    ])

    valid, invalid = load_tickets(path)

    assert len(valid) == 1
    assert len(invalid) == 0


# Test 2: Missing field
def test_missing_field(tmp_path):
    path = create_csv(
        tmp_path,
        ["ticket_id", "service_type", "priority", "created_date"],
        [["T102", "repair", "high", "2026-11-24"]]
    )

    valid, invalid = load_tickets(path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 3: Invalid date
def test_bad_date(tmp_path):
    path = create_csv(tmp_path, headers, [
        ["T103", "Anu", "repair", "high", "wrong-date"]
    ])

    valid, invalid = load_tickets(path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 4: Invalid service type
def test_bad_enum(tmp_path):
    path = create_csv(tmp_path, headers, [
        ["T104", "Priya", "cleaning", "high", "2026-11-24"]
    ])

    valid, invalid = load_tickets(path)

    assert len(valid) == 0
    assert len(invalid) == 1


# Test 5: Empty CSV
def test_empty_file(tmp_path):
    file_path = tmp_path / "empty.csv"
    file_path.write_text("")

    valid, invalid = load_tickets(str(file_path))

    assert len(valid) == 0
    assert len(invalid) == 0
