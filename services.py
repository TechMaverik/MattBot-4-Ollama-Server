import requests


class Services:

    def chatbot_services(self, user_msg):
        payload = {"model": "llama2", "prompt": user_msg, "stream": False}

        feedback = requests.post("http://localhost:11434/api/generate", json=payload)
        return feedback.json()


# payload = {"model": "llama2", "prompt": "my chest is paining", "stream": False}

# ans = Services().chatbot_services(payload)
# print(ans)
