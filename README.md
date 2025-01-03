# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Table Of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Learn More](#learn-more)
- [Usage](#usage)
- [Project Structure](#Project-structure)
- [Environment Variables](#environment-variables)
- [Experiment Results](#experiment-result)
- [API Routes](#api-routes)
## Introduction
The **LLM Evaluation Platform** is a versatile web-based application designed to streamline the evaluation and comparison of large language models (LLMs). In an era where LLMs are increasingly adopted across industries, selecting the right model for specific tasks requires a systematic and data-driven approach. This platform provides users with a unified interface to test LLMs, analyze their outputs, and visualize their performance through meaningful metrics.

Built with a robust backend powered by Flask and an intuitive frontend leveraging React and TypeScript, the platform enables users to input prompts, retrieve responses from multiple LLMs, and assess their performance side-by-side. By integrating essential metrics such as accuracy, relevancy, and response time, the platform empowers users to make informed decisions based on real data. Additionally, a feature-rich analytics dashboard provides clear and interactive visualizations of aggregated metrics, enabling deeper insights into model performance.

Whether you are a researcher exploring model capabilities or a developer deploying LLMs for business use cases, the LLM Evaluation Platform offers a comprehensive and scalable solution for evaluating LLMs effectively and efficiently.

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

## Features
### Compare multiple LLMs on standardized prompts.

### Evaluate models based on:

    - Precision

    - Recall

    - F1 Score

    - Perplexity

    - Response Time

### Visualize the results in a user-friendly dashboard.

### Store all experiment results in a local SQLite database.

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

# Usage
Submit a Prompt

Enter your prompt and reference response in the provided text areas.

Click on the Submit Prompt button to run the evaluation.

Results will be displayed in the table below.