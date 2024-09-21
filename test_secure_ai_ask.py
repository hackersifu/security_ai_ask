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
        
        print("What programming languages are being used in this project?")
        answer_3 = input()
        
        print("Does your application or service require authentication?")
        answer_4 = input()
        
        print("Does your service handle or store customer data? If so, what types?")
        answer_5 = input()
        
        model_selection = [
            inquirer.List('model',
                          message="Please select the model you would like to use for this session.",
                          choices=['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo'],
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

def ask_openai(model_string, prompt):
    """The reusable function to query OpenAI for each subtask"""
    try:
        if model_string in ['gpt-3.5-turbo', 'gpt-4', 'gpt-4-turbo']:
            response = openai.ChatCompletion.create(
                model=model_string,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4,
                top_p=1,
                frequency_penalty=0.3,
                presence_penalty=0.3,
                max_tokens=1500,
                stop=None
            )
            return response["choices"][0]["message"]["content"]
    except Exception as exception_handle:
        logging.error(exception_handle)
        return None

def secure_ai_ask(model_string, answer_1, answer_2, answer_3, answer_4, answer_5):
    """Function to break down security questions into subtasks"""
    
    subtasks = [
        {"question": "Review the security risks of exposing resources to the internet.", "answer": answer_1},
        {"question": "Provide best practices for securing cloud resources, based on the cloud provider(s) used.", "answer": answer_2},
        {"question": "Provide programming language-specific security guidance, and include code examples.", "answer": answer_3},
        {"question": "Review authentication requirements for securing the application.", "answer": answer_4},
        {"question": "Provide best practices for handling customer data securely based on the these types of data.", "answer": answer_5},
    ]

    # Iterate over each subtask and send a separate query to OpenAI
    for task in subtasks:
        prompt = f"{task['question']}\n\nDetails:\n{task['answer']}\n"
        print(f"Asking OpenAI: {task['question']}")
        response = ask_openai(model_string, prompt)
        print(f"Response:\n{response}\n")


if __name__ == '__main__':
    """Main function for Secure AI Ask"""
    model_string, answer_1, answer_2, answer_3, answer_4, answer_5 = prompt_questions()
    secure_ai_ask(model_string, answer_1, answer_2, answer_3, answer_4, answer_5)
