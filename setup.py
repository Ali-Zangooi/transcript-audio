import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.0'
PACKAGE_NAME = 'AudioTranscript'
AUTHOR = 'Ali Zangooi'
AUTHOR_EMAIL = 'seagu.ll@yahoo.com'
URL = 'https://github.com/Ali-Zangooi/transcript-audio/tree/main'

LICENSE = 'GNU general public license version 3'
DESCRIPTION = 'Audio file transcription'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'speech_recognition',
      'scipy'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
