
import pytest
from pydantic import BaseModel
from typing import List, Tuple
from your_source_file import ExtractNameAndEmail, PersonasData, NamesAndEmails

'''
Replace 'your_source_file' with the name of your actual source file that contains
the ExtractNameAndEmail component.
'''

# Define test cases with mocked input and expected output data
test_cases = [
    (PersonasData(personas=[
        {"name": "John Doe", "email": "john.doe@example.com"},
        {"name": "Jane Doe", "email": "jane.doe@example.com"}
    ]),
    NamesAndEmails(names_and_emails=[
        ("John Doe", "john.doe@example.com"),
        ("Jane Doe", "jane.doe@example.com")
    ])),
    (PersonasData(personas=[]),
    NamesAndEmails(names_and_emails=[])),
    (PersonasData(personas=[
        {"name": "Bob Smith", "email": "bob.smith@example.com"},
        {"name": "Alice Johnson", "email": "alice.johnson@example.com"},
        {"name": "Charlie Brown", "email": "charlie.brown@example.com"}
    ]),
    NamesAndEmails(names_and_emails=[
        ("Bob Smith", "bob.smith@example.com"),
        ("Alice Johnson", "alice.johnson@example.com"),
        ("Charlie Brown", "charlie.brown@example.com")
    ]))
]

@pytest.mark.parametrize("input_data, expected_output", test_cases)
def test_transform(input_data: PersonasData, expected_output: NamesAndEmails):
    component = ExtractNameAndEmail()
    result = component.transform(input_data)
    assert result == expected_output

# Additional error handling and edge case scenarios can be added as needed.
