import streamlit as st
import requests

# Function to call your API
def call_api(user_input):
    api_url = "http://dev-judy-security-demo-alb-1215923742.eu-central-1.elb.amazonaws.com/vulnerabilities"  # Replace with your actual API endpoint
    headers = {
        "Content-Type": "application/json"
    }
    payload = {"description": user_input}
    
    try:
        response = requests.post(api_url, json=payload, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses

        # Check if the response is JSON
        if response.headers.get("Content-Type") == "application/json":
            return response.json()
        else:
            return {"error": "Unexpected response format from API. Expected JSON."}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Streamlit UI
st.title("API Query Tool")

# User input form
user_input = st.text_input("Enter your question:")

# Check if user input is provided
if user_input:
    # Call API and get response
    response = call_api(user_input)
    
    # Display response from API
    if "error" in response:
        st.error(f"Error: {response['error']}")
    else:
        st.write("Response from API:")
        st.json(response.get("result", "No 'message' key found in response"))
