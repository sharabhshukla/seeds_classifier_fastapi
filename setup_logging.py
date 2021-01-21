from loguru import logger
import os


def setup_logger():
    if os.environ.get("GOOGLE_COMPUTE_ENGINE"):
        import google.cloud.logging
        from google.cloud.logging.handlers import CloudLoggingHandler

        client = google.cloud.logging.Client()
        gce_handler = CloudLoggingHandler(client, name="somerandomshit")
        logger.add(gce_handler)
    return logger
