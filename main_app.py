from fastapi_simple_security import api_key_security, api_key_router
from seeds_classifier.seed_classifier import SeedClassifier
from fastapi import FastAPI, status, Depends
from features import Features
from setup_logging import setup_logger
import numpy as np
import uvicorn


logger = setup_logger()
app = FastAPI()
app.include_router(api_key_router, prefix="/auth", tags=["_auth"])
clf = SeedClassifier()


@app.get("/", status_code=status.HTTP_200_OK)
def get_root():
    logger.info("Accessing the root of the api")
    return "Welcome to the root"


@app.get("/health", status_code=status.HTTP_200_OK)
def get_health():
    logger.info("Health check")
    return "Ok"


@app.get(
    "/secure", dependencies=[Depends(api_key_security)], status_code=status.HTTP_200_OK
)
def get_secure_access():
    return "Welcome to the secure area, if now have access to the secure area"


@app.post(
    "/classify",
    dependencies=[Depends(api_key_security)],
    status_code=status.HTTP_200_OK,
)
def get_class(features: Features):
    x_feat = np.array(
        [
            features.area,
            features.perimeter,
            features.compactness,
            features.length,
            features.width,
            features.asymmetry,
            features.kernel_length,
        ]
    ).reshape(1, -1)
    logger.info("x features {}".format(x_feat))
    logger.info("class of {}".format(str(clf.classify(x_feat))))
    return str(clf.classify(x_feat))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
