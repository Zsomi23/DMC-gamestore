import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG)

__verson__ = '0.1.0'

def main():
    logger.info('Starting GameStore %s', __verson__)

if __name__ == "__main__":
    main()