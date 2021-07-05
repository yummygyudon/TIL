# Git

> 형상관리 / (분산)버전 관리 시스템 _ 코드의 History를 관리하는 도구

- 개발 과정 / 역사 확인 & 프로젝트 이전 버전 '복원', '비교' 가능



# GitHub

> 개발자들의 구글 드라이브 (ex. 오픈소스 프로젝트)
>
> 개발자의 이력서 & 연습장 (▶1년 동안의 게시물)

## 필요 프로그램

- Git bash

  - [명령어]

    ```bash
    #비어있는 파일 만들기
    $ touch (파일명.파일형식)
    #만들어진 파일 이름 조회
    $ ls
    #현제 Working Directory(작업공간) 주소 조회
    $ pwd
    #폴더 만들기
    $ mkdir (폴더명)
    #폴더 이동
    $ cd (폴더명)
    ```

- Typora (가장 보편적으로 사용하는 프로그램)

## 작업 흐름

> 폴더 [표시/숨기기] 탭 - 파일 확장명 & 숨김할목 Check

1. git init  → (master) 시작 시점 

   - git"파일 생성

 ```bash
 $ git init
 ```

​     

2. 프로젝트 진행(기능 구현)

  ```bash
  $ touch github.md
  ```
3. 버전 확정

     1. add (git status 로 생겼는지 확인 가능)
            : 특정 파일을 커밋하기 위해 추가 ( Staging Area)
        
              ```bash
              $git add(파일명)
              ```
        
     2. commit (git log로 커밋 목록 확인 가능)
            : 버전 기록 (Commit)
        
        ```bash
        $git commit -m'(커밋메세지)''
        ```

* *git log --oneline : 커밋 한줄씩만 보기*

* *git log -2--oneline : 최근 커밋 2개 보기*

* *git status : add 상황 / git log : commit 상황*

  

  3. 원격 저장소 등록 및 Push

     ```bash
     $git remote add origin <url>
     $git push origin master
     ```
     
  3. 원격 저장소 관리
     ```bash
     $git remote -v
     $git remote rm master
     ```
     
  4. 원격 저장소 복제
     ```bash
     $git clone <url>
     ```
  
  