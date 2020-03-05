from lambda_deployment_test_utils.pre_post_test_utils import lambda_test, fn_assert


@lambda_test("pre")
def pre_traffic_test_1(fn):
    event = {"Name": "PreTrafficLambda"}
    expected = {"HelloMessage": "Hello PreTrafficLambda, this a response from Lambda!!"}
    actual_result = fn(event)
    fn_assert(
        actual_result == expected,
        "Check test: Actual result did not match expected test result",
    )


@lambda_test("pre")
def pre_traffic_test_2(fn):
    event = {"Name": "PreTrafficLambda2"}
    expected = {"HelloMessage": "Hello PreTrafficLambda2, this a response from Lambda!!"}
    actual_result = fn(event)
    fn_assert(
        actual_result == expected,
        "Check test: Actual result did not match expected test result",
    )
