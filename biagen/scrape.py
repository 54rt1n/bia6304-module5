# biagen/scrape.py

import logging
import trafilatura
from trafilatura.settings import use_config
import trafilatura.settings

logger = logging.getLogger(__name__)

def fetch_url(url: str, bare: bool = False, **kwargs) -> str:
    """Fetch a url and return the extracted text"""
    try:
        logger.debug(f"Fetching url: {url}")

        config = trafilatura.settings.DEFAULT_CONFIG

        use_config(config=config)

        downloaded = trafilatura.fetch_url(url)

        if downloaded is None:
            raise ValueError(f"Failed to download content from {url}")

        if bare:
            extracted = trafilatura.html2txt(downloaded)
        else:
            extracted = trafilatura.extract(downloaded, favor_recall=True)

        if extracted is None:
            raise ValueError(f"Failed to extract text from {url}")

        logger.info(f"Fetched {len(extracted)} bytes from {url}")
        logger.debug(extracted)

        return extracted

    except Exception as e:
        logger.error(f"Error while fetching and extracting content from {url}: {str(e)}")
        raise
