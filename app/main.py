from care_rules import (classify_sunlight, generate_care_tip, is_soil_dry, needs_watering, recommended_soil_type)

def run_demo()->None:
    moisture = 20
    plant_type = "Chili"
    sunlight_hours = 2

    dry = is_soil_dry(moisture)
    water = needs_watering(moisture, plant_type=plant_type)

    sunlight = classify_sunlight(sunlight_hours)

    soil_tip = recommended_soil_type(plant_type)
    care_tip = generate_care_tip(needs_water=water, sunlight_level=sunlight)

    print(f"Plant Type: {plant_type}")
    print(f"Moisture: {moisture}%")
    print(f"Sunlight: {sunlight_hours} hours ({sunlight})")
    print(f"Soil Dry: {dry}")
    print(f"Watering Needed: {water}")
    print(f"Soil Tip: {soil_tip}")
    print(f"Care Tip: {care_tip}")


if __name__ == "__main__":
    run_demo()
