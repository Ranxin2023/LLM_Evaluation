from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from groq import Groq
import math
from openai import OpenAI
import os
from nltk.translate.bleu_score import sentence_bleu
# from pathlib import Path
import sqlite3
import time

load_dotenv()
# env_path=Path(__file__).resolve().parent / ".env"
# load_dotenv(dotenv_path=env_path)
db_path=os.getenv("DATABASE_PATH")
if not db_path:
    raise ValueError("No database found")


# Initialize app
app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
# Create the database tables
# Initialize SQLAlchemy

groq_api_key=os.getenv("GROQ_API_KEY")
openai_api_key=os.getenv("OPENAI_API_KEY")
groq_client = Groq(
    api_key=groq_api_key,
)
openai_client = OpenAI(
    
    api_key=openai_api_key
)
llms=["gpt-4",  "gpt-4o-mini", "llama3-8b-8192","gemma2-9b-it"]
simple_prompt="What is the capital of French"

def insert_into_db(model_name, response, perplexity, precision, recall, f1_score, response_time, commit_time):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cmd = '''
        INSERT INTO models (model_name, response, perplexity, precision, recall, f1_score, response_time, commit_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        '''
        cursor.execute(cmd, [model_name, response, perplexity, precision, recall, f1_score, response_time, commit_time])
        conn.commit()
        conn.close()
        print("Inserting successfully into the models table.")
    except sqlite3.Error as e:
        print(f"Error inserting into database: {e}")
# Helper function: Calculate Perplexity
def calculate_perplexity(response, tokens_probabilities):
    # Simulated example: log probabilities for each token
    log_prob_sum = sum(math.log(p) for p in tokens_probabilities)
    perplexity = math.exp(-log_prob_sum / len(tokens_probabilities))
    return perplexity

# Helper function: Calculate BLEU Score
def calculate_bleu(reference, response):
    reference = [reference.split()]  # BLEU expects a list of tokenized references
    response = response.split()  # Tokenize the response
    return sentence_bleu(reference, response)

# Helper function: Calculate F1 Score
def calculate_f1(reference, response):
    # Convert to binary relevance (1 for overlap, 0 otherwise) for simplicity
    reference_set = set(reference.split())
    response_set = set(response.split())
    true_positives = len(reference_set & response_set)
    precision = true_positives / len(response_set) if response_set else 0
    recall = true_positives / len(reference_set) if reference_set else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
    return [round(precision, 3), round(recall, 3), round(f1, 3)]
def query_openai(prompt=simple_prompt, model="gpt-4"):
    try:
        # openai.api_key = openai_api_key
        response = openai_client.chat.completions.create(
        # model name used here is text-davinci-003
        # there are many other models available under the 
        # umbrella of GPT-3
            model=model,
            store=True,
            messages=[
                # {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error with OpenAI: {e}"
    
def query_groq(prompt=simple_prompt, model="llama-3.1-70b-versatile"):
    try:
        response = groq_client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
@app.route('/api/submit_prompt', methods=['POST'])
def submit_prompt():
    results=[]
    data = request.json
    prompt = data['prompt']
    reference=data['reference']
    for i in range(len(llms)):
        lower_llm=llms[i].lower()
        start_time=time.time()
        if i<2:
            response=query_openai(prompt=prompt, model=lower_llm)
        else:
            response=query_groq(prompt=prompt, model=lower_llm)
        end_time=time.time()
        response_time=end_time-start_time
        tokens_probabilities = [0.9, 0.8, 0.7, 0.95, 0.85]
        perplexity = calculate_perplexity(response, tokens_probabilities)
        [precision, recall, f1] = calculate_f1(reference, response)
        # bleu = calculate_bleu(reference, response)
        local_time = datetime.now()  
        formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")
        insert_into_db(lower_llm, response, perplexity, precision, recall, f1, response_time, formatted_time)
        results.append({
                "llm_name": lower_llm,
                "response": response,
                "perplexity": round(perplexity, 2),
                "precision": precision, 
                "recall":recall, 
                # "bleu_score": round(bleu, 2),
                "f1_score": f1,
                "response_time": round(response_time, 3),
        })
    # print(f"result is {results}")
    return jsonify({"results":results})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)