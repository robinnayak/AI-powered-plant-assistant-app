import pytest

from app.care_rules import (
    classify_sunlight,
    generate_care_tip,
    is_soil_dry,
    needs_watering,
    recommended_soil_type,
)


def test_is_soil_dry_true():
    assert is_soil_dry(20, dry_threshold=30) is True


def test_is_soil_dry_false():
    assert is_soil_dry(40, dry_threshold=30) is False


def test_needs_watering_known_plant():
    assert needs_watering(30, "tomato") is True


def test_needs_watering_unknown_plant_uses_default():
    assert needs_watering(35, "unknown_plant") is True


def test_classify_sunlight_levels():
    assert classify_sunlight(2) == "low"
    assert classify_sunlight(4) == "medium"
    assert classify_sunlight(8) == "high"


def test_recommended_soil_type_unknown():
    msg = recommended_soil_type("unknown")
    assert "Use well-draining soil." in msg


def test_generate_care_tip_valid():
    tip = generate_care_tip(True, "medium")
    assert "Water your plant regularly to keep the soil moist." in tip


def test_generate_care_tip_invalid_sunlight():
    with pytest.raises(ValueError):
        generate_care_tip(True, "very_high")