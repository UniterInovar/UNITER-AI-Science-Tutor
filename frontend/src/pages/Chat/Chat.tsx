import ChatWindow from "../../components/Chat/ChatWindow";
import ChatComposer from "../../components/Chat/ChatComposer";

import type { Message } from "../../types/chat";
import type { Attachment } from "../../types/attachment";

export default function Chat() {
  const messages: Message[] = [
    {
      id: 1,
      sender: "user",
      message: "What is Electrolysis?",
    },
    {
      id: 2,
      sender: "ai",
      message:
        "Electrolysis is the chemical decomposition of an electrolyte using electric current.",
    },
  ];

  function handleSend(
    subject: string,
    message: string,
    attachments: Attachment[]
  ) {
    console.log(subject);
    console.log(message);
    console.log(attachments);

    alert(
      `${subject}

${message}

Attachments: ${attachments.length}`
    );
  }

  return (
    <>
      <ChatWindow messages={messages} />

      <ChatComposer onSend={handleSend} />
    </>
  );
}