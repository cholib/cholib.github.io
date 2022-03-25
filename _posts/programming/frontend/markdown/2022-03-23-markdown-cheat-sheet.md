---
layout: post
title: "마크다운 문법(Markdown Syntax)"
category: programming
tags: frontend 
image: /assets/img/md/Markdown.png
accent_image: 
  background: url('/assets/img/md/i-love-markdown.png') center/cover
  overlay: false
accent_color: '#ccc'
theme_color: '#ccc'
description: >
  Markdodwn Cheat Sheet 
invert_sidebar: true  
date: 2022-03-23
last_modified_at: 2022-03-23
---

<details>
<summary>🧾 Prologue (접기/펼치기)</summary>
<div markdown="1">

<br>
 

## Markdown이란?
### 정의

> Markdown은 문서 작성을 지원하는 태그(Tag) 형식의 문법.

> Markup 언어의 일종으로, HTML 경험 없이도 헤더, 글 머리 기호, 테이블, 이미지/ 링크 삽입, 글자 모양 등 다양한 서식을 쉽게 추가하는 방식의 문서 편집 문법.

> 마크다운(markdown)은 일반 텍스트 문서의 양식을 편집하는 문법이다. README 파일이나 온라인 문서, 혹은 일반 텍스트 편집기로 문서 양식을 편집할 때 쓰인다. 마크다운을 이용해 작성된 문서는 쉽게 HTML 등 다른 문서형태로 변환이 가능하다. (출처 - 위키백과)

> 마크다운 (Markdown)은 마크업 언어의 일종으로, 존 그루버(John Gruber)와 아론 스워츠(Aaron Swartz)가 만들었다. 처음 이메일의 글쓰기 형식에 영감받아 python을 이용하여 html변환기를 만드면서 시작되었다. 그루버는 마크다운으로 작성한 문서를 HTML로 변환하는 펄 스크립트도 만들었다. 

### 특징

마크다운 문법은 읽기도 쉽지만 쓰기도 쉽다는 장점이 있다. html보다 간단하고, 마크다운에서는 소스코드를 그대로 입력할 수 있기 때문에 코드를 복사해서 사용하기도 편하고, 코드블록을 사용하면 코딩언어에 따라 하이라이트를 지원하여 가독성이 높아지는 효과가 있다.  

생산성 관련하여 작성 속도, 편리성 면에서 Web문서 작성시 유리하다. 다만, 표준이 없어 핵심문법을 제외하고는 편집자에 따라 조금씩 상이하다. Tistory, Naver 블로그가 채택한 WISYWIG 에디터에 익숙한 사용자들에게는 마크다운 문법이 코딩처럼 느껴지실 수 있지만, 조금 익숙해지면 오히려 WISYWIG에디터보다 편하다는 것을 알게 될 것이다. 마크다운 문서의 파일 확장자는 .md를 쓴다. 

</div>
</details>
<br>

* this unordered seed list will be replaced by the toc
{:toc}


## 코드 블록

### 인라인 블록
```html
`inline 코드`입니다.
```
`inline 코드`입니다.

### 코드 블록
물결표시(Tilde)키에 있는 \` (Grave)를 세 개 쓰고 랭귀지명 입력후 코드 작성.  
\`\`\`언어 이름(소문자)   
   코드 입력  
\`\`\`  


예를 들어,

\`\`\`c#<br>
public int Score{<br>
   get{<br>
     return Score;<br>
   }<br>
   set{<br>
      if (Score<0){<br>
      Score = 0;<br>
     }<br>
   Score += value;<br>
   }<br>
}<br>
\`\`\` 

```c#
     public int Score{
         get{
             return Score;
         }
 
         set{
             if (Score<0){
                 Score = 0;
             }
             Score += value;
         }
     }
```

<br>

## 표

`|` (VERTICAL BAR) 와 `-`를 세 개 이상 입력하여 표를 만들 수 있다.
- 정렬
  - 왼쪽 정렬 \|:---\|
  - 오른쪽 정렬 \|---:\|
  - 가운데 정렬 \|:---:\|

```markdown
|제목|별점|명대사|
|:---:|---:|---|
|타짜|⭐⭐⭐⭐⭐|"쏠 수 있습니다."|
|범죄와의 전쟁|⭐⭐⭐⭐⭐|"위축 되었습니까?"|
|내부자들|⭐⭐⭐⭐⭐|"몰디브에 가서 모히또를 드시겠습니까?"|
```  

|제목|별점|명대사|
|:---:|---:|---|
|타짜|⭐⭐⭐⭐⭐|"쏠 수 있습니다."|
|범죄와의 전쟁|⭐⭐⭐⭐⭐|"위축 되었습니까?"|
|내부자들|⭐⭐⭐⭐⭐|"몰디브에 가서 모히또를 드시겠습니까?"|

<br>

## 줄바꿈
1️⃣ `줄바꿈`을 하고 싶다면 문장 뒤에서 <kbd>spacebar</kbd>를 두 번 + <kbd>Enter</kbd> 입력합니다.
```markdown
안녕하세요.  
조연어입니다.
```
안녕하세요.   
조연어입니다.

2️⃣ \<br>을 입력합니다.
```html
안녕하세요. <br> 조연어입니다.
```
안녕하세요. <br> 조연어입니다.

<br>

## 문단 나누기

한 줄의 공백을 입력하여 작성합니다.


```markdown
안녕하세요.

조연어 입니다.
```

안녕하세요.

조연어 입니다.


<br>

## 들여쓰기 

<kbd>Tab</kbd> 또는 <kbd>spacebar</kbd> 네 번 입력하여 하위 목록을 표시해 줄 수 있다.

```markdown
- hi
  - hello
    - 안녕
```
- hi
  - hello
    - 안녕

<br>

## 마크다운 문법 표시
마크다운 키워드 앞에 `\` (<kbd>Back Slash</kbd>) 를 붙여준다. 
```markdown
\<u>이렇게</u>
```
\<u>이렇게</u>  
밑줄 그어진 형태로 <u>이렇게</u>로 보일텐데 `\` (Back Slash) 를 앞에 붙여주어 문법 그대로 \<u>가 보여진다.

<br>



## 텍스트

### 강조
```markdown
**볼드체**
```
**볼드체**


### 이탤릭체
```markdown
*기울어진 텍스트*
***굵고 기울여진 텍스트***
```
*기울어진 텍스트입니다*
***굵고 기울어진 텍스트***

### 취소선
```markdown
~~취소 표시~~
```
~~취소 표시~~

### 밑줄
```html
<u>텍스트에 밑줄</u>
```
<u>텍스트에 밑줄</u>

### 글씨 색
```html
<span style="color:green"> 녹색입니다.</span>
```  
<span style="color:green"> 녹색입니다.</span>

#### 적용 
```html
~~***<u>오예스</u>***~~
```
~~***<u><span style="color:red">오예스</span></u>***~~

<br>


## Link

### 텍스트에 링크 삽입
\[링크설명](링크 주소)
```html
[Google](https://www.google.com)
```
[Google](https://www.google.com)

### 동일 파일 내에서의 문단(헤더) 이동 링크
\[설명어]\(문단의 주소)


### 이미지에 링크 삽입
\!\[image](이미지주소)  

![image](/assets\img\md\atelier401restroompicture.jpg){: width="70%" height="70%"}{: .align-center}

### 이미지에 링크 삽입(새창)
\!\[image](이미지주소)](이동하려는 링크 주소)&#123;: target="_blank"&#125;<br>
[![image](/assets\img\md\w3cschool.jpg){: target="_blank"}{: width="100px" height="100px"}{: .align-center}](https://www.w3schools.com/)



### 유튜브 삽입
```html
<div class="iframe-container">
    <iframe src="유튜브 링크 주소" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>
```
<div class="iframe-container">
    <iframe src="https://www.youtube.com/embed/jtGVbx4E1a8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

<br>

## 인용문
`>` 로 표현할 수 있다.  
`>>` 두개 쓰면 중첩된 인용문.
중첩시킬땐 앞에 <kbd>spacebar</kbd> 두 번 입력한다. 
```html
>  인용문입니다.
  >>  인용문 속 인용문입니다.
```
>  인용문입니다.
  >>  인용문 속 인용문입니다.

<br>

## 목차
### Unordered list
```html
- 가나다
  * 라마바
    + 사아자 
  * 차카타
- 파하하
```  
- 가나다
  * 라마바
    + 사아자 
  * 차카타
- 파하하

### Ordered list
```html
1. 가나다
2. 라마바  
   1. 사아자
      - 차
      - 카
   2. 타파
       - 하하
       - 하하하
3. 알겠쥬   
```
1. 가나다
2. 라마바  
   1. 사아자
      - 차
      - 카
   2. 타파
       - 하하
       - 하하하
3. 알겠쥬  

### check list
✔ \- \[ \] 입력으로 리스트를 체크박스 형태로 표시할 수 있다.  
(\[\]앞뒤로 space(여백) 주의.)

```markdown
- [x] Checked
- [ ] Unchecked
- [ ] 아메리카노
- [x] 카페라떼
- [ ] 카푸치노
```

- [x] Checked
- [ ] Unchecked
- [ ] 아메리카노
- [x] 카페라떼
- [ ] 카푸치노


<br>

## 구분선
`***`와 `---`로 나타낼 수 있다.
```
***
---
```
***
---


<br>

## 토글 (접기/펼치기)

마크다운에서는 지원하지 않으나 HTML의 `details` 태그로 사용 가능하다.  
`div markdown=”1”` 은 jekyll에서 html사이에 <b>Markdown</b>을 인식 하기위해서 사용.
```html
<details>
<summary>클릭</summary>
<div markdown="1">       

짜잔!

</div>
</details>
```

<details>
<summary>클릭(접기/펼치기)</summary>
<div markdown="1">       

짜잔!

</div>
</details>

<br>

## 맨 위로 가기 버튼
링크를 `#`로 설정하면 페이지 맨 위로 이동.  

```html
<a href="#" class="btn--primary">맨 위로</a>
```

<a href="#" class="btn--primary">맨 위로</a>



<br>
 
## Header
<u>글의 제목</u>이 된다. 각 제목마다 permalink가 있는 것이 특징! # ~ ###### 로 제목 크기에 따라 h1 ~ h6을 나타낸다.
```markdown
# h1
## h2
### h3
#### h4
##### h5
###### h6
```
# h1
## h2
### h3
#### h4
##### h5
###### h6 

<br>

***
<br>

<br>

👨‍💻 개인 학습자료용 기록 블로그입니다. 오류나 틀린 부분에 대해서는 언제든지 댓글이나 메일로 알려주시면 즉시 수정토록 하겠습니다. 감사합니다.👨‍🔧
      
[🔼TOP](# "맨 위로 이동하기"){: .btn .btn--primary }{: .align-right}

<br>

<a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/"><img alt="크리에이티브 커먼즈 라이선스" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png" /></a>이 저작물은 <a rel="license" href="http://creativecommons.org/licenses/by-nc-nd/4.0/">크리에이티브 커먼즈 저작자표시-비영리-변경금지 4.0 국제 라이선스</a>에 따라 이용할 수 있습니다.


<!--link address-->

