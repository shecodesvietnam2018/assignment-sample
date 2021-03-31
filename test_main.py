import main


def test_program(capfd):
    main.input = lambda: "3"
    out, err = capfd.readouterr()
    return out == "Odd"
