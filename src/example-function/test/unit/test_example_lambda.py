import pytest
from example_lambda import handler


@pytest.fixture()
def test_event():
    return {
        'Name': "test input"
    }


def test_lambda_handler(test_event):
    response = handler(test_event, None)
    assert {"HelloMessage": f"Hello {response}, this a response from Lambda!!"}
