import sys
from simhash import Simhash
import jieba.analyse
import logging

jieba.setLogLevel(logging.INFO) # Shut the fk up!

# Custom exception class, inherited from Exception
class EmptyTextException(Exception):
    def __init__(self, *args: object) -> None:
        # Call the constructor of the parent class and pass the exception message
        super().__init__(*args)


# Raise a custom exception in this function
def check_empty(file_content):
    if not file_content:
        raise EmptyTextException("One of the files is empty!")    


def participle(content):
    """
    perform word segmentation and calculate weights
    :param: text
    :return: metatable in the form of(token, weight)
    """
    # Determine whether it is a string type
    try:
        if not isinstance(content, str):
            raise TypeError
        # 今天也是可爱的调包侠哎嘿
        jieba.analyse.set_stop_words('./CNstopwords.txt')
        tags = jieba.analyse.extract_tags(content, topK=20, withWeight=True)
        return tags
    except TypeError:
        print("I say string! You understand?");
        return TypeError



def save_file(file_path, file_content):
    # Determine whether it's a float type and whether the size is in [0, 1]
    try:
        if not isinstance(file_content, float):
            raise TypeError
        if file_content < 0 or file_content > 1:
            raise ValueError
        # Open the file in write mode 'w'
        with open(file_path, 'w') as file:
            # Write content
            file.write("{:.2f}".format(file_content))
    except TypeError:
        print("I say float! You understand")
        return TypeError
    except ValueError:
        print("Keep your value in [0, 1]!")
        return ValueError


def read_file(file_path):
    # Open the file in read-only mode 'r'
    try:
        with open(file_path, 'r') as file:
            # Read the entire file content
            file_content = file.read()
            check_empty(file_content)        
    except FileNotFoundError:
        print(f"File '{file_path}' not found")
        return FileNotFoundError
    except EmptyTextException as e:
        print(f"Caught custom exception: {e}")
        return EmptyTextException
    except Exception as e:
        print(f"An error occurred: {e}")
        return Exception
    else:
        return file_content


def caculate_similarity(original_text_weight, plagiarized_text_weight):
    """
    get the similarity of two texts
    :param text_a: original text
    :param text_b: plagiarized text
    :return: similarity
    """
    # Determine whether it's a list type. About the source code, here is a list
    # with the meta-group as the element
    try:
        if not isinstance(original_text_weight, list) or not isinstance(plagiarized_text_weight, list):
            raise TypeError
        o_simhash = Simhash(original_text_weight)
        p_simhash = Simhash(plagiarized_text_weight)
        max_hashbit = max(len(bin(o_simhash.value)), len(bin(p_simhash.value)))
        # Hamming distance
        distince = o_simhash.distance(p_simhash)
        print(f"The hamming distance(they are similar when the value is less than 4): {distince}")
        similar = 1 - distince / max_hashbit
        return similar
    except TypeError:
        return TypeError


def main():
    # Get the parameters of the command line``
    # Note that the first one is the script name
    # args = sys.argv
    # original_text_path = args[1]
    # plagiarized_text_path = args[2]
    # output_text_path = args[3]

    original_text_path = './orig.txt'
    plagiarized_text_path = './orig_0.8_add.txt'
    output_text_path = './output.txt'
    args = [original_text_path, plagiarized_text_path, output_text_path]

    try:
        # Check whether the parameter is a character type
        are_all_string = all(isinstance(item, str) for item in args)
        if not are_all_string:
            raise TypeError
    except TypeError:
        print("What's up bro? Just check your input OK?")
        return TypeError
    
    # Read file
    original_textLweight = participle(read_file(original_text_path))
    plagiarized_textLweight = participle(read_file(plagiarized_text_path))
    
    # caculate similarity
    similarity = caculate_similarity(original_textLweight, plagiarized_textLweight)
    
    # Output the result to the specified file
    save_file(output_text_path, similarity)


if __name__ == '__main__':
    main()
