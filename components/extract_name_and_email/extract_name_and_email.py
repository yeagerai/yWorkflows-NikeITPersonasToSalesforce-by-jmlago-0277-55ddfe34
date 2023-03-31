
from typing import List, Tuple
from fastapi import FastAPI
from pydantic import BaseModel
from core.abstract_component import AbstractComponent

class PersonasData(BaseModel):
    personas: List[dict]

class NamesAndEmails(BaseModel):
    names_and_emails: List[Tuple[str, str]]

class ExtractNameAndEmail(AbstractComponent):
    def __init__(self):
        super().__init__()

    def transform(self, args: PersonasData) -> NamesAndEmails:
        names_and_emails = []

        for persona in args.personas:
            name = persona["name"]
            email = persona["email"]
            names_and_emails.append((name, email))

        # Send the extracted names and email addresses to Salesforce
        # (You need to implement the logic for interacting with Salesforce API here)

        return NamesAndEmails(names_and_emails=names_and_emails)

extract_name_and_email_app = FastAPI()

@extract_name_and_email_app.post("/transform/")
async def transform(args: PersonasData) -> NamesAndEmails:
    extract_name_and_email = ExtractNameAndEmail()
    return extract_name_and_email.transform(args)
