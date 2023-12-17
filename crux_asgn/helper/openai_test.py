import openai
import json
from .constants import OPEN_AI_KEY
openai.api_key = OPEN_AI_KEY

validation_agent = [
    {
        'name': 'validate_column_name',
        'description': 'validate wether the column name fits correctly for the given description',
        'parameters': {
            'type': 'object',
            'properties': {
                'verdict': {
                    'type': 'boolean',
                    'description': 'Verdict whether column name is valid for the decription or not'
                }
            }
        }
    }
]

xlsx_custom_functions = [
    {
        'name': 'get_semantic_column_name',
        'description': 'Get a semantic column name for a database column',
        'parameters': {
            'type': 'object',
            'properties': {
                'column_name': {
                    'type': 'string',
                    'description': 'Column name for database table , e.g: user_name, employee_house_id , is_verified , '
                }
            }
        }
    }
]

def get_semantic_column_name_by_description(description):
  prompt = "using column description provide a logical identifier or lable that identify the column for a database table please don't keep spaces in the label , Description:"+ str(description) 
  validation_prompt = "Ensure if the following identifier is a valid identifier/label for the column that describes: "+ str(description) + " ,column name :"
  for _ in range(5):
    response = openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": prompt}
      ],
      functions=xlsx_custom_functions,
      function_call='auto'
    )
    # Extract the generated column name from the response
    column_name = "None"
    try:
      if not response.choices[0].message.function_call is None:
        column_name = json.loads(response.choices[0].message.function_call.arguments)["column_name"]
    except:
      pass
    print(f"Column Name: {column_name}")

    response = openai.chat.completions.create(
      model="gpt-4-0613",
      messages=[
        {"role": "user", "content": validation_prompt+column_name}
      ],
      functions=validation_agent,
      function_call='auto'
    )
    # Extract the generated column name from the response
    verdict = "Not clear"
    try:
      if not response.choices[0].message.function_call is None:
        verdict = json.loads(response.choices[0].message.function_call.arguments)["verdict"]
    except:
      pass
    if(verdict==True):
      return column_name
    else:
      print(verdict)
    print(verdict)
  return None