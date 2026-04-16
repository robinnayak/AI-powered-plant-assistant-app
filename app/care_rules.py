"""
care_rules.py

Day 2 reference module for clean function design.
This module contains small, focused functions for plant-care decisions.
"""

from typing import Dict
from config import PlantType, SunlightLevel, DEFAULT_MOISTURE_THRESHOLD, PLANT_MOISTURE_THRESHOLD, SOIL_RECOMMENDATIONS, CARE_TIPS, SUNLIGHT_LOW_MAX, SUNLIGHT_MEDIUM_MAX





def _validate_moisture(moisture:float)->float:
    if not isinstance(moisture, (int, float)):
        raise TypeError("Moisture must be a number (int, float).")
    
    if moisture < 0 or moisture > 100:
        raise ValueError("Moisture must be between 0 and 100.")

    return float(moisture)


def _normalize_plan_type(plant_type:str)-> str:
    if not isinstance(plant_type, str):
        raise TypeError("Plant type must be a string.")
    normalized =  plant_type.lower().strip()

    if not normalized:
        raise ValueError("plant_type cannot be empty.")
    
    return normalized


#core functions 

def is_soil_dry(moisture: float, dry_threshold: int = 35)-> bool:

    value = _validate_moisture(moisture)
    return value < dry_threshold


def needs_watering(moisture: float, plant_type: str) -> bool:
    value = _validate_moisture(moisture)
    plant = _normalize_plan_type(plant_type)

    threshold = PLANT_MOISTURE_THRESHOLD.get(plant, DEFAULT_MOISTURE_THRESHOLD)
    return value < threshold


def classify_sunlight(hours: float) -> str:
    if not isinstance(hours, (int, float)):
        raise TypeError("Hours must be a number (int, float).")
    
    if hours < 0 or hours > 24:
        raise ValueError("Hours must be between 0 and 24.")

    if hours < SUNLIGHT_LOW_MAX:
        return SunlightLevel.LOW.value
    elif hours < SUNLIGHT_MEDIUM_MAX:
        return SunlightLevel.MEDIUM.value
    else:
        return SunlightLevel.HIGH.value


def recommended_soil_type(plant_type:str) -> str:

    plant = _normalize_plan_type(plant_type)

    return SOIL_RECOMMENDATIONS.get(plant, SOIL_RECOMMENDATIONS[PlantType.DEFAULT.value])


def generate_care_tip(needs_water: bool = False, sunlight_level:str = "medium")-> str:
    
    sunlight = sunlight_level.lower().strip()

    if sunlight not in ["low", "medium", "high"]:
        raise ValueError("Sunlight level must be 'low', 'medium', or 'high'.")

    water_tip = CARE_TIPS["water_needed"] if needs_water else CARE_TIPS["no_water_needed"]
    sunlight_tip = CARE_TIPS[f"{sunlight}_sunlight"]

    return f"{water_tip} {sunlight_tip}"


if __name__ == "__main__":
    # soil = is_soil_dry(moisture=56)
    # print("Dry Soil: ", soil)
    needs_water = needs_watering(moisture=10, plant_type="cactus")
    # print("Watering needed: ", needs_water)
    if needs_water:
        print("Watering needed")
    else:
        print("Watering not needed")
    tip = generate_care_tip(needs_water, sunlight_level="high")
    print(tip)
