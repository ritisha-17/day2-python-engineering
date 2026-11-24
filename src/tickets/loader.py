
import csv
import logging

from pydantic import ValidationError
from tickets.models import Ticket

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)


def load_tickets(file_path: str) -> tuple[list[Ticket], list[dict]]:
    valid_tickets = []
    invalid_tickets = []

    with open(file_path, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            try:
                # Validate CSV row using Pydantic
                ticket = Ticket(**row)

                valid_tickets.append(ticket)

                logger.info("Row %s: Valid ticket", row_number)

            except ValidationError as error:

                invalid_tickets.append({
                    "row": row_number,
                    "errors": error.errors()
                })

                logger.warning(
                    "Row %s: Invalid ticket", row_number
                )

    return valid_tickets, invalid_tickets
