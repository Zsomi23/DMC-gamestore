import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

from gamestore.game_router import router as gr

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

__version__ = '0.1.0'

app = FastAPI(
        title='GameStore',
        version=__version__
    )

app.include_router(gr)

@app.get('/')
def docs():
    return RedirectResponse(url='/docs')


def main():
    logger.info('Starting GameStore %s', __version__)
    uvicorn.run(app, log_config=None)


if __name__ == "__main__":
    main()