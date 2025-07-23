#!/bin/bash

set -e  # 에러 발생 시 즉시 종료
# set -x  # 실행되는 명령어 출력

# 현재 디렉터리 기준으로 하위의 모든 .deb 파일 찾기
find . -type f -name "*.deb" | while read -r debfile; do
    echo "------------------- Installing $debfile -------------------"
    apt-get install --yes --no-install-recommends -f "./$debfile"
    printf "\n"
done