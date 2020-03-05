from lambda_deployment_test_utils.pre_post_test_utils import handler_factory


handler = handler_factory(
    test_group="pre", modules=["test.integration.pre_traffic_test_data"]
)
