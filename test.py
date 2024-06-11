from sender_stand_request import create_order_and_get_track, get_order_by_track
# Лера Абрамс, 16-я когорта — Финальный проект. Инженер по тестированию плюс


def test_order_creation_and_retrieval():
    track_number = create_order_and_get_track()
    response = get_order_by_track(track_number)
    assert response.status_code == 200






