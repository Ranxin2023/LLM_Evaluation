import React, { useState } from "react";

type ModelResult = {
  llm_name: string;
  response: string;
  perplexity: number;
  precision: number;
  // bleu_score: number;
  f1_score: number;
  response_time: number;
};
const App: React.FC = () => {
  const [prompt, setPrompt] = useState<string>("");
  // const [response, setResponse] = useState<string | null>(null);
  const [results, setResults] = useState<ModelResult[]>([
    {
      llm_name: "gpt-4",
      response: "",
      perplexity: 0,
      precision: 0,
      f1_score: 0,
      response_time: 0,
    },
    {
      llm_name: "gpt-4o-mini",
      response: "",
      perplexity: 0,
      precision: 0,
      f1_score: 0,
      response_time: 0,
    },
    {
      llm_name: "llama3-8b-8192",
      response: "",
      perplexity: 0,
      precision: 0,
      f1_score: 0,
      response_time: 0,
    },
    {
      llm_name: "gemma2-9b-it",
      response: "",
      perplexity: 0,
      precision: 0,
      f1_score: 0,
      response_time: 0,
    },
  ]);
  const [reference, setReference] = useState<string>("");

  const submitPrompt = async () => {
    if(!prompt){
      alert("Must enter a prompt")
      return 
    }
    const res = await fetch("http://127.0.0.1:5000/api/submit_prompt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt, reference}),
    });
    console.log(`res is${res}`)
    if (!res.ok) {
      throw new Error("Failed to fetch model results.");
    }

    const data = await res.json();
    setResults(data.results||[]); 
    
  };

  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      justifyContent: "center",
      minHeight: "100vh",
      background: "linear-gradient(to bottom, purple, indigo)",
      color: "white",
      fontFamily: "'Arial', sans-serif",
      padding: "20px",
    }}>
      <h1 style={{color: '#44ff22', fontWeight:'bold', fontSize:40}}>LLM Evaluation Platform</h1>
      <textarea
        rows={5}
        cols={50}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt here..."
        style={{
          marginBottom: "10px",
          width: "70%",
          padding: "10px",
          fontSize: "1rem",
          borderRadius: "5px",
          border: "1px solid #ccc",
          resize: "none",
        }}
      />
       <textarea
        rows={5}
        cols={50}
        value={reference}
        onChange={(e) => setReference(e.target.value)}
        placeholder="Enter the reference here..."
        style={{
          marginBottom: "10px",
          width: "70%",
          padding: "10px",
          fontSize: "1rem",
          borderRadius: "5px",
          border: "1px solid #ccc",
          resize: "none",
        }}
      />
      <br />
      <button
        onClick={submitPrompt}
        style={{
          backgroundColor: "#ff5733",
          color: "white",
          border: "none",
          padding: "15px 30px",
          fontSize: "1.2rem",
          cursor: "pointer",
          borderRadius: "5px",
          transition: "0.3s",
        }}
        onMouseEnter={(e) =>
          ((e.target as HTMLButtonElement).style.backgroundColor = "#ff8f66")
        }
        onMouseLeave={(e) =>
          ((e.target as HTMLButtonElement).style.backgroundColor = "#ff5733")
        }
      >
        Submit Prompt
      </button>

      {results.length > 0 && (
        <div> 
          <h2>Model Evaluation Results</h2>
          <table border={1} style={{
            marginTop: "20px",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "5px",
            background: "linear-gradient(to bottom, #ff5733, #aa8844)",
            color: "#fff",
            width: "80%",
            maxWidth: "1200px",
            textAlign: "left",
          }}>
            <thead>
              <tr>
                <th>Model Name</th>
                <th>Response</th>
                <th>Perplexity</th>
                <th>Precision</th>
                {/* <th>BLEU Score</th> */}
                <th>F1 Score</th>
                <th>Response Time (s)</th>
              </tr>
            </thead>
            <tbody>
              {results.map((result, index) => (
                <tr key={index}>
                  <td>{result.llm_name}</td>
                  <td>{result.response}</td>
                  <td>{result.perplexity}</td>
                  <td>{result.precision}</td>
                  {/* <td>{result.bleu_score}</td> */}
                  <td>{result.f1_score}</td>
                  <td>{result.response_time}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default App;
