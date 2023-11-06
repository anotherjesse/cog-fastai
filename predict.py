# Prediction interface for Cog ⚙️
# https://github.com/replicate/cog/blob/main/docs/python.md

from cog import BasePredictor
import pkg_resources
import json


class Predictor(BasePredictor):
    def predict(self) -> str:
        """Run a single prediction on the model"""
        installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
        return json.dumps(installed_packages, indent=2)

