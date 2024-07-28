import mpu

from uszipcode import SearchEngine

from model.league import League
from model.team import Team

MILES_PER_KM = 0.621371

def calculate_distance_between_team_and_league(team: Team, league: League):
    return _calc_distance_between_zip_codes(team.zip_code, league.zip_code)

# Returns the distance in miles
def _calc_distance_between_zip_codes(zip1: str, zip2: str) -> float:
    search = SearchEngine()

    zip1_coords = search.by_zipcode(zip1)
    zip2_coords = search.by_zipcode(zip2)

    dist_km = mpu.haversine_distance((zip1_coords.lat,zip1_coords.lng),(zip2_coords.lat,zip2_coords.lng))
    dist_miles = dist_km * MILES_PER_KM

    return dist_miles