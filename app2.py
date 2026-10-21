from flask import Flask, render_template, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    selected_models = request.json.get('models', [])  # Get array of selected models
    ollama_url = 'http://localhost:11434/api/generate'
    
    responses = {}
    
    try:
        for model in selected_models:
            response = requests.post(
                ollama_url,
                json={'model': model, 'prompt': user_message},
                headers={'Content-Type': 'application/json'},
                stream=True
            )
            
            full_response = ""
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    json_data = json.loads(decoded_line)
                    full_response += json_data.get('response', '')
            
            responses[model] = full_response
        
        return jsonify({'responses': responses})
    except Exception as e:
        return jsonify({'error': f"Error occurred: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)