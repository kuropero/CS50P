# implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.
#.gif   image/gif
#.jpg   image/jpeg
#.jpeg  image/jpeg
#.png   image/png
#.pdf   application/pdf
#.txt   text/plain
#.zip   application/zip

# ### Method 1 ####
# file_type = input("What file is this?\n").lower().strip()

# if file_type.endswith(".gif", ".jpeg", ".png"):
#     print("image/" + file_type[file_type.find(".")+1:])

# elif file_type.endswith(".jpg"):
#     print("image/jpeg")

# elif file_type.endswith(".pdf") or file_type.endswith(".zip"):
#     print("application/" + file_type[-3:])

# elif file_type.endswith(".txt"):
#     print("text/plain")

# else:
#     print("application/octet-stream")

#### Method 2 ####
filename = input("File type: ").lower().strip()
filetype = filename.split(".")[-1]

match filetype:
    case "jpeg" | "gif" | "png":
        print(f"image/{filetype}")

    case "jpg":
        print("image/jpeg")

    case "pdf" | "zip":
        print(f"application/{filetype}")

    case "txt":
        print("text/plain")

    case _:
        print("application/octet-stream")
