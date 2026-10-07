import logging
from pathlib import Path
from datetime import datetime

from src.constants import LOG_DIR

# Create logs directory if it doesn't exist
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Log file name with timestamp
LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
