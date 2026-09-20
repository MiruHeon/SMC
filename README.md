# Space Mission Core
우주 비행체 관제 소프트웨어인 SMC는 ESP32와 라즈베리파이가 탑재 된 큐브 위성의 간단한 통신 상태를 실험하기 위한 소프트웨어 입니다. 이 저장소는 앞서 설명한 SMC의 c파일을 내포하고 있으며 지상국 시스템(GSC), 위성 시스템(SSC) 등의 임무를 수행할 수 있습니다.

## What is SMC?
SMC(Space Mission Core)는 통신 데이터 중계 소프트웨어로, wifi 상에서 소켓 통신으로 서로 데이터를 주고받을 수 있게 설계되었습니다.

## Background
항공우주공학에서 배운 위성이 너무나 재밌었고, 흥미로웠기 때문에, 자연스레 "만들어보자!" 라는 생각이 들었던 것 같고, 우선 위성의 통신 시스템부터 직접 만들어 보고 싶다는 생각에 제작하게 되었습니다. 

## Overview
제작에는 Python과 C가 사용되었으며, 통신 방식은 시리얼통신(UART), 115200 bps로 단일화 했습니다.
이런 SMC는 GSC(지상국용), SSC(위성용)으로 나누어 지며, 위성용은 극한의 메모리 효율을 내야 하므로, C로 작성되었으며, 지상국용은 데이터를 쉽게 중계하기 위해, Python과 pyqt5 라이브러리를 활용하여 제작하였습니다.

<p align="center">
  <img src="https://github.com/MiruHeon/Normal-Project/blob/main/Ground%20sys.png?raw=true" alt="GSC" width="500" />
</p>
<p align="center">
  <img src="https://github.com/MiruHeon/Normal-Project/blob/main/gsc2.png?raw=true" alt="GSC2" width="500" />
</p>

## Architecture
```
데이터 전송(위성)
      ↓
데이터 확인(지상국)
      ↓
데이터 시각화(지상국)
```

## 개발 팀원 소개
| 류용헌 |
|:------:|
| <img src="https://github.com/MiruHeon/Normal-Project/blob/main/profile.png?raw=true" alt="류용헌" width="150"> |
| PL |

## 참고
NASA cFS 프레임워크
