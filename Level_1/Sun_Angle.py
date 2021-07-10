from typing import Union
from datetime import timedelta, datetime


def sun_angle(time_srs: str) -> Union[int, str]:
    SUN_UP_TIME = datetime.strptime("06:00", "%H:%M")
    SUN_DOWN_TIME = datetime.strptime("18:00", "%H:%M")

    cur_time = datetime.strptime(time_srs, "%H:%M")

    if cur_time < SUN_UP_TIME or cur_time > SUN_DOWN_TIME:
        return "I don't see the sun!"
    resolution = 180 / (
        (SUN_DOWN_TIME - SUN_UP_TIME).seconds / 60
    )  # Resolution : Degree per minutes

    return round(((cur_time - SUN_UP_TIME).seconds / 60) * resolution, 2)


if __name__ == "__main__":
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
