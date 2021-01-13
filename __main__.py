import argparse
import re
from pathlib import Path

from app.regex_patterns import *
from app.supported_extentions import *

parser = argparse.ArgumentParser(
    description='Program for searching and summarising text of all founded by extension \n Supported extensions: '
                '*.txt, *.java, *.class, *.kt, *.ts'
)
parser.add_argument('-dir', default='.', help='Root directory')
parser.add_argument(
    '-clean',
    default=True,
    help='Perform clean files to delete comments(java/kotlin style), packages, imports'
)
parser.add_argument(
    '-fileExt',
    default=java_extension,
    choices=[java_extension, class_extension, text_extension, kotlin_extension, typescript_extension],
    help='File extension which will be searched'
)

args = parser.parse_args()


def remove_packages_imports(file_extension, file_text) -> str:
    if file_extension == java_extension:
        result_file_text = re.sub(java_package_imports_regexp, '', file_text)
    elif file_extension == kotlin_extension:
        result_file_text = re.sub(kotlin_package_imports_regexp, '', file_text)
    elif file_extension == typescript_extension:
        result_file_text = re.sub(typescript_package_imports_regexp, '', file_text)
    else:
        result_file_text = file_text
    return result_file_text


def clean_up_text(file_text, file_extension) -> str:
    result_file_text = remove_packages_imports(file_extension, file_text)

    result_file_text = re.sub(java_kotlin_comments_regexp, '', result_file_text)
    result_file_text = re.sub(new_line_endings_regexp, '\n', result_file_text)
    result_file_text = re.sub(empty_lines_with_tabs_regexp, '', result_file_text)
    return result_file_text


def accumulate_all_java_file_to_file():
    print('Change slash in searching dir to unix style')
    args.dir = re.sub(r'\\', '/', args.dir)
    print('Searching path is ' + args.dir + '\n')
    print('Searching files with extension is ' + args.fileExt)

    files_path_to_read = list(Path(args.dir).rglob(args.fileExt))

    print(str(files_path_to_read.__len__()) + ' Files was founded')

    if not files_path_to_read.__len__():
        print('Any files was founded in directory file result.txt wasn\'t created')
        return

    with open('./result.txt', mode='w+', encoding='utf-8') as result_file:
        for file in files_path_to_read:
            with open(file.absolute().__str__(), encoding='utf-8') as reader:
                file_text = reader.read()

                if args.clean:
                    file_text = clean_up_text(file_text, args.fileExt)

                result_file.write(file_text)

    print(str(files_path_to_read.__len__()) + ' Files was written to result file')


if __name__ == '__main__':
    accumulate_all_java_file_to_file()
