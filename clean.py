# coding: utf-8
def is_russian_letter(char):
    # Check if the character is a Russian letter or a newline
    return ('а' <= char <= 'я') or ('А' <= char <= 'Я') or (char in 'ёЁ') or (char == '\n')

def remove_non_russian_letters(file_path):
    # Open the input file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Filter the content to keep only Russian letters and newlines
    cleaned_content = ''.join(char for char in content if is_russian_letter(char))

    # Write the cleaned content back to a new file or overwrite the existing one
    with open('cleaned_' + file_path, 'w', encoding='utf-8') as cleaned_file:
        cleaned_file.write(cleaned_content)

# Example usage
remove_non_russian_letters('nouns.txt')
