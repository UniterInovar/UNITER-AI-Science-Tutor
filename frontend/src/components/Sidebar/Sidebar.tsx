import "./Sidebar.css";

import {
    FaFlask,
    FaAtom,
    FaLeaf,
    FaCalculator,
    FaBook,
    FaChartLine,
    FaCog
} from "react-icons/fa";

export default function Sidebar() {
    return (
        <aside className="sidebar">

            <h2>Subjects</h2>

            <ul>

                <li>
                    <FaFlask />
                    Chemistry
                </li>

                <li>
                    <FaAtom />
                    Physics
                </li>

                <li>
                    <FaLeaf />
                    Biology
                </li>

                <li>
                    <FaCalculator />
                    Mathematics
                </li>

            </ul>

            <h2>Learning</h2>

            <ul>

                <li>
                    <FaBook />
                    Lessons
                </li>

                <li>
                    <FaChartLine />
                    Progress
                </li>

                <li>
                    <FaCog />
                    Settings
                </li>

            </ul>

        </aside>
    );
}