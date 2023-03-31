
# NikeITPersonasToSalesforce

This component is a workflow designed to move data from Nike IT personas to Salesforce. It first takes the access token input for accessing the LinkedIn API and an object input of Salesforce credentials (username, password, security token, client_id, and client_secret). Then, it adds the persona data into Salesforce and outputs the result of the operation.

## Initial generation prompt
description: "IOs - input:\n- description: A valid OAuth2 access token for accessing\
  \ the LinkedIn API.\n  name: AccessToken\n  type: str\n- description: An object\
  \ containing Salesforce credentials (username, password, security\n    token, and\
  \ client_id, and client_secret).\n  name: SalesforceCredentials\n  type: object\n\
  output:\n- description: The result of adding persona data into Salesforce.\n  name:\
  \ SalesforceResult\n  type: object\n"
name: NikeITPersonasToSalesforce


## Transformer breakdown
- Execute the transform of the AbstractWorkflow
- Prepare the Output BaseModel

## Parameters
[]

        