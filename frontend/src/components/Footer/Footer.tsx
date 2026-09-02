export default function Footer() {
  return (
    <footer
      style={{
        padding: "20px",
        textAlign: "center",
        background: "#0f172a",
        color: "white",
      }}
    >
      © {new Date().getFullYear()} UNITER AI Science Tutor
    </footer>
  );
}