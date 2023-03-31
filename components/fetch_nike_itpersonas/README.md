
# FetchNikeITPersonas

Using the LinkedIn API, this component fetches information about personas from Nike's IT department. The AccessToken input is passed as an authorization header to make the request.

## Initial generation prompt
description: Using the LinkedIn API, this component fetches information about personas
  from Nike's IT department. The AccessToken input is passed as an authorization header
  to make the request.
input_from_other_nodes:
- name: AccessToken
  type: str
name: FetchNikeITPersonas


## Transformer breakdown
- Create the request headers, including the authorization header with the AccessToken
- Send the API request to the LinkedIn endpoint to fetch personas from Nike's IT department
- Collect and parse the response containing personas data
- Return the parsed personas data as a list of dictionaries

## Parameters
[]

        