import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const UserGameList = () => {
    const { accountName } = useParams();
    const [games, setGames] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchUserGames = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:5000/games/${encodeURIComponent(accountName)}`);
                if (!response.ok) {
                    throw new Error("Failed to fetch user games");
                }
                const data = await response.json();
                setGames(data.games);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchUserGames();
    }, [accountName]);

    if (loading) {
        return <p>Loading games...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    return (
        <div>
            <h2>Games for {accountName}</h2>
            <table>
                <thead>
                    <tr>
                        <th>Champion</th>
                        <th>Opponent Champion</th>
                        <th>Kills</th>
                        <th>Deaths</th>
                        <th>Assists</th>
                        <th>Win</th>
                        <th>Vision Score</th>
                    </tr>
                </thead>
                <tbody>
                    {games.map((game) => (
                        <tr key={game.id}>
                            <td>{game.champion}</td>
                            <td>{game.opponentChampion}</td>
                            <td>{game.kills}</td>
                            <td>{game.deaths}</td>
                            <td>{game.assists}</td>
                            <td>{game.win ? "Yes" : "No"}</td>
                            <td>{game.visionScore}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default UserGameList;