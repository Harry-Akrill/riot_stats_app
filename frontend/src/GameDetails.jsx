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
        
        <div style={{ display: "flex", alignItems: "flex-start", gap: "20px", flexWrap: "wrap" }}>
            <h2>{game.role} Lane Matchup</h2>
            <h2>WINNER - {game.win == "WIN" ? game.champion : game.opponentChampion} </h2>
            <div>
                <h2>Overall Game Stats</h2>
                <h3>{game.accountName} Stats:</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Stat</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>   
                        <tr>
                            <td>Champion</td>
                            <td><img
                                src={`https://ddragon.leagueoflegends.com/cdn/15.2.1/img/champion/${game.champion}.png`}
                                alt={game.champion}
                                width="45"
                                height="45"
                                style={{ margin: "0 5px", verticalAlign: "middle" }}
                            /></td>
                        </tr>
                        <tr>
                            <td>KDA</td>
                            <td>
                                {(game.deaths === 0 ? game.kills + game.assists : ((game.kills + game.assists) / game.deaths).toFixed(2))}
                            </td>
                        </tr>
                        <tr>
                            <td>Champion Level</td>
                            <td>{game.champLevel}</td>
                        </tr>
                        <tr>
                            <td>Kill Participation</td>
                            <td>{Math.round(game.killParticipation* 100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Gold per Minute</td>
                            <td>{Math.round(game.goldPerMinute*100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Damage per Minute</td>
                            <td>{Math.round(game.damagePerMinute)}</td>
                        </tr>
                    </tbody>
                </table>
            
                <h3>Opponent Stats:</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Stat</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Champion</td>
                            <td><img
                                    src={`https://ddragon.leagueoflegends.com/cdn/15.2.1/img/champion/${game.opponentChampion}.png`}
                                    alt={game.opponentChampion}
                                    width="45"
                                    height="45"
                                    style={{ margin: "0 5px", verticalAlign: "middle" }}
                            /></td>
                        </tr>
                        <tr>
                            <td>KDA</td>
                            <td>
                                {(game.opponentDeaths === 0 ? game.opponentKills + game.opponentAssists : ((game.opponentKills + game.opponentAssists) / game.opponentDeaths).toFixed(2))}
                            </td>
                        </tr>
                        <tr>
                            <td>Champion Level</td>
                            <td>{game.opponentChampLevel}</td>
                        </tr>
                        <tr>
                            <td>Kill Participation</td>
                            <td>{Math.round(game.opponentKillParticipation* 100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Gold per Minute</td>
                            <td>{Math.round(game.opponentGoldPerMinute*100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Damage per Minute</td>
                            <td>{Math.round(game.opponentDamagePerMinute)}</td>
                        </tr>
                    </tbody>
                </table>
                
            </div>
            <div>
            <h2>Laning Stats vs Opponent</h2>
            <h3>{game.accountName} Stats:</h3>
                <table>
                    <thead>
                        <tr>
                            <th>Stat</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Turret Plates Taken</td>
                            <td>
                                {game.turretPlatesTaken}
                            </td>
                        </tr>
                        <tr>
                            <td>Damage to Champs at 14</td>
                            <td>
                                {game.damageToChampsAt14}
                            </td>
                        </tr>
                        <tr>
                            <td>Champion Level</td>
                            <td>{game.opponentChampLevel}</td>
                        </tr>
                        <tr>
                            <td>Kill Participation</td>
                            <td>{Math.round(game.opponentKillParticipation* 100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Gold per Minute</td>
                            <td>{Math.round(game.opponentGoldPerMinute*100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Damage per Minute</td>
                            <td>{Math.round(game.opponentDamagePerMinute)}</td>
                        </tr>
                    </tbody>
                </table> 
                <h3>Opponent Stats:</h3> 
                <table>
                    <thead>
                        <tr>
                            <th>Stat</th>
                            <th>Value</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Turret Plates Taken</td>
                            <td>
                                {game.opponentTurretPlatesTaken}
                            </td>
                        </tr>
                        <tr>
                            <td>KDA</td>
                            <td>
                                {(game.opponentDeaths === 0 ? game.opponentKills + game.opponentAssists : ((game.opponentKills + game.opponentAssists) / game.opponentDeaths).toFixed(2))}
                            </td>
                        </tr>
                        <tr>
                            <td>Champion Level</td>
                            <td>{game.opponentChampLevel}</td>
                        </tr>
                        <tr>
                            <td>Kill Participation</td>
                            <td>{Math.round(game.opponentKillParticipation* 100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Gold per Minute</td>
                            <td>{Math.round(game.opponentGoldPerMinute*100) / 100}</td>
                        </tr>
                        <tr>
                            <td>Damage per Minute</td>
                            <td>{Math.round(game.opponentDamagePerMinute)}</td>
                        </tr>
                    </tbody>
                </table>
            </div>  
        </div>
        
    );
};

export default GameDetails;