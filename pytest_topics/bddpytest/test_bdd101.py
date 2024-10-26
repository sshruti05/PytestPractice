from pytest_bdd import scenario, scenarios, given, when, then

from pathlib import Path
featureFileDir = 'myfeatures'
featureFile = 'first101.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)