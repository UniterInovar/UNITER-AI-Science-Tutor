import { useState } from "react";
import api from "./services/api";
import type { TutorResponse } from "./types/tutor";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<TutorResponse | null>(null);
  const [error, setError] = useState("");

  const askAI = async () => {
    if (question.trim() === "") return;

    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await api.post<TutorResponse>("/ai/ask", {
        question,
      });

      setResult(response.data);
    } catch (err) {
      console.error(err);
      setError("Unable to connect to the AI Tutor.");
    }

    setLoading(false);
  };

  return (
    <div className="container">

      <h1>UNITER AI Science Tutor</h1>

      <p className="subtitle">
        Ask any Chemistry, Physics, Biology or Mathematics question.
      </p>

      <textarea
        rows={4}
        placeholder="Example: Explain electrolysis."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
      />

      <button onClick={askAI}>
        Ask AI
      </button>

      {loading && (
        <p className="loading">
          Thinking...
        </p>
      )}

      {error && (
        <p className="error">
          {error}
        </p>
      )}

      {result && (
        <div className="lesson">

          <h2>{result.response.topic}</h2>

          <h3>Definition</h3>

          <p>{result.response.definition}</p>

          <h3>Simple Explanation</h3>

          <p>{result.response.simple_explanation}</p>

          <h3>Detailed Explanation</h3>

          <p>{result.response.detailed_explanation}</p>

          <h3>Equations</h3>

          <ul>
            {result.response.equations.map((eq, index) => (
              <li key={index}>
                <strong>{eq.name}</strong>: {eq.equation}
              </li>
            ))}
          </ul>

          <h3>Applications</h3>

          <ul>
            {result.response.applications.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>Exam Tips</h3>

          <ul>
            {result.response.exam_tips.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>Practice Questions</h3>

          <ul>
            {result.response.practice_questions.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

          <h3>Related Topics</h3>

          <ul>
            {result.response.related_topics.map((item, index) => (
              <li key={index}>{item}</li>
            ))}
          </ul>

        </div>
      )}

    </div>
  );
}

export default App;