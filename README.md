# AMC Service Ticket Validation System

## Overview
A Python project that reads AMC service tickets from a CSV file and validates them using Pydantic.

## Technologies
- Python
- Pydantic
- Pytest
- CSV
- Logging

## Features
- CSV ticket loading
- Data validation using Pydantic
- Valid and invalid ticket separation
- Error logging
- Automated testing

## How to Run
```bash
python -m pip install -e .
python run.py
```

## Test
```bash
python -m pytest -v
```

## Results
- Total tickets: 5
- Valid tickets: 4
- Invalid tickets: 1
- Test cases passed: 5
git add README.md

Project completed as part of Day 2 Python Engineering Bootcamp.