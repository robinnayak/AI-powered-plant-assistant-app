from enum import Enum
from typing import Final, Dict


class PlantType(Enum):
    TOMATO = "tomato"
    CACTUS = "cactus"
    MINT = "mint"
    ROSE = "rose"
    BASIL = "basil"
    CHILI = "chili"
    DEFAULT = 'default'


class SunlightLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


DEFAULT_MOISTURE_THRESHOLD: Final[float] = 40.0


PLANT_MOISTURE_THRESHOLD: Final[Dict[str, float]] = {
    PlantType.TOMATO.value: 45.0,
    PlantType.CACTUS.value: 20.0,
    PlantType.MINT.value: 55.0,
    PlantType.ROSE.value: 40.0,
    PlantType.BASIL.value: 50.0,
    PlantType.CHILI.value: 45.0,
    PlantType.DEFAULT.value: 40.0,
}

SOIL_RECOMMENDATIONS: Final[Dict[PlantType, str]] = {
    PlantType.TOMATO.value: "Use well-draining loamy soil rich in organic matter.",
    PlantType.CACTUS.value: "Use sandy, fast-draining soil to avoid root rot.",
    PlantType.MINT.value: "Use moist, fertile soil with good drainage.",
    PlantType.ROSE.value: "Use loamy, slightly acidic, well-draining soil.",
    PlantType.BASIL.value: "Use light, nutrient-rich, well-draining soil.",
    PlantType.CHILI.value: "Use well-draining, fertile soil rich in organic matter.",
    PlantType.DEFAULT.value: "Use well-draining soil.",
}

CARE_TIPS: Final[Dict[str, str]] = {
    "water_needed": "Water your plant regularly to keep the soil moist.",
    "no_water_needed": "Your plant has enough water. Avoid overwatering.",
    "low_sunlight": "This plant needs low sunlight. Place it in a shaded area.",
    "medium_sunlight": "This plant needs medium sunlight. Place it in a partially shaded area.",
    "high_sunlight": "This plant needs high sunlight. Place it in a sunny area.",
}

SUNLIGHT_LOW_MAX: Final[float] = 3.0
SUNLIGHT_MEDIUM_MAX: Final[float] = 6.0


