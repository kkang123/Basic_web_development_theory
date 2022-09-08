# 💻📖 git

**git Merge, Rebase**

<br>


* [Merge와 Reabse 차이](#Merge와-Reabse-차이)
* [Merge](#Merge)
* [Rebase](#Rebase)
* [Commit](#Commit)
    

<br>


## Merge와 Reabse 차이

Merge는 branch를 통합하는 것이고, Rebase는 branch의 base를 옮긴다는 개념의 차이가 있다.

사용법으로는

1. Merge만 사용한다.

2. Rebase와 Merge를 사용한다.

## Merge

`git merge [브랜치명]` : '현재'브랜치에서 [브랜치명]의 변경사항을 병합

`git merge`를 통해 다른 브랜치와 병합할 수 있다.

main 브랜치에서 `git merge [branch001]을 하면 branch001을 main브랜치에 병합 하는 것이다.


## Rebase


Rebase란?

우선 rebase는 base를 다시 지정한다는 (re-base)의 의미다.


A <- B <- C <- D1 <- `[main]`
            <- D2 <- `[master]`

다음 커밋 중 D1, D2 두개의 커밋은 C라는 같은 조상에 시작되었다. 이때, 이 C가 base이다.


## Commit

Commit은 변경 내용을 확정 `git commit`

`git commit -m "message"`를 통해 커밋 메세지를 남길 수 있다.