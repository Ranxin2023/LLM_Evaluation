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
- [API Routes](#api-routes)
## Introduction
The **LLM Evaluation Platform** is a versatile web-based application designed to streamline the evaluation and comparison of large language models (LLMs). In an era where LLMs are increasingly adopted across industries, selecting the right model for specific tasks requires a systematic and data-driven approach. This platform provides users with a unified interface to test LLMs, analyze their outputs, and visualize their performance through meaningful metrics.

Built with a robust backend powered by Flask and an intuitive frontend leveraging React and TypeScript, the platform enables users to input prompts, retrieve responses from multiple LLMs, and assess their performance side-by-side. By integrating essential metrics such as accuracy, relevancy, and response time, the platform empowers users to make informed decisions based on real data. Additionally, a feature-rich analytics dashboard provides clear and interactive visualizations of aggregated metrics, enabling deeper insights into model performance.

Whether you are a researcher exploring model capabilities or a developer deploying LLMs for business use cases, the LLM Evaluation Platform offers a comprehensive and scalable solution for evaluating LLMs effectively and efficiently.


## Installation

In the project directory, you can run:
1. install the front end
```sh
npm install

```
2. Runs the app in the development mode.

```sh
npm start

```

3. install the backend
```sh
pip install -r requirements.txt
python app.py
```
Open [http://localhost:3000](http://localhost:3000) to view it in the browser.

The page will reload if you make edits.\
You will also see any lint errors in the console.

4. `npm test`

Launches the test runner in the interactive watch mode.\
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

5. `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

6. `npm run eject`

**Note: this is a one-way operation. Once you `eject`, you can’t go back!**

If you aren’t satisfied with the build tool and configuration choices, you can `eject` at any time. This command will remove the single build dependency from your project.

Instead, it will copy all the configuration files and the transitive dependencies (webpack, Babel, ESLint, etc) right into your project so you have full control over them. All of the commands except `eject` will still work, but they will point to the copied scripts so you can tweak them. At this point you’re on your own.

You don’t have to ever use `eject`. The curated feature set is suitable for small and middle deployments, and you shouldn’t feel obligated to use this feature. However we understand that this tool wouldn’t be useful if you couldn’t customize it when you are ready for it.

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
| GPT-4      | 0.83      | 0.83     | 1.210             |
| GPT-4o-mini| 0.75      | 0.78     | 0.550             |
| Llama      | 0.55      | 0.65     | 0.430             |
| Gemma      | 0.50      | 0.85     | 0.300             |