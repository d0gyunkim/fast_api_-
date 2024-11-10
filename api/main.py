from fastapi import FastAPI  # FastAPI import


app = FastAPI()   # fastapi 객체를 생성한다. uvicorn이라는 ASGI 서버를 통해 이 파일의 app 인스턴스가 참조된다


@app.get("/print_hello") # 이 부분을 파이썬에서는 데코라이터라고 한다. 이는 함수를 변형하고 함수에 새로운 기능을 추가한다. 
# fastapi에서는 fastapi 객체에 대해 데코레이터로 수정된 함수를 경로 동작 함수라고 한다. 이는 경로(path)와 동작(operation) 두부분으로 나뉜다
# 경로는 /print_hello이고 동작은 GET이다. GET은 HTTP 메서드 중 하나로, 서버에게 리소스를 요청하는 메서드이다.
async def hello(): # 아래의 텍스트를 반환한다.
    return {"message": "Hello World, from FastAPI!"}

@app.get("/print_name") # 이 부분을 파이썬에서는 데코라이터라고 한다. 이는 함수를 변형하고 함수에 새로운 기능을 추가한다. 
async def print_name(): # 아래의 텍스트를 반환한다.
    return {"message": "my name is dk"}
