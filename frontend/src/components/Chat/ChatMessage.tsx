import "./ChatMessage.css";

import type { Message } from "../../types/chat";

type ChatMessageProps = Omit<Message, "id" | "timestamp">;

export default function ChatMessage({
  sender,
  message,
}: ChatMessageProps) {
  return (
    <div className={`chat-message ${sender}`}>
      <div className="avatar">
        {sender === "user" ? "👤" : "🤖"}
      </div>

      <div className="bubble">
        {message}
      </div>
    </div>
  );
}