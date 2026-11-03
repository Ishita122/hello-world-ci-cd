# app.py
# CI trigger test: comment-only change to verify workflow runs on push
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__":
    print(hello_world())
