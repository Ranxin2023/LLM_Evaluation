import React, { useState } from "react";

const App: React.FC = () => {
  const [prompt, setPrompt] = useState<string>("");
  const [response, setResponse] = useState<string | null>(null);
  const [responseTime, setResponseTime] = useState<number | null>(null);

  const submitPrompt = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/submit_prompt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt }),
    });
    const data = await res.json();
    setResponse(data.response);
    setResponseTime(data.response_time);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>LLM Evaluation Platform</h1>
      <textarea
        rows={5}
        cols={50}
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt here..."
      />
      <br />
      <button onClick={submitPrompt} style={{ margin: "10px" }}>
        Submit Prompt
      </button>

      {response && (
        <div>
          <h2>Response:</h2>
          <p>{response}</p>
          <h2>Response Time:</h2>
          <p>{responseTime?.toFixed(2)} seconds</p>
        </div>
      )}
    </div>
  );
};

export default App;
