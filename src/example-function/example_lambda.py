import logging
import os
from aws_xray_sdk.core import xray_recorder  # noqa: F401
from aws_xray_sdk.core import patch_all

patch_all()

# logging
LOG_LEVEL = os.environ.get("LOG_LEVEL", logging.INFO)
root_logger = logging.getLogger()
root_logger.setLevel(LOG_LEVEL)
log = logging.getLogger(__name__)


def handler(event, context):
    log.debug("Received event {}".format(event))
    name = event["Name"]
    return {"HelloMessage": f"Hello {name}, this a response from Lambda!!"}
