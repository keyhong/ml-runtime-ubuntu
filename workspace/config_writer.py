from pathlib import Path
from typing import Dict, Union


def write_yaml_config(yaml, new_config_dict: Dict[str, Union[str, int]]) -> None:
    """config.yaml 작성 함수"""

    with open(
        file=Path(__file__).resolve().parents[0] / "config.yaml",
        mode="w",
        encoding="utf-8",
    ) as f:
        # for key, value in new_config_dict.items():
        #     _cfg[key] = value

        yaml.dump(new_config_dict, f)
