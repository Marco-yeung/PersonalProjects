def main():
    print(condition(file_check()))

def file_check():
    file_name = input("File name: ")
    file_name = file_name.replace(" ", "")
    return file_name

def condition(x):
    sort_list = ["gif", "jpg", "jpeg", "png", "pdf", "txt", "zip"]
    # endswtih can be used with tuple, we can turn the list into tuple to use this fucntion
    if x.endswith(tuple(sort_list)):
        return f"image/{x}"
    else:
        return "application/octet-stream"
    
if __name__ == "__main__":
    main()