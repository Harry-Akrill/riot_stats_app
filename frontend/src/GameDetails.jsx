import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

const GameDetails = () => {
    const { gameId } = useParams();
    const [game, setGame] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    useEffect(() => {
        const fetchGameDetails = async () => {
            try {
                const response = await fetch(`http://127.0.0.1:5000/games/details/${gameId}`);
                if (!response.ok) {
                    throw new Error("Failed to fetch game details");
                }
                const data = await response.json();
                setGame(data);
            } catch (error) {
                setError(error.message);
            } finally {
                setLoading(false);
            }
        };

        fetchGameDetails();
    }, [gameId]);

    if (loading) {
        return <p>Loading game details...</p>;
    }

    if (error) {
        return <p>Error: {error}</p>;
    }

    if (!game) {
        return <p>Game not found.</p>;
    }

    return (
        <div>
            <h2>Game Details</h2>
            <table>
                <thead>
                    <tr>
                        <th>Stat</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {Object.entries(game).map(([key, value]) => (
                        <tr key={key}>
                            <td>{key}</td>
                            <td>{value}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default GameDetails;