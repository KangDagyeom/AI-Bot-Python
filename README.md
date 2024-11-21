# AI-Bot-Python 🧠

<a href="https://github.com/KangDagyeom/AI-Bot-Python/stargazers"><img src="https://img.shields.io/github/stars/KangDagyeom/AI-Bot-Python" alt="Stars Badge"/></a>
<a href="https://github.com/KangDagyeom/AI-Bot-Python/network/members"><img src="https://img.shields.io/github/forks/KangDagyeom/AI-Bot-Python" alt="Forks Badge"/></a>
<a href="https://github.com/KangDagyeom/AI-Bot-Python/pulls"><img src="https://img.shields.io/github/issues-pr/KangDagyeom/AI-Bot-Python" alt="Pull Requests Badge"/></a>
<a href="https://github.com/KangDagyeom/AI-Bot-Python/issues"><img src="https://img.shields.io/github/issues/KangDagyeom/AI-Bot-Python" alt="Issues Badge"/></a>
<a href="https://github.com/KangDagyeom/AI-Bot-Python/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/KangDagyeom/AI-Bot-Python?color=2b9348"></a>
<a href="https://github.com/KangDagyeom/AI-Bot-Python/blob/master/LICENSE"><img src="https://img.shields.io/github/license/KangDagyeom/AI-Bot-Python?color=2b9348" alt="License Badge"/></a>

![Static Badge](https://img.shields.io/badge/Python-Python%203.7%20or%20later%20-%233776AB?style=for-the-badge&logo=python)
![Static Badge](https://img.shields.io/badge/PythonLib-OpenAI%20lib%20-%23ffffff?style=for-the-badge&logo=openai)
![Static Badge](https://img.shields.io/badge/Ollama-llama3.2%20-%23ebf700?style=for-the-badge&logo=ollama)

This project demonstrates a Python-based chatbot script that interacts with OpenAI's API to enable dynamic, real-time conversations.

## Features ✨
-Interactive Chat: Engage in real-time conversations with an AI chatbot.
-Streaming Responses: Dynamic and seamless response updates.
-Custom Endpoint: Works with your local OpenAI API instance.
## Getting Started 🌟
**Prerequisites**

Ensure you have the following installed:
```
Python 3.7 or later  
OpenAI Python SDK
Ollama gemma 9b If you want high quality
```
## Installation
Clone the repository:
```
git clone https://github.com/KangDagyeom/AI-Bot-Python.git
```
## Navigate to the project directory:
```
cd AI-Bot-Python
```
## Install dependencies:
```
pip install -r requirements.txt
```
## Usage 🚀
Modify the script to configure your API:
```
from openai import OpenAI

client = OpenAI(  
    base_url="http://localhost:11434/v1",  
    api_key="ollama" 
)
```
## Run the script:
```
python ai_bot.py
```
**Start chatting! To exit, type:**
```
exit
```
**Example Interaction 📖**
```
You: Hello!  
Bot: Hi! How can I assist you today?  

You: Tell me about Python.  
Bot: Python is a popular programming language known for its simplicity and versatility.  

You: exit  
Goodbye!
```

## Directory Structure 🔰
```
AI-Bot-Python/  
│  
├── ai_bot.py       # Main script for interaction  
├── requirements.txt     # Dependencies  
└── README.md            # Documentation
```
## Known Issues 🚩
Ensure the API key and endpoint are configured correctly.
Limited handling of invalid inputs.

## Contributing 🙌
Fork the repository.
Create a feature branch:
```
git checkout -b feature/YourFeature
```
Commit your changes:
```
git commit -m "Add YourFeature"
```
Push to the branch:
```
git push origin feature/YourFeature
```
Open a pull request.
## License 🛑
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments 💫
OpenAI Team: For providing robust APIs and tools.

Community Contributors: For valuable feedback and contributions.





