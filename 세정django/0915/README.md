### 할일

### 게시글작성

### 게시글목록

### 게시글삭제

* 요청 정리
  
  인덱스 화면 요청(/articles/index/)
  
  작성 화면 요청 (/articles/new/)
  
  DB에 글 저장하고 ,index화면 보여주기 요청(/articles/create/)

       DB에 글 삭제하고, index화면 보여주기 요청(/articles/delete/)



### 운영자 계정 생성

python manage.py createsuperuser



model.py 에서 작성하면 Article 에서 title이 Article object가 아니라 우리가 적은 title로 나오게 된다.

  def __str__(self):

        return self.title  
