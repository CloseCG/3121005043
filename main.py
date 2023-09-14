import sys


# Custom exception class, inherited from Exception
class EmptyTextException(Exception):
    def __init__(self, *args: object) -> None:
        # Call the constructor of the parent class and pass the exception message
        super().__init__(*args)


# Raise a custom exception in this function
def check_empty(file_content):
    if not file_content:
        raise EmptyTextException("One of the files is empty!")    


def save_file():
    pass


def read_file(file_path):
    # Open the file in read-only mode 'r'
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            file_content = file.read()
            check_empty(file_content)        
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
    except EmptyTextException as e:
        print(f"Caught custom exception: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def caculate_similarity(original_text, plagiarized_text):
    pass


def main():
    # Get the parameters of the command line
    # Note that the first one is the script name
    args = sys.argv
    original_text_path = args[1]
    plagiarized_text_path = args[2]
    output_text_path = args[3]

    try:
        # Check whether the parameter is a character type
        are_all_string = all(isinstance(item, str) for item in args)
        if not are_all_string:
            raise TypeError
    except TypeError:
        print("What's up bro? Just check your input OK?")
        return TypeError
    
    # Read file
    original_text = read_file()
    plagiarized_text = read_file()
    

    # 计算相似度
    pass
    
    # 输出结果到terminal
    pass



if __init__ == '__main__':
    main()