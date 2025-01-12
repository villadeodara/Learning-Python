def get_extension(fn):
    fn = fn.strip().lower()
    if fn.endswith(".gif"):
        print("image/gif")
    elif fn.endswith((".jpg", ".jpeg")):
        print("image/jpeg")
    elif fn.endswith(".png"):
        print("image/png")
    elif fn.endswith(".pdf"):
        print("application/pdf")
    elif fn.endswith(".txt"):
        print("text/plain")
    elif fn.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

def main():
    fn = input("File name: ")
    get_extension(fn)

main()
