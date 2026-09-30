import sender_stand_request


def positive_assert():
    
    track = sender_stand_request.get_new_order_track()

    response = sender_stand_request.get_order_by_track(track)

    assert response.status_code == 200


def test_get_order_by_track():
    positive_assert()