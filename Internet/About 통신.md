# "통신" 이란

음... 우선 주제가 무척 간단명료한 느낌이 난다.

사실 이전까지 통신이 무엇일까 생각을 해보면 무척 단순하다.

"어떤 얘기/정보를 주고 받는 것"이라고 생각하고 끝이었던 깊게 생각해보지 않은 주제이다.



아마 다들 알다시피 간단해보이는 단어를 깊게 파보는 순간,

그 선택을 후회하는 경우가 많다.

"**통신**" 또한 위 경우에 해당하는 것을 알고있다.

사실 전공을 통해 배운 부분도 없을 뿐더러

지금까지 공부하면서도 크게 알아보려 하지 않았던 것 같다.



그러던 와중,

Django를 공부할 때, ***<u>GET / POST</u>***를 통한 통신을 구현할 때,

물론 코드를 작성하고 의도에 따라 구현이 되는 것이 기쁘고 신기했지만

너무 겉핧기같다는 생각이 금새 들었다.



*"통신이 이렇게 저렇게 되어 내 눈 앞에 이렇게 나타나는 구나! "* 가 아닌

*<u>"이렇게 코드를 짜면 이렇게 나타나는 구나! "</u>*로 이해를 한 것 같아

어딘가 찝찝했다.



그렇게 GET은 무엇이며 POST는 또 무엇일까? 가볍게 알아볼까 라는 마음가짐으로

검색을 나섰는데

아뿔사, 이해할 수 있는 단어와 구조가 아니였다.

파면 팔수록 모르는 것 투성이.....

*"Django로 웹페이지를 만들면 무얼하나..왜, 어떻게 되는지도 모르는데.."* 라는 생각과 

답답한 마음뿐이였다.



이건 나 스스로도 통신에 'ㅌ'자도 모르면서

웹페이지를 만드는 건 너무나도 부끄럽고 당당하지 못할 것 같아

완벽하고 자세하진 않더라도

알아볼 수 있는데까지 처음부터 천천히 이해하면서 배워가고 싶어 

이렇게 정리글을 쓰면서 통신에 대해 알아가는 첫 걸음을 떼려한다.



> 구글링을 통해 다양한 사이트를 참고하면서 공부해볼 예정이고
>
> 주로 **위키백과 [국문/영문]** 와 **정보통신기술용어해설** 을 사용한다.



서론이 너무 길었다.

바로 시작!

---



## ※ 통신 : Communication

커뮤니케이션....

참 여러가지 방면에서 설명할 수 있는 주제인 것 같다.

이 글에선 〔컴퓨터 통신 및 네트워킹〕 면에서의 통신을 다뤄보겠다.



한 마디로 우선 정리하자면

**"송수신 간에 약속된 수단 및 절차에 따라 채널을 통해 정보를 주고 받는 것"** 이다.

이 간단하지만 의미가 깊은 과정을 이해하기 위해서는

위에서 언급했듯이 

다양한 수단과 절차, 채널, 그리고 주고받는 방법 및 규칙들을 알아야 한다.

각 각 자세한 요소들은 추후에 알아보도록 하고

우선 거시적으로 통신과 직접적인 관련 요소들만 짧게 알아보자.





### 1. 통신 이론 (Communication Theory)

위를 살펴보면 **채널**을 통해 정보를 주고 받는다고 나와 있다.

이 통신이론은

<u>"통신 채널 양 단간에 **오류없는** **신뢰적**이고 **효율적**인 정보 신호 전송"</u> 에 관련되는 기술 이론들이다.



#### **변조 [Modulation]** 이론

- 보통 흔히 알고있고 크게 나뉘고 있는 것이 **아날로그 방식** 과 **디지털 방식** 이다.

- **아날로그 통신/변조 (Analog Communication/Modulation) 방식**

  : 아날로그 신호에 의해 반송파의 파라미터 (진폭, 주파수, 위상) 을 변화시켜 전송된다.

  (<span style ="font-size:14px">주파수는 진폭과 수직적인 **진동 횟수**라고 보면 된다._파라미터들의 값에 따라 각기 다른 정보가 담긴다고 생각하면 쉽다.</span>)

  

  ◎ **구분**

   - **선형성**

      - **선형**(Linear) - **진폭변조** (AM)

        : 전송되는 신호(반송파)가 정보 신호에 따라 선형적으로 변화되는 변조 방식

        주파수 효율성이 좋아서, <u>*대역제한된 채널*</u> 에서도 사용 용이

        

        정보신호&반송파신호 주파수 이외에 새로운 주파수는 발생하지 않고

        대역폭의 2배를 넘지 않으며

        스펙트럼 형태도 바뀌지 않는다.

        SNR 관련 문제 발생은 전송 전력을 늘리는 것만으로 해결 가능하다. 

        (전력 ▲ = 신호 복원/복조 용이 = 통신 품질▲)

        

        <span style ="font-size:14px">*＊**SNR** (신호대잡음비) : 수신측에 도착한 일정 신호에서 나타난 **신호전력** 대 **잡음전력** 간의 **비율*** → <u>"잡음이 신호에 대해 끼친 영향을 정량적으로 나타낸 것"</u></span>

        

      - **비선형** - **각 변조** (FM , PM)

        <span style ="font-size:14px">*＊비선형 변조 (Nonlinear) = 각 변조  (Angle) = 지수 (Exponential) 변조*</span>

        제곱법칙처럼 비선형적인 형태의 변조이며

        **각(Angle)** 성분에 정보를 실어보내는 변조 방식이다.

        중첩이나 새로운 주파수 발생, SNR 부분에서 선형 변조방식과 차이점이 있다.

        <span style ="font-size:14px">(중첩 원리 X / 더 넓은 대역폭 필요 / 잡음에 강함 /새로운 주파수 성분 가질 수 있음.)</span>

  

  

   - **변조 대상 파라미터 _ *진폭 / 주파수 / 위상***

      - **진폭** : **AM** (Amplitude Modulation)

      - **주파수** : **FM** (Frequency Modulation)

      - **위상** : **PM** (Phase Modulation)

      - **진폭 & 위상** : **QAM** (Quadrature Amplitude Modulation_직교 진폭 변조)

        : 제한된 주파수 대역에서도 전송효율 ▲

        <span style ="font-size:14px">(직교위상변조 방식의 일종 _ 디지털에도 위와 같은 방식의 변조 有 _ASK & PSK)</span>

  

  <span style ="font-size:14px">*＊**아날로그** 신호(Analog Signal) : 시간 및 진폭 값 모<u>든 부분에서 연속적</u>인 신호*</span>

  <span style ="font-size:14px">*＊연속시간 신호(Continous-time Signal) : 시간에서만 연속적인 신호* → <u>때론 이산적 값도 허용</u>하는 차이점</span>

  <span style ="font-size:14px">*＊이산시간 신호(Discrete-time Signal) : 시간에서만 이산적인 신호* → <u>이산시간마다 연속적&이산적 값</u> 가지는 특징</span>

  <span style ="font-size:14px">*＊샘플 신호(Sampled-data Signal) : <u>이산시간마다 연속 값(진폭)</u> 갖는 신호* </span>

  <span style ="font-size:14px">*＊**디지털** 신호(Digital Signal) : 시간 및 진폭 값 <u>모든 부분에서 이산적</u>인 신호* → 각 이산적 값 사이에는 값이 없다</span>

  

  <span style ="font-size:14px">*＊반송파(Carrier) : 정보가 포함되는 높은 주파수의 파형 _ 통상적으로 반송파의 주파수는 <u>원래의 정보 신호보다 훨씬 높은 주파수</u>를 사용한다.*</span>





- **디지털 통신/변조 (Digital Communication/Modulation) 방식**

진폭 & 위상 : **QAM** (Quadrature Amplitude Modulation_직교 진폭 변조)

: **ASK**(진폭편이변조) **+ PSK**(위상편이변조) _ 과거, 기존 아날로그 전화 회선으로 디지털 전송할 때, 고속 변조기로 사용 됨 

#### **샘플링** 이론





#### **정보** 이론





#### **동기화**







### 2. 통신 요소 (Elements)

### 3. 통신 시스템

### 4. 통신 매체 (Medium)
이 매체 Medium이란 단어는
필자 또한 이번에 공부하며 알게된 영단어인데 매체라는 의미를 가진다.
향후 **MAC** / **매체 접근 제어**를 알아볼 때도 발견할 수 있다...
어쨋든
통신을 위한 매체라는 뜻이고

### 5. 통신 채널 (Channel)

### 6. 통신 회선 (Line)

### 7. 통신 망 (Networks)

### 8. 통신 계층 (Layer)
신뢰성 있는 통신을 위해서는 엄격한 단계적 과정과 절차가 필요한 것을 다들 알 것이다.
이 단계를 범위,요소,장치 등 다양한 기준을 기반으로 단계적 통신을 계층으로 나누어 설명한다.
ISO에서 지정한 표준 모델(OSI 7계층 모델) , 실질적인 인터넷 통신을 나타낸 모델(TCP/IP Protocol Suite) , APPLE 사에서 제안한 모델 등
다양한 계층 기반 모델들이 존재한다.

#### ++ 무선 통신 (Wireless Communication _ RF Communication)

#### ++ 이동 통신 (Mobile Telecommunication)
흔히 알고 있는 회사들..
○○텔레콤, XX 텔레콤이라는 이름의 기원이다. 'Telecommunication'
이동 통신은 **세대**를 기준으로 나눌 수 있다.