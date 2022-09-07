# 💻📖 git

**git Merge, Rebase**

<br>


* [Merge와 Reabse 차이](#Merge와 Reabse 차이)
* [Merge](#Merge)
* [Rebase](#Rebase)
    

<br>


## Merge와 Reabse 차이

Merge는 branch를 통합하는 것이고, Rebase는 branch의 base를 옮긴다는 개념의 차이가 있다.

사용법으로는

1. Merge만 사용한다.

2. Rebase와 Merge를 사용한다.

## Merge



## Rebase


Rebase란?

우선 rebase는 base를 다시 지정한다는 (re-base)의 의미다.


A <- B <- C <- D1 <- `[main]`
            <- D2 <- `[master]`

다음 커밋 중 D1, D2 두개의 커밋은 C라는 같은 조상에 시작되었다. 이때, 이 C가 base이다.
