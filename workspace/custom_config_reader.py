from typing import Dict, Set

# 구매한 종목셋
PURCHASED_STOCK: Set[str] = set()

# 포착한 종목셋
# CAPTURED_STOCK: Dict[str, int] = dict()
CAPTURED_STOCK: Set[str] = set()

# 구매할 종목의 개수
TARGET_PURCHASE_STOCK_NUM = 3

# 시가총액 (억 ₩) 최대 조건
MAX_MARKET_CAP = 5_000

# 현재가 (₩) 최소 조건
MIN_STCK_PRPR_COND = 1_000

# 현재가 (₩) 최대 조건
MAX_STCK_PRPR_COND = 25_000

# 전전일 기준가 대비 전일가 비율 (%) 최대 조건
MAX_PRDY_1_PRRT_COND = 20

# 기준가 대비 현재가 비율 (%) 최소 조건
MIN_PRDY_CTRT_COND = 3

# 기준가 대비 현재가 비율 (%) 최대 조건
MAX_PRDY_CTRT_COND = 15

# 최고가 대비 현재가 비율 (%) 차이 최대 조건
MAX_HGPR_VRSS_PRPR_RATE_DIFF_COND = -2

# 누적 거래대금 (₩) 최소 조건
MIN_ACML_TR_PBMN_COND = 3_000_000_000

# 누적 거래량 (주) 최소 조건
MIN_ACML_VOL_COND = 200_000

# 거래대금 변화액 (₩) 차이 최소 조건
MIN_ACML_TR_PBMN_DIFF_COND = 100_000_000

# 구매 제한 기준가 대비 시가 비율 (%) 최소 조건
PURCH_LIM_MIN_PRDY_CLPR_VRSS_OPRC_RATE_COND = -2

# 구매 제한 기준가 대비 시가 비율 (%) 최대 조건
PURCH_LIM_MAX_PRDY_CLPR_VRSS_OPRC_RATE_COND = 8

# 구매 제한 시가 대비 현재가 비율 (%) 차이 최대 조건
PURCH_LIM_MAX_OPRC_VRSS_PRPR_RATE_DIFF_COND = 7

# 구매 제한 누적 거래대금 (억 ₩) 최대 조건
PURCH_LIM_MAX_ACML_TR_PBMN_COND = 120

# 구매 제한 누적 거래량 (만 주) 최대 조건
PURCH_LIM_MAX_ACML_VOL_COND = 150


def enable_debug_mode() -> None:
    print("디버깅 모드 활성화\n")

    global \
        TARGET_PURCHASE_STOCK_NUM, \
        MAX_MARKET_CAP, \
        MIN_PRDY_CTRT_COND, \
        MAX_PRDY_CTRT_COND, \
        MAX_HGPR_VRSS_PRPR_RATE_DIFF_COND, \
        MIN_ACML_TR_PBMN_DIFF_COND, \
        PURCH_LIM_MIN_PRDY_CLPR_VRSS_OPRC_RATE_COND, \
        PURCH_LIM_MAX_OPRC_VRSS_PRPR_RATE_DIFF_COND, \
        PURCH_LIM_MAX_ACML_TR_PBMN_COND, \
        PURCH_LIM_MAX_ACML_VOL_COND

    # 시가총액 (억 ₩) 최대 조건
    MAX_MARKET_CAP = 6_000

    # 기준가 대비 현재가 비율 (%) 최소 조건
    MIN_PRDY_CTRT_COND = -15

    # 기준가 대비 현재가 비율 (%) 최대 조건
    MAX_PRDY_CTRT_COND = 30

    # 최고가 대비 현재가 비율 (%) 차이 최대 조건
    MAX_HGPR_VRSS_PRPR_RATE_DIFF_COND = -30

    # 거래대금 변화액 (₩) 차이 최소 조건
    MIN_ACML_TR_PBMN_DIFF_COND = 0

    # 구매 제한 기준가 대비 시가 비율 (%) 최소 조건
    PURCH_LIM_MIN_PRDY_CLPR_VRSS_OPRC_RATE_COND = -30

    # 구매 제한 시가 대비 현재가 비율 (%) 차이 최대 조건
    PURCH_LIM_MAX_OPRC_VRSS_PRPR_RATE_DIFF_COND = 30

    # 구매 제한 누적 거래대금 (억 ₩) 최대 조건
    PURCH_LIM_MAX_ACML_TR_PBMN_COND = 10_000

    # 구매 제한 누적 거래량 (주) 최대 조건
    PURCH_LIM_MAX_ACML_VOL_COND = 10_000
