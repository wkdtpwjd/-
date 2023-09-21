from django.db import models

# Create your models here.
# 내가 application 에서 사용할 데이터 정의
# Model 형태로
# 되게 많은 기능을 포함해야 하는데....
# 장고가 이미 많이 만들어 뒀습니다.
# 어떤 데이터가 필요한지만 설정하면 됩니다.
# 게시판의 게시글 : 제목, 내용
class Article(models.Model):
    # 사용할 값이름 = 자료형 
    title = models.CharField(max_length=10)        # 짧은 문자열
    content = models.TextField()      # 긴 문자열