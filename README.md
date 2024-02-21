# Security Review Bot - AI Powered Security Reviewer
The Security Review Bot is an AI powered security reviewer that can be used to help analysts perform security reviews. The Security Review Bot uses OpenAI to receive code input (in .txt format) from a developer, to perform additional analysis for the developer. This analysis can be used to augment the developer's review, to provide thorough results for reporting.

## Disclaimer
**2024-02-21: This project is currently in development and is a proof of concept. Additionally, you are responsible for any data that you provide to OpenAI via this project. Please ensure that you are not providing any sensitive data to OpenAI via this project. This includes any logs that are provided, API keys, and any data via the context prompt.**

**Please review OpenAI's pricing details here: https://openai.com/pricing**

## Prerequisites
The following are prerequisites for using the Log Analysis Buddy:
- An OpenAPI key (from creating an OpenAI account)
- Python 3.9 or higher
- Python packages contained in the requirements.txt file (installed via pip)
  - openai (and various dependent packages for this module)

## License
This project is licensed under the Apache 2.0 licensing terms. Please see the LICENSE file for more information.