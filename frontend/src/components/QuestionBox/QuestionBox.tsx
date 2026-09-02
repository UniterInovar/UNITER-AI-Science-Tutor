import { useState } from "react";
import "./QuestionBox.css";

interface QuestionBoxProps {
  onAsk: (question: string) => void;
  loading: boolean;
}

export default function QuestionBox({
  onAsk,
  loading,
}: QuestionBoxProps) {
  const [question, setQuestion] = useState("");

  function handleSubmit() {
    if (!question.trim()) return;

    onAsk(question);
  }

  return (
    <div className="question-box">
      <textarea
        placeholder="Ask any Chemistry, Physics, Biology or Mathematics question..."
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        rows={5}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>
    </div>
  );
}