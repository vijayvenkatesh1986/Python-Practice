try:
    path = "C:/Vijay/Admin/Downloads\\demo.txt"
    filepath = open(path,"w")
    filepath.write("Exception Handling validation....")
    filepath = open(path,'r')
    print(filepath.read())

except Exception as e:
    print(e)

finally:
    try:
        filepath.close()
    except Exception as e:
        print(e)

