from result_calculation import result

def test_result():
    assert result(35) == "Pass"
    assert result(70) == "Pass"
    assert result(85) == "Pass"
    assert result(100) == "Pass"


def test_result_fail():
    assert result(5) == "Fail"