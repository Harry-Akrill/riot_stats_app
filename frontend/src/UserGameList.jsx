import React, { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

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
        <div className="table-container">
            <h2>Games for {accountName}</h2>
            <table>
            <thead>
                <tr>
                    <th>Account Name</th>
                    <th>Role</th>
                    <th>Queue</th>
                    <th>Champion</th>
                    <th>Win</th>
                    <th>KDA</th>
                    <th>Level</th>
                    <th>Kill Participation</th>
                    <th>Opponent Champion</th>
                    <th>Opponent Level</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                {games.map((game) => (
                    <tr key={game.id}>
                        <td>{game.accountName}</td>
                        <td>{game.role}</td>
                        <td>{game.queue}</td>
                        <td><img
                            src={`https://ddragon.leagueoflegends.com/cdn/15.2.1/img/champion/${game.champion}.png`}
                            alt={game.champion}
                            width="30"
                            height="30"
                            style={{ margin: "0 5px", verticalAlign: "middle" }}
                        /></td>
                        <td>{game.win}</td>
                        <td>
                            {(game.deaths === 0 ? game.kills + game.assists : ((game.kills + game.assists) / game.deaths).toFixed(2))}
                        </td>
                        <td>{game.champLevel}</td>
                        <td>{Math.round(game.killParticipation* 100) / 100} %</td>
                        <td><img
                            src={`https://ddragon.leagueoflegends.com/cdn/15.2.1/img/champion/${game.opponentChampion}.png`}
                            alt={game.opponentChampion}
                            width="30"
                            height="30"
                            style={{ margin: "0 5px", verticalAlign: "middle" }}
                        /></td>
                        <td>{game.opponentChampLevel}</td>
                        <td>
                            <Link to={`/games/details/${game.id}`}>View</Link>
                        </td>
                    </tr>
                ))}
            </tbody>
            </table>
        </div>
    );
};

export default UserGameList;