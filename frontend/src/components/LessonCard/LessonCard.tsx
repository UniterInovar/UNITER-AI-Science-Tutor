import "./LessonCard.css";

import type { TutorResponse } from "../../types/tutor";

interface LessonCardProps {
  lesson: TutorResponse | null;
}

export default function LessonCard({ lesson }: LessonCardProps) {
  if (!lesson) {
    return (
      <div className="lesson-card empty">
        <h3>AI Response</h3>
        <p>Your lesson will appear here.</p>
      </div>
    );
  }

  return (
    <div className="lesson-card">
      <h2>{lesson.topic}</h2>

      <section>
        <h3>Definition</h3>
        <p>{lesson.definition}</p>
      </section>

      <section>
        <h3>Simple Explanation</h3>
        <p>{lesson.simple_explanation}</p>
      </section>

      <section>
        <h3>Detailed Explanation</h3>
        <p>{lesson.detailed_explanation}</p>
      </section>

      {lesson.equations.length > 0 && (
        <section>
          <h3>Equations</h3>

          {lesson.equations.map((eq) => (
            <div
              key={eq.name}
              className="equation"
            >
              <strong>{eq.name}</strong>

              <code>{eq.equation}</code>
            </div>
          ))}
        </section>
      )}

      <section>
        <h3>Applications</h3>

        <ul>
          {lesson.applications.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </section>

      <section>
        <h3>Exam Tips</h3>

        <ul>
          {lesson.exam_tips.map((tip) => (
            <li key={tip}>{tip}</li>
          ))}
        </ul>
      </section>

      <section>
        <h3>Practice Questions</h3>

        <ul>
          {lesson.practice_questions.map((q) => (
            <li key={q}>{q}</li>
          ))}
        </ul>
      </section>
    </div>
  );
}