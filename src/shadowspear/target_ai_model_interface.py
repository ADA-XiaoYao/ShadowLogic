import requests
import json

class TargetAIModelInterface:
    """ShadowSpear's Target AI Model Interface for standardized interaction with various AI models.

    This module provides abstracted interfaces for sending inputs, receiving outputs,
    and potentially querying model metadata, supporting different communication protocols.
    """

    def __init__(self):
        pass

    def interact_llm_api(self, api_endpoint, prompt, api_key=None, model_name="gpt-4", temperature=0.7):
        """Interacts with a generic LLM API endpoint.

        Args:
            api_endpoint (str): The URL of the LLM API endpoint.
            prompt (str): The prompt to send to the LLM.
            api_key (str, optional): API key for authentication. Defaults to None.
            model_name (str, optional): The name of the LLM model to use. Defaults to "gpt-4".
            temperature (float, optional): Controls randomness in generation. Defaults to 0.7.

        Returns:
            dict: The JSON response from the LLM API, or an error message.
        """
        headers = {
            "Content-Type": "application/json",
        }
        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        data = {
            "model": model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
        }

        try:
            response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"LLM API interaction failed: {e}"}
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON response from LLM API"}

    def interact_custom_api(self, api_endpoint, data, headers=None, method="POST"):
        """Interacts with a custom AI model API endpoint.

        Args:
            api_endpoint (str): The URL of the custom API endpoint.
            data (dict): The data payload to send.
            headers (dict, optional): Custom headers for the request. Defaults to None.
            method (str, optional): HTTP method (e.g., "POST", "GET"). Defaults to "POST".

        Returns:
            dict: The JSON response from the API, or an error message.
        """
        if headers is None:
            headers = {"Content-Type": "application/json"}

        try:
            if method.upper() == "POST":
                response = requests.post(api_endpoint, headers=headers, data=json.dumps(data))
            elif method.upper() == "GET":
                response = requests.get(api_endpoint, headers=headers, params=data)
            else:
                return {"error": f"Unsupported HTTP method: {method}"}

            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"Custom API interaction failed: {e}"}
        except json.JSONDecodeError:
            return {"error": "Failed to decode JSON response from custom API"}
