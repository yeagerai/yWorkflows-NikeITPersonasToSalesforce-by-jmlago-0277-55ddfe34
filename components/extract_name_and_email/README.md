
# ExtractNameAndEmail

This component processes the personas data from FetchNikeITPersonas, extracting their names and email addresses, and sends the extracted information to Salesforce.

## Initial generation prompt
description: This component processes the personas data from FetchNikeITPersonas and
  extracts their names and email addresses before sending them to Salesforce.
input_from_other_nodes:
- name: PersonasData
  type: list
name: ExtractNameAndEmail


## Transformer breakdown
- 1. Iterate through the PersonasData input list
- 2. For each persona, extract the name and email address
- 3. Create a new tuple with the name and email address
- 4. Append the tuple to the NamesAndEmails list
- 5. Return the NamesAndEmails list

## Parameters
[]

        