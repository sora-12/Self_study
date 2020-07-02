c = get_config()

c.NotebookApp.ip = '*' 
c.NotebookApp.allow_root = True # root 계정에서 jupyter 사용 설정 ( 특히, docker의 경우)
c.NotebookApp.open_browser = True # jupyter 실행 시 브라우저 자동 실행 여부
c.NotebookApp.port = 8888

# c.NotebookApp.password = u'sha1:a3f5120bb892:8615550b50d21dd9df0aad7ac40df8000d1f69ef'

# c.NotebookApp.password_required = True
