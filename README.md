# math_sim
수학 시뮬레이션하기


<br>

만든 프로그램:<br>
수열 - 공 튕기기 시뮬레이션<br>
함수 - 삼각형 넓이 구하기,제논의 역설<br>
확률 - 몬티홀 문제, 몬티홀 문제 시뮬레이션<br>

<h2> 공 튕기기 시뮬레이션 </h2>
<p>
공이 튕겨 올라갈 때마다 공이 튀어오르는 정도에 따라 튀어오르는 높이가 감소하는 모습을 수열의 일반항으로 정리한 뒤 이를 그래프를 통해 나타내었습니다<br/>

[코드](https://github.com/WhiteHerb/math_sim/blob/802e786f3f4b370bfbadc3f624afcd0249410c00/ballsim/bounce.py)
</p>

<h2> 삼각형 넓이 구하기 </h2><br/>
<p> 
Turtle을 통해 gui를 제작하였고 사용하가 삼각형을 그린 뒤 숫자 1을 누르면 삼각형의 넓이를 구하는 프로그랩입니다 <br/>
작동 순서 :<br/>
1. Turtle의 gui를 누를떄마다 원래 위치에서 마우스가 눌린 위치까지의 각도를 구한 뒤 마우스가 눌린 위치로 이동하고 원래 점에서 지금 점까지의 길이를 구한 뒤 각도, 길이 정보를 저장합니다<br/>
2. 1번 과정을 3번 반복한 뒤 세 선중 하나의 각도와 이웃한 두 변의 길이를 통해 삼각형의 넓이를 구합니다 ( sinA * l1 * l2 / 2 )<br/>

[코드](https://github.com/WhiteHerb/math_sim/blob/802e786f3f4b370bfbadc3f624afcd0249410c00/triangle/main.py)
</p>
<br/>

<h2>제논의 역설</h2><br/>
<p>
아킬레우스의 역설이라고도 불리는 제논의 역설은 "어떠한 물체는 절대 목표지점에 다가갈 수 없다"는 역설입니다.<br/>
거북이와 사람이 경주를한다고 가정해봅시다<br/>
거북이는 속도가 매우 느려서 사람보다 100m 앞에서 출발하는 헨드캡이 주어졌습니다.<br/>
거북이가 천천히 걸어가는 동안 사람은 거북이를 따라잡으러 뛰어갈 것입니다.<br/>
사람이 100m를 달려 거북이를 따라잡으려 했지만 그동안 거북이는 10m를 더 앞서갔습니다.<br/>
사람이 다시 10m를 달려갔지만 그 사이 거북이는 1m를 또 앞서갑니다.<br/>
사람이 또 다시 1m를 달려가면 거북이는 0.1m를 달려갑니다.<br/>
이런식으로 사람이 거북이를 절대 따라잡지 못할것처럼 보이는 이 상황이 제논의 역설입니다.<br/>
물론 우리는 이러한 상황이 말도 안되는 일이라는 것을 알지만, 이것이 틀렸음을 수학적으로 증명하는 것이 불가능하기 때문에 이를 역설이라고 부릅니다.<br/>
<br/>

이번에 만든 프로그램은 제논의 역설에서 사람이 뛰어가는 거리를 그래프로 나타내었습니다<br/>
[코드](https://github.com/WhiteHerb/math_sim/blob/5607e0abbdc564e1748de7191b10bb19c4ed3520/grap/zanon.py)
</p><br/>

2022/06/20 업데이트<br>
수열 - 피보나치 수열 구하기: <br>
  피보나치 수열에서 40만번째 자리의 숫자 출력/저장 <br>
  이 이상은 램 부족 리눅스에선 killed 윈도우에선 심한 렉 유발 <br>
시그마 - 자연수의 4제곱들의 합: <br>
  시그마의 n에 해당하는 부분을 1~8000까지 대입하여 해당 샘플을 제작 <br>
  머신러닝에서 선형 회귀 기법을 이용해 학습(정확도: 1) <br>
  입력 받은 숫자 까지 각 자연수의 4제곱들의 합을 예측 <br>
  
<h2>몬티홀 문제</h2><br/>
<p>
몬티 홀 문제는 미국/캐나다 TV 프로그앰《Let's Make a Deal》에서 유래한 확률 게임입니다.

>당신이 한 게임 쇼에 참여하여 세 문 가운데 하나를 고를 기회가 주어졌다고 생각해봐라. 한 문 뒤에는 자동차가 있으며, 다른 두 문 뒤에는 염소가 있다. 당신은 1번 문을 고르고, 문 뒤에 무엇이 있는지 아는 사회자는 염소가 있는 3번 문을 연다. 그는 당신에게 "2번 문을 고르고 싶습니까?"라고 묻는다. 당신의 선택을 바꾸는 것은 이득이 되는가?

언듯 보기에는 바꾸든 바꾸지 않든 어처피 1/2로 같은 확률 아닌가? 싶지만 사실 이 문제에는 큰 함정이 숨겨져 있습니다.

예를 들어 당신이 선텍을 바꾼다고 할 때 3개의 문 중에서 1번 문을 선텍했다고 해보자 1번 문이 꽝일 확률은 2/3입니다.
이때 사회자는 당신이 고르지 않은 꽝인 문 하나와 당첨인 문 하나 중에서 꽝인 문을 열어줍니다.
이때 당신은 선텍을 바꿀 것이므로 무조건 당첨이다. 따라서 당신이 선텍을 바꿀 경우 당첨을 고를 확률은 2/3입니다.

반면에 당신이 선텍을 바꾸지 않는다면 처음 뽑을때 당첨을 뽑아야 하므로 1/3입니다.
따라서 이 문제는 "선텍을 바꾼다"가 당첨될 확률이 더 높습니다

아래는 몬티홀 문제를 플레이 할 수 있도록 만든 마크 플러그인과 파이썬 시뮬레이션 코드입니다 <br/>
[몬티홀 시뮬레이션](https://github.com/WhiteHerb/math_sim/blob/918aff672398de8e56887639aca10b8d0d9aad74/montihol/montihol.py)<br/>
[몬티홀 플러그인](https://github.com/WhiteHerb/math_sim/blob/cc3d9336d34d7a98d67ff7d1517b5908fef59065/montihol/montihol.jar)<br/>
</p>
