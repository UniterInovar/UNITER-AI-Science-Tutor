import ChatMessage from "../components/Chat/ChatMessage";

export default function Home() {
  return (
    <>
      <ChatMessage
        sender="user"
        message="What is Electrolysis?"
      />

      <ChatMessage
        sender="ai"
        message="Electrolysis is the chemical decomposition of an electrolyte by the passage of electric current."
      />
    </>
  );
}