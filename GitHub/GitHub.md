# Git

> 형상관리 / (분산)버전 관리 시스템 _ 코드의 History를 관리하는 도구

- 개발 과정 / 역사 확인 & 프로젝트 이전 버전 '복원', '비교' 가능



# GitHub

> 개발자들의 구글 드라이브 (ex. 오픈소스 프로젝트)
>
> 개발자의 이력서 & 연습장 (▶1년 동안의 게시물 → 끈기, 열정 )

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
    #현재 홈 디렉토리
    $ ~
    #화면 정리
    $ clear
    `ctrl` + `l`
    
    
    ================================================
    #작업 중인 디렉토리
    $ cd
    #상위 디렉토리 이동
    $ cd..
    #하위 디렉토리 이동
    $ cd [이동할 디렉토리 이름]
    #홈디렉토리 이동
    $ cd ~
    #디렉토리 삭제
    $ rm
    #디렉토리 안 하위 디렉토리 파일까지 함께 삭제
    $ rm -ㄱ
    ```

- Typora (가장 보편적으로 사용하는 프로그램)

## 작업 흐름

> 폴더 [표시/숨기기] 탭 - 파일 확장명 & 숨김할목 Check

1. git init  → (master) 시작 시점 

   - git"파일 생성

 ```bash
 $ git init
 ```

2. 프로젝트 진행(기능 구현)

  ```bash
  $ touch github.md
  ```

3. 버전 확정

     1. add (git status 로 생겼는지 확인 가능)
            : 특정 파일을 커밋하기 위해 추가 ( Staging Area)
        
        ```bash
        #현 디렉토리 내 모든 파일/폴더
        $git add .
        #특정 폴더
        $git add <folder>/
        #여러 파일
        #공백으로 구분
        $git add <file>.txt <file>.bmp
        ```
        
        
        
     2. commit (git log로 커밋 목록 확인 가능)
            : 버전 기록 (Commit)
        
        ```bash
        $git commit -m'(커밋메세지)''
        ```

- *git log --oneline : 커밋 한줄씩만 보기*

* *git log -2--oneline : 최근 커밋 2개 보기*

* *git status : add 상황 / git log : commit 상황*

  

  3. 원격 저장소 등록 및 Push

     ```bash
     $git remote add origin <url>
     #만들 레파지토리 주소 copy 이후 붙여넣기
     $git push origin master
     ```
     
  3. 원격 저장소 관리
     ```bash
     #조회
     $git remote -v
     #삭제
     $git remote rm origin
     ```
     
  4. 원격 저장소 복제
     ```bash
     $git clone <url>
     ```
  





## gitconfig

> Git 설정 파일

시스템, 글로벌, 로컬 설정을 각기 다르게 할 수 있음

*(global 설정 기본)*

프로젝트별 다른 설정 : `global` 대신 `local`

### Global

> ~/.gitconfig 파일에 기록되는 설정

```bash
#현재 설정 조회
$ git config --global -l
```

#### 필수

- User 정보

: Commit 시 Author로 기록되기 위해 초기 설정 필요

```bash
$ git config --global user.email "[자주쓰는 이메일]"
$ git config --global user.name "[]"
```

#### 선택

- Credential (*Github 인증* 등)

```bash
$ git config --global credential.provider generic
```

**git bash 2.32 발생 버그 해결*



**커밋 에디터 설정**

> 기존 vim ▶ visual studio code 로 변경

```bash
#먼저 다운로드 받고 실행해야함.
$ git config --global core.editor "code --wait"
```





## gitignore

>Git으로 추적하지 않을 / 추적되지 않을
>
>굳이 공유될 필요가 없거나 중요한 기밀 파일 등을 Commit 할 때

`.gitignore` 파일 생성 & 설정

```bash
#특정 파일
<file>.csv
<file>.xlsc
#특정 폴더
<folder>/
#특정 확장자
#와일드 카드 문자 사용 가능
*.bmp
```



- 일반적으로 `OS(운영체제 - mac, windows)` ,`특정 언어` ,`특정 개발환경`
  - https://github.com/github/gitignore/blob/master/Python.gitignore
  - https://gitignore.io





## Status

> Working Directory / Staging Area 여부 파악
>
> Untracked 데이터의 여부 파악 

- Untracked

- Tracked

  ​	Unmodified (조회 안됨_add가 안됨)

  ​	Modified

  ​	Staged

![image-20210706212333896](md-images/image-20210706212333896.png)





## Log

> Commit 내역 & Commit Index, Commit Message 파악

```bash
$git log --oneline #한 줄로
$git log -2 #최근 2개
$git log -2 --oneline #한 줄로 최근 2개
#브랜치 조회
$git log --oneline --graph #브랜치 그래프 형태 조회
```



## Reset & Revert

### 



## Revert



## Restore









## 오류



