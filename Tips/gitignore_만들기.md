## .gitignore

* `.gitignore`는 git에서 특정한 몇몇 파일들의 히스토리를 추적하지 않기 위해서 사용한다.
* `.gitignore`는 단순한 텍스트 파일이며, 저장소 내 root에 위치할 수도 있고 각각의 서브 디렉토리 안에 위치할 수도 있다.
  * root에 위치하게 되면 모든 서브 디렉토리는 root의 .gitignore 설정을 상속 받게 된다.
* [.gitignore에 대한 상세 내용](https://git-scm.com/docs/gitignore)

<br/>
## .gitignore 파일의 내용
파일 내 명시되는 폴더, 파일명은 git에서 untrack 상태가 되므로, 버전 관리 대상에서 제외된다.  
파일 및 폴더명에 `*, !`와 같은 패턴도 포함될 수 있다.  
 * `*`은 `all`과 같은 의미이며, 접미사로 사용된다.
 * `!`은 특정 폴더가 untrack 상태이더라도 그 안의 특정 파일은 untrack 대상으로부터 제외시키고 싶을 때 사용한다.
```code
# exclude everything except directory foo/bar
/*
!/foo
/foo/*
!/foo/bar
```

<br/>
## .gitignore 파일 만들기
 * 프로젝트를 진행하기에 앞서, 빌드 시 생성되는 임시 파일들은 굳이 저장소에 업로드 할 필요가 없기 때문에 `.gitignore` 파일부터 먼저 저장소 폴더 안에 포함시키는 편이 좋다.
 * 각 개발 언어마다 빌드 시, 만들어지는 임시 파일들은 다르기 때문에 이를 적절하기 filter 처리해야 한다.
   * C/C++: *.o, *.obj, *.dll, *.so, *.a, *.pdb, *.exe 등등
   * C#: *.dll, *.pdb, *.exe 등등
 * 위에서 나열한 확장자들 이외에 여러가지 추가 파일들이 있으므로 이를 매번 기억할 수 없기 때문에,  
   `.gitignore`를 만들어 주는 써드파티 툴들이 몇몇 있다.
   * [https://www.gitignore.io/](https://www.gitignore.io/)에서 프로젝트 언어에 알맞는 `.gitignore` 파일을 만들 수 있다.
   * OS X, Linux에선 파일명이 없는 파일을 만들 수 있지만, Windows는 간단하지 않으므로 다음과 같이 한다.  
   
     ```bash
     # 메모장에서 gitignore.txt 파일 생성.
     # gitignore.txt 파일이 있는 폴더에서 명령 프롬프트를 띄워서 다음과 같이 파일명을 변경한다.
     $ ren gitignore.txt .gitignore
     ```
