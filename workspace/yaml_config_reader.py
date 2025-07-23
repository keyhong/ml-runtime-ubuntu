"""Configuration"""

from datetime import datetime
from pathlib import Path

from ruamel.yaml import YAML

from wealth.config.config_writer import write_yaml_config

yaml = YAML()
yaml.preserve_quotes = True  # 따옴표 유지

# 개인정보 파일 가져오기
with open(
    file=Path(__file__).resolve().parents[0] / "config.yaml",
    mode="r",
    encoding="utf-8",
) as f:
    _cfg = yaml.load(f)

    # 접근토큰 발급 (없다면 실행 후 프롬프트 결과를 config.yaml 파일에 넣어줄 것)
    # if datetime.now() > datetime.strptime(ACCESS_TOKEN_EXPIRED, "%Y-%m-%d %H:%M:%S"):
    if True:
        ACCESS_TOKEN, ACCESS_TOKEN_EXPIRED = get_new_koreaninvestment_access_token(BASE_URL, APP_KEY, APP_SECRET)

        _cfg["ACCESS_TOKEN"] = ACCESS_TOKEN
        _cfg["ACCESS_TOKEN_EXPIRED"] = ACCESS_TOKEN_EXPIRED

