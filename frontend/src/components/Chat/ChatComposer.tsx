import { useRef, useState } from "react";
import "./ChatComposer.css";

import type { Attachment } from "../../types/attachment";

interface ChatComposerProps {
  onSend?: (
    subject: string,
    message: string,
    attachments: Attachment[]
  ) => void;
}

export default function ChatComposer({
  onSend,
}: ChatComposerProps) {
  const [subject, setSubject] = useState("Chemistry");
  const [message, setMessage] = useState("");

  const [attachments, setAttachments] = useState<Attachment[]>([]);

  const documentInput = useRef<HTMLInputElement>(null);
  const imageInput = useRef<HTMLInputElement>(null);

  function addFiles(
    files: FileList | null,
    type: "document" | "image"
  ) {
    if (!files) return;

    const uploaded: Attachment[] = Array.from(files).map((file) => ({
      id: crypto.randomUUID(),
      file,
      type,
    }));

    setAttachments((prev) => [...prev, ...uploaded]);
  }

  function removeAttachment(id: string) {
    setAttachments((prev) =>
      prev.filter((item) => item.id !== id)
    );
  }

  function handleSend() {
    if (!message.trim()) return;

    onSend?.(
      subject,
      message,
      attachments
    );

    setMessage("");
    setAttachments([]);
  }

  return (
    <div className="chat-composer">
      <select
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
      >
        <option>Chemistry</option>
        <option>Physics</option>
        <option>Biology</option>
        <option>Mathematics</option>
      </select>

      <textarea
        rows={4}
        placeholder="Ask any science question..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />

      <input
        ref={documentInput}
        hidden
        multiple
        type="file"
        accept=".pdf,.doc,.docx,.txt"
        onChange={(e) =>
          addFiles(e.target.files, "document")
        }
      />

      <input
        ref={imageInput}
        hidden
        multiple
        type="file"
        accept="image/*"
        onChange={(e) =>
          addFiles(e.target.files, "image")
        }
      />

      <div className="composer-actions">

        <button
          onClick={() =>
            documentInput.current?.click()
          }
        >
          📎
        </button>

        <button
          onClick={() =>
            imageInput.current?.click()
          }
        >
          🖼️
        </button>

        <button>
          📷
        </button>

        <button>
          🎤
        </button>

        <button
          className="send-btn"
          onClick={handleSend}
        >
          ➤ Send
        </button>

      </div>

      {attachments.length > 0 && (

        <div className="attachment-list">

          {attachments.map((item) => (

            <div
              key={item.id}
              className="attachment-item"
            >
              <span>

                {item.type === "document"
                  ? "📄"
                  : "🖼️"}

                {" "}

                {item.file.name}

              </span>

              <button
                onClick={() =>
                  removeAttachment(item.id)
                }
              >
                ❌
              </button>

            </div>

          ))}

        </div>

      )}

    </div>
  );
}