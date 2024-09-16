# Python code to ask OpenAI questions about Security Best Practices

import openai
import logging
import inquirer
import json
import getpass


def prompt_questions():
    """Function for prompting questions to the user"""
    try:
        print("Please enter the OpenAI API Key you would like to use for this session.")
        openai.api_key = getpass.getpass('API Key:')
        print("Are you creating any resources that will be public to the internet?")
        answer_1 = input()
        print("What cloud (e.g. AWS, Azure, Google Cloud) services or resources will you be using?")
        answer_2 = input()
        print("What programming or languages are being used in this project?")
        answer_3 = input()
        print("Does your application or service require authentication?")
        answer_4 = input()
        print("Does your service handle or store customer data? If so, what types?")
        answer_5 = input()
        
        
        model_selection = [
            inquirer.List('model',
                        message="Please select the model you would like to use for this session.",
                        choices=['text-davinci-002', 'gpt-3.5-turbo', 'gpt-4', 'gpt-4o'],
                        ),
        ]
        # Data type conversion to JSON, then to string to get the model selection
        model_selection_answers = inquirer.prompt(model_selection)
        model_string_raw = json.dumps(model_selection_answers)
        model_json = json.loads(model_string_raw)
        model_string = (model_json["model"])
    except Exception as exception_handle:
        logging.error(exception_handle)
    return model_string, answer_1, answer_2, answer_3, answer_4, answer_5

def secure_ai_ask(model_string, answer_1, answer_2, answer_3, answer_4, answer_5):
    """Function to run Secure AI Ask"""
    additional_context = "Perform a detailed security review, but do not repeat the same information unnecessarily. Conclude the response with 'END'. Provide technical guidance, to include example code samples, and recommendations based on the following information: \n\n" + " Are you creating any resources that will be public to the internet? \n\n" + answer_1 + "\n\n" + "What AWS services or resources will you be using? \n\n" + answer_2 + "\n\n" + "What programming or languages are being used in this project? \n\n" + answer_3 + "\n\n" + "Does your application or service require authentication? \n\n" + answer_4 + "\n\n" + "Does your service handle or store customer data? If so, what types? \n\n" + answer_5 + "\n\n"
    try:
        # text-davinci-002 model code
        if model_string == 'text-davinci-002':
            response = openai.Completion.create(
                model="text-davinci-002",
                prompt=additional_context,
                temperature=0.4,
                max_tokens=2000,
                top_p=1,
                frequency_penalty=-0.5,
                presence_penalty=0.3,
                stop=None
            )
            print(response["choices"][0]["text"])
        # gpt-3.5-turbo model code
        elif model_string == 'gpt-3.5-turbo':
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                            {
                                "role": "user", 
                                "content": additional_context
                            }
                        ],
                temperature=0.4,
                top_p=1,
                frequency_penalty=-0.3,
                presence_penalty=0.3,
                stop=None
            )
            print(response["choices"][0]["message"]["content"])
        # gpt-4 model code
        elif model_string == 'gpt-4':
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                            {
                                "role": "user", 
                                "content": additional_context
                            }
                        ],
                temperature=0.4,
                top_p=1,
                frequency_penalty=-0.3,
                presence_penalty=0.3,
                stop=None
            )
            print(response["choices"][0]["message"]["content"])
        # gpt-4o model code
        elif model_string == 'gpt-4o':
            response = openai.ChatCompletion.create(
                model="gpt-4o",
                messages=[
                            {
                                "role": "user", 
                                "content": additional_context
                            }
                        ],
                temperature=0.4,
                top_p=1,
                frequency_penalty=-0.5,
                presence_penalty=0.3,
                stop=["END"]
            )
            print(response["choices"][0]["message"]["content"])
    except Exception as exception_handle:
        logging.error(exception_handle)


if __name__ == '__main__':
    """Main fuction for Secure AI Ask"""
    model_string, answer_1, answer_2, answer_3, answer_4, answer_5 = prompt_questions()
    secure_ai_ask(model_string, answer_1, answer_2, answer_3, answer_4, answer_5)