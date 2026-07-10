export default function Home() {
    return (

        <div
            style={{
                minHeight: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                background: "#f4f7fb",
            }}
        >

            <div
                style={{
                    width: "900px",
                    background: "white",
                    borderRadius: "15px",
                    padding: "50px",
                    boxShadow: "0 10px 30px rgba(0,0,0,.1)"
                }}
            >

                <h1
                    style={{
                        fontSize: "42px",
                        color: "#2563eb",
                        marginBottom: "10px"
                    }}
                >
                    UNITER AI Science Tutor
                </h1>

                <p
                    style={{
                        color: "#555",
                        marginBottom: "40px"
                    }}
                >
                    Learn Smarter with Artificial Intelligence
                </p>

                <input

                    placeholder="Ask any Chemistry, Physics, Biology or Mathematics question..."

                    style={{

                        width: "100%",

                        padding: "18px",

                        fontSize: "18px",

                        borderRadius: "10px",

                        border: "1px solid #ddd"

                    }}

                />

                <button

                    style={{

                        marginTop: "20px",

                        width: "100%",

                        padding: "18px",

                        background: "#2563eb",

                        color: "white",

                        border: "none",

                        borderRadius: "10px",

                        fontSize: "18px"

                    }}

                >

                    Ask AI

                </button>

                <div

                    style={{

                        marginTop: "40px",

                        background: "#eef4ff",

                        padding: "30px",

                        borderRadius: "12px"

                    }}

                >

                    <h2>

                        AI Response

                    </h2>

                    <p
                        style={{
                            marginTop: "20px"
                        }}
                    >

                        Your lesson will appear here.

                    </p>

                </div>

            </div>

        </div>

    );
}