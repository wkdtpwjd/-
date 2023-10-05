from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    pass
# pass 로 두고 필요시에 작성한다 . 
# 반드시 User모델을 대체해야 한다
# 커스텀 User모델은 기본 User모델과 동일하게 작동 하면서도
# 필요한 경우 나중에 맞춤 설정할 수 있기 떄문
# 단 User모델 대체 작업은 프로젝트의 모든 migrations,첫 migrate를 실행하기전에 
# 이 작업을 마쳐야 함