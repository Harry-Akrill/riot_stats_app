import requests
import time
from api_key import API_KEY

def get_puuid(summoner_name, tag_line, region):
    url = f"https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}?api_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['puuid']
    except requests.exceptions.RequestException as e:
        print(f"Error getting puuid: {e}")
        return None

def get_match_ids(puuid, region, num_games, queue):
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={num_games}&queue={queue}&api_key={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error getting match ids: {e}")
        return None

def get_match_data(match_id, region):
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={API_KEY}"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 429:
                print("Rate limit hit for getting match data, sleeping for 10 seconds...")
                time.sleep(10)
                continue
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching match data: {e}")
            return None

def get_player_data(match_data, puuid):
    participants = match_data["metadata"]["participants"]
    player_index = participants.index(puuid)
    return match_data["info"]["participants"][player_index]

def get_match_timeline(match_id, region):
    url = f"https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={API_KEY}"
    while True:
        try:
            response = requests.get(url)
            if response.status_code == 429:
                print("Rate limit hit for getting match timeline, sleeping for 10 seconds...")
                time.sleep(10)
                continue
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching match timeline: {e}")
            return None

def get_player_stats_at_time(match_timeline, puuid, frame_no):
    participant_info = match_timeline["info"]["participants"]
    participant_id = next((p["participantId"] for p in participant_info if p["puuid"] == puuid), None)
    if participant_id is None:
        raise ValueError("Player PUUID not found in match timeline data")
    return match_timeline["info"]["frames"][frame_no]["participantFrames"][str(participant_id)]

def find_lane_opponent_puuid(match_data, player_data):
    role = player_data["individualPosition"]
    participants = match_data["info"]["participants"]
    for participant in participants:
        if participant["individualPosition"] == role and participant["puuid"] != player_data["puuid"]:
            return participant["puuid"]
    return ""

def gather_all_data(puuid, role, match_ids, region):
    data = {
        "champion": [],
        "kills": [],
        "deaths": [],
        "assists": [],
        "win": [],
        "turretPlatesTaken": [],
        "dmgChamps14": [],
        "champLevel": [],
        "damageToBuildings": [],
        "goldPerMinute": [],
        "damagePerMinute": [],
        "totalDmgChamps": [],
        "visionScore": [],
        "visionWardsBoughtInGame": [],
        "wardsPlaced": [],
        "controlWardsPlaced": [],
        "completeSupportQuestInTime": [],
        "killParticipation": [],
        "visionScorePerMinute": [],
        "wardTakedowns": [],
        "teamDamagePercentage": [],
        "csdiff14min": [],
        "jungleCsdiff14": [],
        "golddiff14min": [],
        "xpDiff14": [],
        "goldDiff": [],
        "champXpDiff": [],
        "opponentChampion": [],
        "opponentKills": [],
        "opponentDeaths": [],
        "opponentAssists": [],
        "opponentTurretPlatesTaken": [],
        "opponentDmgChamps14": [],
        "opponentChampLevel": [],
        "opponentChampLevel": [],
        "opponentDamageToBuildings": [],
        "opponentGoldPerMinute": [],
        "opponentDamagePerMinute": [],
        "opponentTotalDmgChamps": [],
        "opponentVisionScore": [],
        "opponentVisionWardsBoughtInGame": [],
        "opponentWardsPlaced": [],
        "opponentControlWardsPlaced": [],
        "opponentCompleteSupportQuestInTime": [],
        "opponentKillParticipation": [],
        "opponentVisionScorePerMinute": [],
        "opponentWardTakedowns": [],
        "opponentTeamDamagePercentage": []
    }

    for match_id in match_ids:
        match_data = get_match_data(match_id, region)
        if not match_data:
            continue

        player_data = get_player_data(match_data, puuid)
        if not player_data:
            continue

        if role.upper() != player_data["individualPosition"]:
            continue

        match_timeline = get_match_timeline(match_id, region)
        if not match_timeline:
            continue

        if match_data["info"]["gameDuration"] / 60 < 14:
            continue

        opponent_puuid = find_lane_opponent_puuid(match_data, player_data)
        if not opponent_puuid:
            continue

        opponent_player_data = get_player_data(match_data, opponent_puuid)
        if not opponent_player_data:
            continue

        stats_at_14 = get_player_stats_at_time(match_timeline, puuid, 14)
        opponent_stats_at_14 = get_player_stats_at_time(match_timeline, opponent_puuid, 14)

        #primary champion
        data["champion"].append(player_data["championName"])
        data["kills"].append(player_data["kills"])
        data["deaths"].append(player_data["deaths"])
        data["assists"].append(player_data["assists"])
        data["win"].append(int(player_data["win"]))
        data["turretPlatesTaken"].append(player_data["challenges"]["turretPlatesTaken"])
        data["dmgChamps14"].append(stats_at_14["damageStats"]["totalDamageDoneToChampions"])
        data["champLevel"].append(player_data["champLevel"])
        data["damageToBuildings"].append(player_data["damageDealtToBuildings"])
        data["goldPerMinute"].append(player_data["challenges"]["goldPerMinute"])
        data["damagePerMinute"].append(player_data["challenges"]["damagePerMinute"])
        data["totalDmgChamps"].append(player_data["totalDamageDealtToChampions"])
        data["visionScore"].append(player_data["visionScore"])
        data["visionWardsBoughtInGame"].append(player_data["visionWardsBoughtInGame"])
        data["wardsPlaced"].append(player_data["wardsPlaced"])
        data["controlWardsPlaced"].append(player_data["challenges"]["controlWardsPlaced"])
        data["completeSupportQuestInTime"].append(player_data["challenges"]["completeSupportQuestInTime"])
        data["killParticipation"].append(player_data["challenges"]["killParticipation"] * 100)
        data["visionScorePerMinute"].append(player_data["challenges"]["visionScorePerMinute"])
        data["wardTakedowns"].append(player_data["challenges"]["wardTakedowns"])
        data["teamDamagePercentage"].append(player_data["challenges"]["teamDamagePercentage"] * 100)

        #differentials
        data["csdiff14min"].append(stats_at_14["minionsKilled"] - opponent_stats_at_14["minionsKilled"])
        data["jungleCsdiff14"].append(stats_at_14["jungleMinionsKilled"] - opponent_stats_at_14["jungleMinionsKilled"])
        data["golddiff14min"].append(stats_at_14["totalGold"] - opponent_stats_at_14["totalGold"])
        data["xpDiff14"].append(stats_at_14["xp"] - opponent_stats_at_14["xp"])
        data["goldDiff"].append(player_data["goldEarned"] - opponent_player_data["goldEarned"])
        data["champXpDiff"].append(player_data["champExperience"] - opponent_player_data["champExperience"])

        data["opponentChampion"].append(opponent_player_data["championName"])
        data["opponentChampLevel"].append(opponent_player_data["champLevel"])
        data["opponentKills"].append(opponent_player_data["kills"])
        data["opponentDeaths"].append(opponent_player_data["deaths"])
        data["opponentAssists"].append(opponent_player_data["assists"])
        data["opponentTurretPlatesTaken"].append(opponent_player_data["challenges"]["turretPlatesTaken"])
        data["opponentDmgChamps14"].append(opponent_stats_at_14["damageStats"]["totalDamageDoneToChampions"])
        data["opponentChampLevel"].append(opponent_player_data["champLevel"])
        data["opponentDamageToBuildings"].append(opponent_player_data["damageDealtToBuildings"])
        data["opponentGoldPerMinute"].append(opponent_player_data["challenges"]["goldPerMinute"])
        data["opponentDamagePerMinute"].append(opponent_player_data["challenges"]["damagePerMinute"])
        data["opponentTotalDmgChamps"].append(opponent_player_data["totalDamageDealtToChampions"])
        data["opponentVisionScore"].append(opponent_player_data["visionScore"])
        data["opponentVisionWardsBoughtInGame"].append(opponent_player_data["visionWardsBoughtInGame"])
        data["opponentWardsPlaced"].append(opponent_player_data["wardsPlaced"])
        data["opponentControlWardsPlaced"].append(opponent_player_data["challenges"]["controlWardsPlaced"])
        data["opponentCompleteSupportQuestInTime"].append(opponent_player_data["challenges"]["completeSupportQuestInTime"])
        data["opponentKillParticipation"].append(opponent_player_data["challenges"]["killParticipation"] * 100)
        data["opponentVisionScorePerMinute"].append(opponent_player_data["challenges"]["visionScorePerMinute"])
        data["opponentWardTakedowns"].append(opponent_player_data["challenges"]["wardTakedowns"])
        data["opponentTeamDamagePercentage"].append(opponent_player_data["challenges"]["teamDamagePercentage"] * 100)


    print("Data gathered:", data)  # Debug print
    return data

def get_player_stats(summoner_name, tag_line, role, region, num_games, queue_id):
    puuid = get_puuid(summoner_name, tag_line, region)
    match_ids = get_match_ids(puuid, region, num_games, queue_id)
    data = gather_all_data(puuid, role, match_ids, region)
    return data