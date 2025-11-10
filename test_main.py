from main import main


def test_main_output(capfd):
    main()
    out, _ = capfd.readouterr()
    assert "Hello, TeamCity!" in out