def test_initial_universe(snap_compare):
    assert snap_compare("../src/game_app/game_app.py")


def test_n_key_should_produce_next_generation(snap_compare):
    assert snap_compare("../src/game_app/game_app.py", press=["n"])


def test_r_key_should_reset_to_seed(snap_compare):
    assert snap_compare("../src/game_app/game_app.py", press=["n", "r"])
