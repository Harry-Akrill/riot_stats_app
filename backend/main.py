from flask import request, jsonify
from config import app, db
from models import Game
from riot_api import get_player_stats
from urllib.parse import unquote

@app.route("/games", methods=["GET"])
def get_games():
    games = Game.query.all()
    json_games = list(map(lambda x: x.to_json(), games))
    return jsonify({"games": json_games})

@app.route("/games/<account_name>", methods=["GET"])
def get_games_by_user(account_name):
    account_name = unquote(account_name) 
    games = Game.query.filter_by(account_name=account_name).all()
    if not games:
        return jsonify({"error": "No games found for this user"}), 404
    json_games = list(map(lambda x: x.to_json(), games))
    return jsonify({"games": json_games})

@app.route("/unique_accounts", methods=["GET"])
def get_unique_accounts():
    unique_accounts = db.session.query(Game.account_name).distinct().all()
    
    accounts = [account[0] for account in unique_accounts] if unique_accounts else []

    return jsonify({"accounts": accounts}), 200 

@app.route("/games/details/<int:game_id>", methods=["GET"])
def get_game_details(game_id):
    game = Game.query.get(game_id)
    if not game:
        return jsonify({"error": "Game not found"}), 404
    return jsonify(game.to_json())


@app.route("/find_games", methods=["POST"])
def find_games():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        summoner_name = data.get("summonerName")
        tag_line = data.get("tagLine")
        region = data.get("region")
        role = data.get("role")
        num_games = data.get("numGames")
        queue = data.get("queue")

        if not all([summoner_name, tag_line, region, role, num_games, queue]):
            return jsonify({"error": "Missing required fields"}), 400

        player_stats = get_player_stats(summoner_name, tag_line, role, region, num_games, queue)

        games_data = []
        for i in range(len(player_stats["champion"])):
            game_data = {
                "champion": player_stats["champion"][i],
                "kills": player_stats["kills"][i],
                "deaths": player_stats["deaths"][i],
                "assists": player_stats["assists"][i],
                "win": player_stats["win"][i],
                "turretPlatesTaken": player_stats["turretPlatesTaken"][i],
                "dmgChamps14": player_stats["dmgChamps14"][i],
                "champLevel": player_stats["champLevel"][i],
                "damageToBuildings": player_stats["damageToBuildings"][i],
                "goldPerMinute": player_stats["goldPerMinute"][i],
                "damagePerMinute": player_stats["damagePerMinute"][i],
                "totalDmgChamps": player_stats["totalDmgChamps"][i],
                "visionScore": player_stats["visionScore"][i],
                "wardsPlaced": player_stats["wardsPlaced"][i],
                "controlWardsPlaced": player_stats["controlWardsPlaced"][i],
                "killParticipation": player_stats["killParticipation"][i],
                "teamDamagePercentage": player_stats["teamDamagePercentage"][i],
                "csdiff14min": player_stats["csdiff14min"][i],
                "golddiff14min": player_stats["golddiff14min"][i],
                "xpDiff14": player_stats["xpDiff14"][i],
                "goldDiff": player_stats["goldDiff"][i],
                "champXpDiff": player_stats["champXpDiff"][i],
                "opponentChampion": player_stats["opponentChampion"][i],
                "opponentKills": player_stats["opponentKills"][i],
                "opponentDeaths": player_stats["opponentDeaths"][i],
                "opponentAssists": player_stats["opponentAssists"][i],
                "opponentTurretPlatesTaken": player_stats["opponentTurretPlatesTaken"][i],
                "opponentDmgChamps14": player_stats["opponentDmgChamps14"][i],
                "opponentChampLevel": player_stats["opponentChampLevel"][i],
                "opponentDamageToBuildings": player_stats["opponentDamageToBuildings"][i],
                "opponentGoldPerMinute": player_stats["opponentGoldPerMinute"][i],
                "opponentDamagePerMinute": player_stats["opponentDamagePerMinute"][i],
                "opponentTotalDmgChamps": player_stats["opponentTotalDmgChamps"][i],
                "opponentVisionScore": player_stats["opponentVisionScore"][i],
                "opponentWardsPlaced": player_stats["opponentWardsPlaced"][i],
                "opponentControlWardsPlaced": player_stats["opponentControlWardsPlaced"][i],
                "opponentKillParticipation": player_stats["opponentKillParticipation"][i],
                "opponentTeamDamagePercentage": player_stats["opponentTeamDamagePercentage"][i],
            }
            games_data.append(game_data)

        for game_data in games_data:
            game = Game(
                account_name=summoner_name + "#" + tag_line,
                role=role,
                queue="SOLOQ" if queue == 420 else queue,
                champion=game_data.get("champion", ""),
                kills=game_data.get("kills", 0),
                deaths=game_data.get("deaths", 0),
                assists=game_data.get("assists", 0),
                win="WIN" if game_data.get("win", 0) == 1 else "LOSS",
                turret_plates_taken=game_data.get("turretPlatesTaken", 0),
                damage_to_champs_at_14=game_data.get("dmgChamps14", 0),
                lvl=game_data.get("champLevel", 0),
                damage_to_buildings=game_data.get("damageToBuildings", 0),
                gold_per_minute=game_data.get("goldPerMinute", 0),
                damage_per_minute=game_data.get("damagePerMinute", 0),
                total_damage_to_champs=game_data.get("totalDmgChamps", 0),
                vision_score=game_data.get("visionScore", 0),
                wards_placed=game_data.get("wardsPlaced", 0),
                control_wards_placed=game_data.get("controlWardsPlaced", 0),
                kill_participation=game_data.get("killParticipation", 0),
                team_damage_percentage=game_data.get("teamDamagePercentage", 0),
                cs_diff_at_14=game_data.get("csdiff14min", 0),
                gold_diff_at_14=game_data.get("golddiff14min", 0),
                xp_diff_at_14=game_data.get("xpDiff14", 0),
                gold_diff=game_data.get("goldDiff", 0),
                xp_diff=game_data.get("champXpDiff", 0),
                opponent_champion=game_data.get("opponentChampion", ""),
                opponent_kills=game_data.get("opponentKills", ""),
                opponent_deaths=game_data.get("opponentDeaths", ""),
                opponent_assists=game_data.get("opponentAssists", ""),
                opponent_turret_plates_taken=game_data.get("opponentTurretPlatesTaken", ""),
                opponent_damage_to_champs_at_14=game_data.get("opponentDmgChamps14", ""),
                opponent_lvl=game_data.get("opponentChampLevel", 0),
                opponent_damage_to_buildings=game_data.get("opponentDamageToBuildings", ""),
                opponent_gold_per_minute=game_data.get("opponentGoldPerMinute", ""),
                opponent_damage_per_minute=game_data.get("opponentDamagePerMinute", ""),
                opponent_total_damage_to_champs=game_data.get("opponentTotalDmgChamps", ""),
                opponent_vision_score=game_data.get("opponentVisionScore", ""),
                opponent_wards_placed=game_data.get("opponentWardsPlaced", ""),
                opponent_control_wards_placed=game_data.get("opponentControlWardsPlaced", ""),
                opponent_kill_participation=game_data.get("opponentKillParticipation", ""),
                opponent_team_damage_percentage=game_data.get("opponentTeamDamagePercentage", ""),
            )
            db.session.add(game)

        db.session.commit()
        return jsonify({"message": "Games saved successfully"}), 201

    except Exception as e:
        print(f"Error in /find_games: {e}")
        return jsonify({"error": str(e)}), 500
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)