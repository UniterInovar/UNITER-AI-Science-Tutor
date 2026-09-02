export interface Attachment {
  id: string;
  file: File;
  type: "document" | "image";
}