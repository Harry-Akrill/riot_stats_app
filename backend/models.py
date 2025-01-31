from config import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    queue = db.Column(db.String(80), nullable=False)
    champion = db.Column(db.String(80), unique=False, nullable=False)
    opponent_champion = db.Column(db.String(80), unique=False, nullable=False)
    kills = db.Column(db.Integer, nullable=False)
    deaths = db.Column(db.Integer, nullable=False)
    assists = db.Column(db.Integer, nullable=False)
    lvl = db.Column(db.Integer, nullable=False)
    opponent_lvl = db.Column(db.Integer, nullable=False)
    win = db.Column(db.Integer, nullable=False)
    vision_score = db.Column(db.Integer, nullable=False)
    control_wards_placed = db.Column(db.Integer, nullable=False)
    wards_placed = db.Column(db.Integer, nullable=False)
    kill_participation = db.Column(db.Float, nullable=False)
    cs_diff_at_14 = db.Column(db.Integer, nullable=False)
    turret_plates_taken = db.Column(db.Integer, nullable=False)
    gold_diff_at_14 = db.Column(db.Integer, nullable=False)
    xp_diff_at_14 = db.Column(db.Integer, nullable=False)
    damage_to_champs_at_14 = db.Column(db.Integer, nullable=False)
    total_damage_to_champs = db.Column(db.Integer, nullable=False)
    team_damage_percentage = db.Column(db.Float, nullable=False)
    xp_diff = db.Column(db.Integer, nullable=False)
    gold_diff = db.Column(db.Integer, nullable=False)
    gold_per_minute = db.Column(db.Integer, nullable=False)
    damage_per_minute = db.Column(db.Integer, nullable=False)
    damage_to_buildings = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "accountName": self.account_name,
            "role": self.role,
            "queue": self.queue,
            "champion": self.champion,
            "opponentChampion": self.opponent_champion,
            "kills": self.kills,
            "deaths": self.deaths,
            "assists": self.assists,
            "champLevel": self.lvl,
            "opponentChampLevel": self.opponent_lvl,
            "win": self.win,
            "visionScore": self.vision_score,
            "controlWardsPlaced": self.control_wards_placed,
            "wardsPlaced": self.wards_placed,
            "killParticipation": self.kill_participation,
            "csDiffAt14": self.cs_diff_at_14,
            "turretPlatesTaken": self.turret_plates_taken,
            "goldDiffAt14": self.gold_diff_at_14,
            "xpDiffAt14": self.xp_diff_at_14,
            "damageToChampsAt14": self.damage_to_champs_at_14,
            "totalDamageToChamps": self.total_damage_to_champs,
            "teamDamagePercentage": self.team_damage_percentage,
            "xpDiff": self.xp_diff,
            "goldDiff": self.gold_diff,
            "goldPerMinute": self.gold_per_minute,
            "damagePerMinute": self.damage_per_minute,
            "damageToBuildings": self.damage_to_buildings,
        }