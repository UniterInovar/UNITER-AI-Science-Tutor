export interface Message {
  id: string;
  sender: "user" | "ai";
  message: string;
  timestamp: string;
}