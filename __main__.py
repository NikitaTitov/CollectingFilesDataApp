import argparse
import re
from pathlib import Path

parser = argparse.ArgumentParser(
    description='Program for searching and summarising text of all founded by extension \n Supported extensions: '
                '*.txt, *.java, *.class'
)
parser.add_argument('-dir', default='.', help='Root directory')
parser.add_argument(
    '-extension',
    default='*.java',
    choices=['*.java', '*.class', '*.txt'],
    help='File extension which will be searched'
)

args = parser.parse_args()


def clean_up_text(file_text) -> str:
    result_file_text = re.sub(r'(import [a-zA-Z]+.+;)|(package [a-zA-Z]+.+;)', '', file_text)
    result_file_text = re.sub(r'(?s:\/\*.*?\*\/)|\/\/.*', '', result_file_text)
    result_file_text = re.sub(r'\n{3,}', '\n', result_file_text)
    result_file_text = re.sub(r'\t\n', '', result_file_text)
    return result_file_text


def accumulate_all_java_file_to_file():
    print('Searching, path is ' + args.dir + '\n')

    files_path_to_read = list(Path(args.dir).rglob(args.extension))
    with open('./result.txt', mode='w+', encoding='utf-8') as result_file:
        for file in files_path_to_read:
            with open(file.absolute().__str__(), encoding='utf-8') as reader:
                file_text = reader.read()
                file_text = clean_up_text(file_text)
                result_file.write(file_text)
    print(str(files_path_to_read.__len__()) + ' Files was founded and written to result file')


if __name__ == '__main__':
    accumulate_all_java_file_to_file()
