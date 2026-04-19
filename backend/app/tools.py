def get_vacation_days(user_id: str = "user_1") -> dict:
    fake_db = {
        "user_1": 14,
        "user_2": 8
    }

    return {
        "user_id": user_id,
        "remaining_days": fake_db.get(user_id, 0)
    }