# Space Mission Core
우주 비행체 관제 소프트웨어인 SMC는 ESP32와 라즈베리파이가 탑재 된 큐브 위성의 간단한 통신 상태를 실험하기 위한 소프트웨어 입니다. 이 저장소는 앞서 설명한 SMC의 c파일을 내포하고 있으며 지상국 시스템(GSC), 위성 시스템(SSC) 등의 임무를 수행할 수 있습니다.

## 개발 팀원 소개
| 류용헌 |
|:------:|
| <img src="https://github.com/MiruHeon/Normal-Project/blob/main/193119713.jpeg?raw=true" alt="류용헌" width="150"> |
| PL |

# 실행 방법

## 리눅스 환경
```cd build``` &&
```cmake ..``` &&
```cmake --build .``` &&
```./server_linux```
## 윈도우 환경
1. **Visual Studio** 또는 **MinGW** 등 C 컴파일러가 설치된 환경에서 `CMakeLists.txt`를 통해 프로젝트를 엽니다.
2. `server_win` 타겟을 빌드하여 실행합니다.
3. 리눅스 환경(라즈베리파이 등)에서 클라이언트를 실행하여 서버와 통신을 확인합니다.

# 참고
NASA cFS 프레임워크
