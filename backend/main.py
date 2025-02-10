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
                "opponentChampion": player_stats["opponentChampion"][i],
                "kills": player_stats["kills"][i],
                "deaths": player_stats["deaths"][i],
                "assists": player_stats["assists"][i],
                "champLevel": player_stats["champLevel"][i],
                "opponentChampLevel": player_stats["opponentChampLevel"][i],
                "win": player_stats["win"][i],
                "visionScore": player_stats["visionScore"][i],
                "controlWardsPlaced": player_stats["controlWardsPlaced"][i],
                "wardsPlaced": player_stats["wardsPlaced"][i],
                "killParticipation": player_stats["killParticipation"][i],
                "csdiff14min": player_stats["csdiff14min"][i],
                "turretPlatesTaken": player_stats["turretPlatesTaken"][i],
                "golddiff14min": player_stats["golddiff14min"][i],
                "xpDiff14": player_stats["xpDiff14"][i],
                "dmgChamps14": player_stats["dmgChamps14"][i],
                "totalDmgChamps": player_stats["totalDmgChamps"][i],
                "teamDamagePercentage": player_stats["teamDamagePercentage"][i],
                "champXpDiff": player_stats["champXpDiff"][i],
                "goldDiff": player_stats["goldDiff"][i],
                "goldPerMinute": player_stats["goldPerMinute"][i],
                "damagePerMinute": player_stats["damagePerMinute"][i],
                "damageToBuildings": player_stats["damageToBuildings"][i],
            }
            games_data.append(game_data)

        for game_data in games_data:
            game = Game(
                account_name=summoner_name + "#" + tag_line,
                role=role,
                queue="SOLOQ" if queue == 420 else queue,
                champion=game_data.get("champion", ""),
                opponent_champion=game_data.get("opponentChampion", ""),
                kills=game_data.get("kills", 0),
                deaths=game_data.get("deaths", 0),
                assists=game_data.get("assists", 0),
                lvl=game_data.get("champLevel", 0),
                opponent_lvl=game_data.get("opponentChampLevel", 0),
                win="WIN" if game_data.get("win", 0) == 1 else "LOSS",
                vision_score=game_data.get("visionScore", 0),
                control_wards_placed=game_data.get("controlWardsPlaced", 0),
                wards_placed=game_data.get("wardsPlaced", 0),
                kill_participation=game_data.get("killParticipation", 0),
                cs_diff_at_14=game_data.get("csdiff14min", 0),
                turret_plates_taken=game_data.get("turretPlatesTaken", 0),
                gold_diff_at_14=game_data.get("golddiff14min", 0),
                xp_diff_at_14=game_data.get("xpDiff14", 0),
                damage_to_champs_at_14=game_data.get("dmgChamps14", 0),
                total_damage_to_champs=game_data.get("totalDmgChamps", 0),
                team_damage_percentage=game_data.get("teamDamagePercentage", 0),
                xp_diff=game_data.get("champXpDiff", 0),
                gold_diff=game_data.get("goldDiff", 0),
                gold_per_minute=game_data.get("goldPerMinute", 0),
                damage_per_minute=game_data.get("damagePerMinute", 0),
                damage_to_buildings=game_data.get("damageToBuildings", 0),
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