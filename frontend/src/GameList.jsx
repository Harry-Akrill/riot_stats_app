import React from "react"

const GameList = ({games}) => {
    return <div>
        <h2>Games</h2>
        <table>
            <thead>
                <tr>
                    <th>Account Name</th>
                    <th>Role</th>
                    <th>Queue</th>
                    <th>Champion</th>
                    <th>Opponent Champion</th>
                    <th>Kills</th>
                    <th>Deaths</th>
                    <th>Assists</th>
                    <th>Level</th>
                    <th>Opponent Level</th>
                    <th>Win</th>
                    <th>Vision Score</th>
                    <th>Control Wards Placed</th>
                    <th>Wards Placed</th>
                    <th>Kill Participation</th>
                    <th>CS Diff @ 14</th>
                    <th>Gold Diff @ 14</th>
                    <th>XP Diff @ 14</th>
                    <th>Damage to Champions @ 14</th>
                    <th>Turret Plates Taken</th>
                    <th>Gold Diff @ Game End</th>
                    <th>XP Diff @ Game End</th>
                    <th>Total Damage to Champions</th>
                    <th>% of Team Damage</th>
                    <th>Gold per Minute</th>
                    <th>Damage per Minute</th>
                    <th>Damage to Buildings</th>
                </tr>
            </thead>
            <tbody>
                {games.map((game) => (
                    <tr key={game.id}>
                        <td>{game.accountName}</td>
                        <td>{game.role}</td>
                        <td>{game.queue}</td>
                        <td>{game.champion}</td>
                        <td>{game.opponentChampion}</td>
                        <td>{game.kills}</td>
                        <td>{game.deaths}</td>
                        <td>{game.assists}</td>
                        <td>{game.champLevel}</td>
                        <td>{game.opponentChampLevel}</td>
                        <td>{game.win}</td>
                        <td>{game.visionScore}</td>
                        <td>{game.controlWardsPlaced}</td>
                        <td>{game.wardsPlaced}</td>
                        <td>{game.killParticipation}</td>
                        <td>{game.csDiffAt14}</td>
                        <td>{game.goldDiffAt14}</td>
                        <td>{game.xpDiffAt14}</td>
                        <td>{game.damageToChampsAt14}</td>
                        <td>{game.turretPlatesTaken}</td>
                        <td>{game.goldDiff}</td>
                        <td>{game.xpDiff}</td>
                        <td>{game.totalDamageToChamps}</td>
                        <td>{game.teamDamagePercentage}</td>
                        <td>{game.goldPerMinute}</td>
                        <td>{game.damagePerMinute}</td>
                        <td>{game.damageToBuildings}</td>
                        
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default GameList