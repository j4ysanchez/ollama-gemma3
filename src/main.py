import requests
import base64


# Define the URL for the locally deployed Ollama model
url = "http://localhost:11434/api/generate"

images = []
# Set up the payload with the model name and prompt
payload = {
    "model": "gemma3:4b",
    "prompt": "Analyze the attached receipt and provide details.",
    "stream": False
}

# Path to the file to be analyzed
file_path = "data/ipad_pro_receipt.png"

# Open the file in binary mode and send the POST request
# with open(file_path, "rb") as file:
#     files = {"file": file}

# open file and encode with base64
with open(file_path, "rb") as file:
    file_data = file.read()
    encoded_file = base64.b64encode(file_data).decode('utf-8')
    images.append(encoded_file)

payload['images'] = images  
response = requests.post(url, json=payload)

# Check the response
if response.status_code == 200:
    try:
        # Attempt to parse the response as JSON
        json_response = response.json()
        print("Response from gemma3:4b:")
        print(json_response)
        print("Response content:", json_response['response'])
    except requests.exceptions.JSONDecodeError:
        print("Error: Received invalid JSON response")
        print("Raw response content:")
        print(response.text)
else:
    print(f"Error: {response.status_code}")
    print(response.text)