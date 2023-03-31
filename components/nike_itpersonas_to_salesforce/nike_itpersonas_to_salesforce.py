
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class AccessToken(BaseModel):
    access_token: str

class SalesforceCredentials(BaseModel):
    username: str
    password: str
    security_token: str
    client_id: str
    client_secret: str


class NikeITPersonasToSalesforceIn(BaseModel):
    access_token: AccessToken
    salesforce_credentials: SalesforceCredentials


class SalesforceResult(BaseModel):
    result: dict


class NikeITPersonasToSalesforceOut(BaseModel):
    salesforce_result: SalesforceResult


class NikeITPersonasToSalesforce(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: NikeITPersonasToSalesforceIn, callbacks: typing.Any
    ) -> NikeITPersonasToSalesforceOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)
        
        salesforce_result = results_dict['SalesforceResult']
        out = NikeITPersonasToSalesforceOut(salesforce_result=salesforce_result)
        
        return out


load_dotenv()
nikeIT_personas_to_salesforce_app = FastAPI()


@nikeIT_personas_to_salesforce_app.post("/transform/")
async def transform(args: NikeITPersonasToSalesforceIn) -> NikeITPersonasToSalesforceOut:
    nike_it_personas_to_salesforce = NikeITPersonasToSalesforce()
    
    return await nike_it_personas_to_salesforce.transform(args, callbacks=None)
