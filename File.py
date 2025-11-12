file_path = "example.txt" 
try: 
    with open(file_path, "r") as file: 
        lines = file.readlines() 
     
    num_lines = len(lines) 
    num_words = 0 
    num_chars = 0 
 
    for line in lines: 
        num_chars += len(line)                    # Count all characters including spaces 
        num_words += len(line.split())            # Count words by splitting on whitespace 
 
    print(f"Number of lines: {num_lines}") 
    print(f"Number of words: {num_words}") 
    print(f"Number of characters: {num_chars}") 
 
except FileNotFoundError: 
    print(f"The file '{file_path}' does not exist.")
