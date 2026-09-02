import "./Navbar.css";

export default function Navbar() {
  return (
    <header className="navbar">
      <div className="logo">
        🧪 UNITER AI Science Tutor
      </div>

      <nav>
        <a href="#">Home</a>
        <a href="#">Subjects</a>
        <a href="#">Practice</a>
        <a href="#">About</a>
      </nav>
    </header>
  );
}