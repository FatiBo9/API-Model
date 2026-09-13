import os
import requests

url1="http://127.0.0.1:5000/predict"
url2="http://127.0.0.1:5000/predict-batch"

def show_response(resp):
    print("status:", resp.status_code)
    print("content:", resp.headers.get("content"))
    try:
        print("JSON:", resp.json())
    except Exception:
        print("response:\n", resp.text[:1000])

def single_prediction(image_path):
    filename=os.path.basename(image_path)
    with open(image_path, "rb") as f:
        files= {"file": (filename, f, "image/jpeg")}
        resp=requests.post(url1, files=files, timeout=20)

    print("\nsingle prediction:")
    show_response(resp)

def batch_prediction(image_paths):
    opened_files= []
    try:
        files = []
        for path in image_paths:
            filename= os.path.basename(path)
            image_file= open(path, "rb")
            opened_files.append(image_file)
            files.append(("files", (filename, image_file, "image/jpeg")))

        resp= requests.post(url2, files=files, timeout=20)

        print("\nbatch prediction:")
        show_response(resp)
    finally:
        for f in opened_files:
            f.close()

if __name__ == "__main__":
    single_prediction(r"C:\Users\PC\Desktop\software integration\cat\cat.7.jpg")
    batch_prediction([
        r"C:\Users\PC\Desktop\software integration\cat\cat.7.jpg",
        r"C:\Users\PC\Desktop\software integration\cat\dog.10.jpg"
    ])