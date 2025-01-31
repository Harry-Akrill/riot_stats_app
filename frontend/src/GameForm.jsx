import { useState } from "react";

const GameForm = ({ onGameAdded }) => {
    const [summonerName, setSummonerName] = useState("");
    const [tagLine, setTagLine] = useState("");
    const [region, setRegion] = useState("europe");
    const [role, setRole] = useState("TOP");
    const [numGames, setNumGames] = useState(10);
    const [queue, setQueue] = useState(420);
    const [loading, setLoading] = useState(false);

    const onSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await fetch("http://127.0.0.1:5000/find_games", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    summonerName,
                    tagLine,
                    region,
                    role,
                    numGames,
                    queue,
                }),
            });

            if (!response.ok) {
                throw new Error("Failed to save games to the database");
            }

            alert("Games successfully saved!");
            onGameAdded();
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred. Please try again.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="summonerName">Summoner Name:</label>
                <input
                    type="text"
                    id="summonerName"
                    value={summonerName}
                    onChange={(e) => setSummonerName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="tagLine">Tag Line:</label>
                <input
                    type="text"
                    id="tagLine"
                    value={tagLine}
                    onChange={(e) => setTagLine(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="region">Region:</label>
                <select
                    id="region"
                    value={region}
                    onChange={(e) => setRegion(e.target.value)}
                >
                    <option value="europe">Europe</option>
                    <option value="na">North America</option>
                    <option value="kr">Korea</option>
                </select>
            </div>
            <div>
                <label htmlFor="role">Role:</label>
                <select
                    id="role"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                >
                    <option value="TOP">Top</option>
                    <option value="JUNGLE">Jungle</option>
                    <option value="MIDDLE">Mid</option>
                    <option value="BOTTOM">Bottom</option>
                    <option value="UTILITY">Support</option>
                </select>
            </div>
            <div>
                <label htmlFor="numGames">Number of Games:</label>
                <input
                    type="number"
                    id="numGames"
                    value={numGames}
                    onChange={(e) => setNumGames(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="queue">Queue ID:</label>
                <input
                    type="number"
                    id="queue"
                    value={queue}
                    onChange={(e) => setQueue(e.target.value)}
                />
            </div>
            <button type="submit" disabled={loading}>
                {loading ? "Searching..." : "Submit"}
            </button>
        </form>
    );
};

export default GameForm;