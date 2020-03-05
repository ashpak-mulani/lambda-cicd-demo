from lambda_deployment_test_utils.pre_post_test_utils import handler_factory

handler = handler_factory(
    test_group="post", modules=["test.integration.post_traffic_test_data"]
)
