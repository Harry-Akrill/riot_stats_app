import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import GameList from "./GameList";
import GameForm from "./GameForm";
import UserGameList from "./UserGameList";
import "./App.css";
import GameDetails from "./GameDetails";

function App() {
    const [games, setGames] = useState([]);
    const [accounts, setAccounts] = useState([]);
    const [loading, setLoading] = useState(false);
    const [isDropdownOpen, setIsDropdownOpen] = useState(false);

    useEffect(() => {
        fetchGames();
        fetchUniqueAccounts();
    }, []);

    const fetchGames = async () => {
        setLoading(true);
        try {
            const response = await fetch("http://127.0.0.1:5000/games");
            const data = await response.json();
            setGames(data.games);
        } catch (error) {
            console.error("Error fetching games:", error);
        } finally {
            setLoading(false);
        }
    };

    const toggleDropdown = () => {
        setIsDropdownOpen(!isDropdownOpen);
    };

    const fetchUniqueAccounts = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/unique_accounts");
            const data = await response.json();
            console.log(data)
            setAccounts(data.accounts);
        } catch (error) {
            console.error("Error fetching unique accounts:", error);
        }
    };

    return (
        <Router>
            <div>
                <h1>Game Tracker</h1>
                <nav>
                    <Link to="/" className="link">Home</Link>
                    <Link to="/gameform">Add Games</Link>
                    <div className="dropdown" onClick={toggleDropdown}>
                        <span className="dropdown-toggle">
                            Accounts <span className="caret">&#9660;</span>
                        </span>
                        {isDropdownOpen && (
                            <ul className="dropdown-content">
                                {accounts.length > 0 ? (
                                    accounts.map((account) => (
                                        <li key={account}>
                                            <Link to={`/user_games/${encodeURIComponent(account)}`}>{account}</Link>
                                        </li>
                                    ))
                                ) : (
                                    <li>No user accounts found.</li>
                                )}
                            </ul>
                        )}
                    </div>
                </nav>
                <Routes>
                    <Route
                        path="/gameform"
                        element={<GameForm onGameAdded={fetchGames} />}
                    />
                    <Route
                        path="/user_games/:accountName"
                        element={<UserGameList />}
                    />
                    <Route 
                        path="/games/details/:gameId" 
                        element={<GameDetails />} 
                    />
                </Routes>
            </div>
        </Router>
    );
};

export default App;