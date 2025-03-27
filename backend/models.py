from config import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    queue = db.Column(db.String(80), nullable=False)

    champion = db.Column(db.String(80), unique=False, nullable=False)
    kills = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    win = db.Column(db.Integer, nullable=False)
    turret_plates_taken = db.Column(db.Integer, nullable=False)
    damage_to_champs_at_14 = db.Column(db.Integer, nullable=False)
    lvl = db.Column(db.Integer, nullable=False)
    damage_to_buildings = db.Column(db.Integer, nullable=False)
    gold_per_minute = db.Column(db.Integer, nullable=False)
    damage_per_minute = db.Column(db.Integer, nullable=False)
    total_damage_to_champs = db.Column(db.Integer, nullable=False)
    vision_score = db.Column(db.Integer, nullable=False)
    wards_placed = db.Column(db.Integer, nullable=False)
    control_wards_placed = db.Column(db.Integer, nullable=False)
    kill_participation = db.Column(db.Float, nullable=False)
    team_damage_percentage = db.Column(db.Float, nullable=False)

    cs_diff_at_14 = db.Column(db.Integer, nullable=False)
    gold_diff_at_14 = db.Column(db.Integer, nullable=False)
    xp_diff_at_14 = db.Column(db.Integer, nullable=False)
    gold_diff = db.Column(db.Integer, nullable=False)
    xp_diff = db.Column(db.Integer, nullable=False)

    opponent_champion = db.Column(db.String(80), unique=False, nullable=False)
    opponent_kills = db.Column(db.Integer, nullable=False)
    opponent_deaths = db.Column(db.Integer, nullable=False)
    opponent_assists = db.Column(db.Integer, nullable=False)
    opponent_turret_plates_taken = db.Column(db.Integer, nullable=False)
    opponent_damage_to_champs_at_14 = db.Column(db.Integer, nullable=False)
    opponent_lvl = db.Column(db.Integer, nullable=False)
    opponent_damage_to_buildings = db.Column(db.Integer, nullable=False)
    opponent_gold_per_minute = db.Column(db.Integer, nullable=False)
    opponent_damage_per_minute = db.Column(db.Integer, nullable=False)
    opponent_total_damage_to_champs = db.Column(db.Integer, nullable=False)
    opponent_vision_score = db.Column(db.Integer, nullable=False)
    opponent_wards_placed = db.Column(db.Integer, nullable=False)
    opponent_control_wards_placed = db.Column(db.Integer, nullable=False)
    opponent_kill_participation = db.Column(db.Float, nullable=False)
    opponent_team_damage_percentage = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "accountName": self.account_name,
            "role": self.role,
            "queue": self.queue,
            "champion": self.champion,
            "kills": self.kills,
            "deaths": self.deaths,
            "assists": self.assists,
            "win": self.win,
            "turretPlatesTaken": self.turret_plates_taken,
            "damageToChampsAt14": self.damage_to_champs_at_14,
            "champLevel": self.lvl,
            "damageToBuildings": self.damage_to_buildings,
            "goldPerMinute": self.gold_per_minute,
            "damagePerMinute": self.damage_per_minute,
            "totalDamageToChamps": self.total_damage_to_champs,
            "visionScore": self.vision_score,
            "wardsPlaced": self.wards_placed,
            "controlWardsPlaced": self.control_wards_placed,
            "killParticipation": self.kill_participation,
            "teamDamagePercentage": self.team_damage_percentage,
            "csDiffAt14": self.cs_diff_at_14,
            "goldDiffAt14": self.gold_diff_at_14,
            "xpDiffAt14": self.xp_diff_at_14,
            "goldDiff": self.gold_diff,
            "xpDiff": self.xp_diff,
            "opponentChampion": self.opponent_champion,
            "opponentChampLevel": self.opponent_lvl,
            "opponentKills": self.opponent_kills,
            "opponentDeaths": self.opponent_deaths,
            "opponentAssists": self.opponent_assists,
            "opponentTurretPlatesTaken": self.opponent_turret_plates_taken,
            "opponentDamageToChampsAt14": self.opponent_damage_to_champs_at_14,
            "opponentChampLevel": self.opponent_lvl,
            "opponentDamageToBuildings": self.opponent_damage_to_buildings,
            "opponentGoldPerMinute": self.opponent_gold_per_minute,
            "opponentDamagePerMinute": self.opponent_damage_per_minute,
            "opponentTotalDamageToChamps": self.opponent_total_damage_to_champs,
            "opponentVisionScore": self.opponent_vision_score,
            "opponentWardsPlaced": self.opponent_wards_placed,
            "opponentControlWardsPlaced": self.opponent_control_wards_placed,
            "opponentKillParticipation": self.opponent_kill_participation,
            "opponentTeamDamagePercentage": self.opponent_team_damage_percentage,
        }