import argparse
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


def accumulate_all_java_file_to_file():
    print('Searching, path is ' + args.dir + '\n')

    files_path_to_read = list(Path(args.dir).rglob(args.extension))
    with open('./result.txt', mode='w+') as result_file:
        for file in files_path_to_read:
            with open(file.absolute().__str__()) as reader:
                result_file.write('Class name is: ' + file.name.__str__() + '\n\n')
                result_file.write(reader.read())
                result_file.write('End class ' + file.name.__str__() + '\n\n')
    print(str(files_path_to_read.__len__()) + ' Files was founded and written to result file')


if __name__ == '__main__':
    accumulate_all_java_file_to_file()
