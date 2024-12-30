from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import time

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///llm_metrics.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define database models
class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(500), nullable=False)
    llm_name = db.Column(db.String(50), nullable=False)
    response = db.Column(db.Text, nullable=False)
    accuracy = db.Column(db.Float, nullable=True)
    relevancy = db.Column(db.Float, nullable=True)
    response_time = db.Column(db.Float, nullable=False)

# Route to submit prompts and fetch responses from multiple LLMs
@app.route('/api/submit_prompt', methods=['POST'])
def submit_prompt():
    data = request.json
    prompt = data['prompt']

    # Simulated LLM responses and metrics
    llms = ["LLM-1", "LLM-2", "LLM-3"]
    results = []

    for llm in llms:
        start_time = time.time()
        response = f"Simulated response from {llm} for: {prompt}"
        end_time = time.time()

        response_time = end_time - start_time
        accuracy = round(0.8, 2)  # Mock accuracy
        relevancy = round(0.9, 2)  # Mock relevancy

        # Save to database
        evaluation = Evaluation(
            prompt=prompt,
            llm_name=llm,
            response=response,
            accuracy=accuracy,
            relevancy=relevancy,
            response_time=response_time
        )
        db.session.add(evaluation)
        results.append({
            "llm_name": llm,
            "response": response,
            "accuracy": accuracy,
            "relevancy": relevancy,
            "response_time": response_time
        })

    db.session.commit()
    return jsonify(results)

# Route to fetch all evaluations
@app.route('/api/evaluations', methods=['GET'])
def get_evaluations():
    evaluations = Evaluation.query.all()
    result = [
        {
            'id': eval.id,
            'prompt': eval.prompt,
            'llm_name': eval.llm_name,
            'response': eval.response,
            'accuracy': eval.accuracy,
            'relevancy': eval.relevancy,
            'response_time': eval.response_time
        }
        for eval in evaluations
    ]
    return jsonify(result)

# Route to fetch analytics for dashboard
@app.route('/api/analytics', methods=['GET'])
def get_analytics():
    analytics = db.session.query(
        Evaluation.llm_name,
        db.func.avg(Evaluation.accuracy).label("avg_accuracy"),
        db.func.avg(Evaluation.relevancy).label("avg_relevancy"),
        db.func.avg(Evaluation.response_time).label("avg_response_time")
    ).group_by(Evaluation.llm_name).all()

    result = [
        {
            'llm_name': record.llm_name,
            'avg_accuracy': round(record.avg_accuracy, 2),
            'avg_relevancy': round(record.avg_relevancy, 2),
            'avg_response_time': round(record.avg_response_time, 2)
        }
        for record in analytics
    ]
    return jsonify(result)

# Initialize the database
with app.app_context():
    db.create_all()

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
