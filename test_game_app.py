def test_game_app(snap_compare):
    assert snap_compare('game_app.py')

def test_n_key_should_produce_next_generation(snap_compare):
    assert snap_compare("game_app.py", press=["n"])

