    
# with open("text.txt", "w") as file:
#     rewrite= file.write("This is a new line.\n")
#     print(rewrite)
    
# with open("text.txt", "a") as file:
#     edit = file.write("who are you?\n")
#     print(edit)
    
# with open("text.txt", "r") as file:
#     content = file.read()
#     print(content)
    
# with open("text.txt", "r") as file:
#     for line in file:
#         print(line.strip())
        
# with open ("newfile.txt", "x") as file:
#     file.write("This is a new file created using 'x' mode.\n")
    
# import os

# if os.path.exists("text.txt"):
#     print("File exists")
# else:
#     print("File not found")    
    
# os.remove("newfile.txt")
import os

while True:
    
    print("1. Create a new file")
    print("2. Write to a file")
    print("3. Read a file")
    print("4. Append to a file")
    print("5. Delete a file")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        filename = input("Enter the Fiile name:")
        with open(filename, "x") as file:
            print(f"{filename} created successfully.")
            
    elif choice == "2":
        filename  = input("Enter the file name:")
        content = input("Enter the content to write:")
        with open(filename, "w") as file:
            file.write(content)
            print(f"Content written to {filename} successfully.")
            
    elif choice == "3":
        filename = input("Enter the file name:")
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of {filename}:\n{content}")
            
    elif choice == "4":
         filename  = input("Enter the file name:")
         add = input("Enter the content to add:")
         with open(filename, "a") as file:
             file.write(add)
             print(f"Content added to {filename} successfully.")

    elif choice == "5":
        filename = input("Enter the file name:")
        if os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} deleted successfully.")
        else:
            print("File not found.")

    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
        
        