export interface Equation {
  name: string;
  equation: string;
}

export interface TutorResponse {
  topic: string;
  definition: string;
  simple_explanation: string;
  detailed_explanation: string;
  equations: Equation[];
  applications: string[];
  exam_tips: string[];
  practice_questions: string[];
  related_topics: string[];
}

export interface AskAIResponse {
  success: boolean;
  question: string;
  subject: string;
  level: string;
  response: TutorResponse;
}