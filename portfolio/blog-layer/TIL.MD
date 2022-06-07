# 2022.05.30

https://wikidocs.net/160270

```
확장 프로그램은 content script와 background script로 구성
content script: 실제 웹사이트에 주입되어 타유저의 웹사이트 컴포넌트 스타일을 바꾸는 등의 역할을 할 수 있음.
```



```
manifest.json파일 content_scripts의 matches는 content scripts가 주입될 웹사이트의 리스트, run_at은 주입되는 순간.
(구글에서 run_at은 document_idle 추천)
```



# 2022.05.31

환경설정하는 것부터가 어렵다.

우선 간단하게 상단의 아이콘을 클릭하면 팝업 페이지가 뜨고, 해당 페이지의 박스를 클릭하면 현재 브라우저의 body가 박스의 색으로 변하는 기초적인 실습을 진행했다.

링크를 입력해 바로 네이버로 이동하려 해봤지만, 실행되지 않았고 대신 vscode에서 alt + b를 눌러보니 그 때는 실행이 되었다.

아마 permission에 무언가를 추가해야 다른 페이지로 이동할 수 있지 않을까? 하는 생각을 해본다.

현재 페이지의 url을 받아오는 작업을 할 예정이다.
