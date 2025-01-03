# LLM Evaluation

## Table Of Contents
- [Introduction](#introduction)
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Setup](#setup)
- [Learn More](#learn-more)
- [Usage](#usage)
- [Project Structure](#Project-structure)
- [Environment Variables](#environment-variables)
- [Experiment Results](#experiment-result)
- [Evaluations](#evaluations)
- [API Routes](#api-routes)
## Introduction
The **LLM Evaluation Platform** is a versatile web-based application designed to streamline the evaluation and comparison of large language models (LLMs). In an era where LLMs are increasingly adopted across industries, selecting the right model for specific tasks requires a systematic and data-driven approach. This platform provides users with a unified interface to test LLMs, analyze their outputs, and visualize their performance through meaningful metrics.

Built with a robust backend powered by Flask and an intuitive frontend leveraging React and TypeScript, the platform enables users to input prompts, retrieve responses from multiple LLMs, and assess their performance side-by-side. By integrating essential metrics such as accuracy, relevancy, and response time, the platform empowers users to make informed decisions based on real data. Additionally, a feature-rich analytics dashboard provides clear and interactive visualizations of aggregated metrics, enabling deeper insights into model performance.

Whether you are a researcher exploring model capabilities or a developer deploying LLMs for business use cases, the LLM Evaluation Platform offers a comprehensive and scalable solution for evaluating LLMs effectively and efficiently.

## Features
### Compare multiple LLMs on standardized prompts.

### Evaluate models based on criteria:

- **Precision**:
    Precision is the ratio of correctly predicted positive observations to the total predicted positive observations. It measures how many of the model's positive predictions were actually correct. High precision indicates that the model's positive predictions are accurate but does not consider missed positive cases (false negatives).

    Formula:
    **Precision = True Positives / (True Positives + False Positives)**

- **Recall**:
    Recall is the ratio of correctly predicted positive observations to all actual positive observations. It measures the model's ability to detect all relevant cases (sensitivity). High recall indicates that the model captures most of the true positive cases but may include some incorrect predictions.

    Formula:
    Recall = True Positives / (True Positives + False Negatives)

- **F1 Score**:
F1 Score is the harmonic mean of precision and recall. It provides a balanced measure that considers both precision and recall. It is especially useful when the dataset is imbalanced (e.g., many more negatives than positives).

Formula:
**F1 Score = 2 * (Precision * Recall) / (Precision + Recall)**

- **Perplexity**:
Perplexity is a measure of how well a probabilistic model predicts a sample. For language models, it evaluates how well the model predicts the likelihood of a sequence of words. Lower perplexity indicates a better-performing model, as it is more confident in its predictions.

Formula:
**Perplexity = exp(-Σ log(probabilities) / N)**
Where **N** is the total number of words in the sequence.
- **Response Time**: 
Response time measures how long the model takes to generate a response. It is an important factor in applications where speed and real-time interaction are critical. A shorter response time indicates better performance in terms of efficiency.

### Visualize the results in a user-friendly dashboard.

### Store all experiment results in a local SQLite database.

## Tech Stack

This project utilizes the following technologies:

### Frontend
- **React.js**: For building a dynamic and interactive user interface.
- **TypeScript**: Used for adding type safety and better developer experience.
- **CSS**: For styling components and layout.

### Backend
- **Flask**: Lightweight Python web framework for handling backend logic and API endpoints.
- **SQLite**: For storing LLM evaluation results and experiment data.

### Machine Learning Integration
- **OpenAI API**: For utilizing advanced language models like GPT-4.
- **Groq API**: For interacting with other supported LLMs.

### Libraries
- **dotenv**: For managing environment variables securely.
- **nltk**: For natural language processing tasks like BLEU score calculation.
- **sklearn**: For metrics calculation like F1 score.
- **requests**: For making HTTP calls to external APIs.

### Development Tools
- **npm**: For managing frontend dependencies and scripts.
- **Python**: For backend development.
- **Postman**: For testing API endpoints.
- **Visual Studio Code**: For code editing and debugging.

This stack was selected to ensure a balance of performance, scalability, and developer productivity.



## Setup

1. Clone the repository
```sh
git clone https://github.com/Ranxin2023/LLM_Evaluation
```
2. navigate to the project directory
```sh
cd llm-evaluation
```
3. install the front end
```sh
npm install

```
4. Runs the app in the development mode.

```sh
npm start

```

5. install the backend
```sh
pip install -r requirements.txt
python app.py
```
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

6. Obtain the API Keys
- Groq API Key
    - Visit the [Groq Developer Portal](https://www.groq.com/developer/).
    - Sign in or create an account if you don’t have one.
    - Navigate to the "API Keys" section.
    - Generate a new API key and copy it.
    - Add the key to your .env file as follows:
    ```sh
    GROQ_API_KEY=your_groq_api_key_here
    ```
- OpenAI API Key
    - Visit the [OpenAI API Platform](https://platform.openai.com/).
    - Sign in or create an account if you don’t have one.
    - Go to the "API Keys" section in your account settings.
    - Generate a new API key and copy it.
    - Add the key to your .env file as follows:
    ```sh
    OPENAI_API_KEY=your_openai_api_key_here
    ```
7. Set Up the SQLite Database
- Create the Database File:
Run the provided database setup script or manually create the database file in the `databases` folder:
```sh
python databases/connectSQLite.py
```
- Verify the Database Structure:
    - Ensure that the database file (`LLMEvaluationsReport.db`) contains the required tables such as `models` and any additional tables used for storing experiment results.
- Integrate with Backend:
    - Ensure the backend (`app.py`) points to the correct SQLite database path in the `.env` file:
    ```sh
    DATABASE_PATH=databases/LLMEvaluationsReport.db
    ```
## Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

To learn LLM Evaluation, check out the following:
- [LLM Evaluation Guide](https://www.superannotate.com/blog/llm-evaluation-guide)
- [LLM Evaluation Metrics](https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation)
- [LLMs as a Judge](https://arize.com/blog-course/llm-evaluation-the-definitive-guide/)

## Experiment Result
| Model Name | Precision | F1 Score | Response Time (s) |
|------------|-----------|----------|-------------------|
| GPT-4      | 0.85      | 0.83     | 1.210             |
| GPT-4o-mini| 0.75      | 0.78     | 0.550             |
| Llama      | 0.56      | 0.65     | 0.430             |
| Gemma      | 0.47      | 0.60     | 0.320             |

### Analysis of Results

1. **GPT-4 Performance**:
   - GPT-4 achieves the best precision (`0.85`) and F1 score (`0.83`), demonstrating its advanced understanding and response generation capabilities.
   - However, its response time (`1.210s`) is the longest, making it less suitable for low-latency applications.

2. **GPT-4o-mini**:
   - This model strikes a balance between precision and speed, with respectable precision (`0.75`) and a response time (`0.550s`) that is significantly faster than GPT-4.

3. **Llama**:
   - Llama provides reasonable precision (`0.56`) and F1 score (`0.65`) with a relatively fast response time (`0.430s`), making it a good choice for moderate-performance scenarios.

4. **Gemma**:
   - Although Gemma has the lowest precision (`0.55`) and F1 score (`0.60`), its response time (`0.320s`) is the fastest, making it an ideal choice for applications requiring real-time responses.

### Conclusion

The choice of model depends on the application's requirements:
- Use **GPT-4** for tasks demanding the highest accuracy and quality.
- Opt for **Gemma** when response time is critical.
- **GPT-4o-mini** and **Llama** provide balanced options for scenarios where both accuracy and speed are important.

## Usage
### Submit a Prompt

- Enter your prompt and reference response in the provided text areas.

- Click on the Submit Prompt button to run the evaluation.

- Results will be displayed in the table below.

## Project Strucuture
```sh
LLM-EVALUATION/
├── backend/
│   ├── app.py                     # Main backend application logic (Flask API)
│   ├── requirements.txt           # Python dependencies
│   ├── test.py                    # Backend test cases
├── databases/
│   ├── connectSQLite.py           # SQLite database connection logic
│   ├── LLMEvaluationsReport.db    # SQLite database file
├── node_modules/                  # Node.js modules
├── public/                        # Static assets for the React app
├── src/                           # Source code for the frontend React app
│   ├── App.css                    # App-wide CSS styles
│   ├── App.test.tsx               # Test cases for the App component
│   ├── App.tsx                    # Main React app component
│   ├── index.css                  # Global styles
│   ├── index.tsx                  # Entry point for React
│   ├── logo.svg                   # App logo
│   ├── reportWebVitals.ts         # Performance metrics
│   ├── setupTests.ts              # Test setup file
├── .env                           # Environment variables (API keys, database path)
├── .gitignore                     # Git ignore rules
├── package.json                   # npm dependencies and scripts
├── package-lock.json              # Lock file for npm dependencies
├── README.md                      # Project documentation
├── test_case.json                 # Test cases for model evaluation
```
### Key Folders

- backend/: Contains all backend-related logic, including the Flask server, database connection, and test files.

- databases/: Contains SQLite-related files for storing evaluation results.

- public/: Contains static assets like the favicon and the main HTML file.

- src/: Contains all frontend React code, including components, styles, and app configurations.

## Evaluations
In this project, the evaluation process is enhanced by introducing a Grader, which is used to assess the quality of model outputs. The Grader compares the model-generated response to the expected output and categorizes the match into three levels:

- Exact Match: The model's response perfectly matches the expected output.
- Partial Match: The model's response closely aligns with the expected output but may not be an exact match. This is common when language models use synonyms or similar phrases.
- Logical Match: The model's response contains some correct elements in logic but words deviates significantly from the expected output.

### How the Grader Works:
- Comparison Logic:
The Grader computes the similarity between the expected output and the model response using various metrics, such as:

    - F1 Score: The F1 score is used as a reference metric to determine the closeness of the match. Higher F1 scores indicate closer matches.
    - Precision and Recall: These metrics are also taken into account to provide a comprehensive evaluation.
- Manual Mapping (Optional):
If automated evaluation metrics are insufficient, manual grading can be performed to assign one of the three categories (Exact Match, LLM Match, Partial Match) based on subjective judgment.

### How to Get the Grader Result:
- Run the Evaluation:
Use the backend to submit a prompt and an expected output. The system will process the models and store the evaluation results in the database, including F1 scores and the Grader result.

### Build Test Cases
To ensure the reliability and robustness of the platform, various test cases were created. Each test case evaluates the system's ability to handle prompts, produce expected outputs, and calculate evaluation metrics.
- Test Case Structure
Each test case is defined by the following fields:

    - User Message: The input prompt provided to the system.
    - Expected Output: The anticipated response generated by the models.
    - Grader: The matching level (exact_match, partial_match, etc.) to evaluate the similarity between the generated response and the expected output.
- Test Case Example:

```json
{
    "prompt": "Explain photosynthesis.",
    "reference": "Photosynthesis is the process by which green plants use sunlight to synthesize nutrients from carbon dioxide and water.",
    "grader": "partial_match"
}
```
- View the Results:
The results, including the Grader evaluation, can be fetched from the database and displayed in the dashboard or directly accessed via the API. The grader categorization will be visible in the result table.