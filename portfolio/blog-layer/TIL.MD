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



