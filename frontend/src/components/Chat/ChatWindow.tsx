import "./ChatWindow.css";

import ChatMessage from "./ChatMessage";
import type { Message } from "../../types/chat";

interface ChatWindowProps {
  messages: Message[];
}

export default function ChatWindow({
  messages,
}: ChatWindowProps) {
  return (
    <div className="chat-window">
      {messages.map((msg) => (
        <ChatMessage
          key={msg.id}
          sender={msg.sender}
          message={msg.message}
        />
      ))}
    </div>
  );
}