#!/usr/bin/python3
import re
import os


def to_name(title):
    words = re.findall(r'\w+', title.lower())
    return '_'.join(words)


class TestCase:
    def __init__(self, article_name, test_name):
        self.test_name = test_name
        self.article_name = article_name
        self.lines = []

    def add_line(self, line):
        self.lines.append(line)

    def write(self):
        file_name = '{}_{}.cpp'.format(self.article_name, self.test_name)
        with open(file_name, 'w') as f:
            f.write(r'#define TEST_EQ(a, b) if (a != b) { cout << "Test failed!\n TEST_EQ(" #a ", " #b "): " << a << " != " << b << "\n"; return 1; }' + '\n')
            for line in self.lines:
                f.write(line)


def extract_tests(filepath):
    filepath_short = os.path.basename(filepath) 
    article_name = filepath_short.split('.')[0]
    print('Look for test cases in "{}"'.format(filepath_short))

    tests = []
    with open(filepath) as f:
        collect_test = False
        collect_lines = False
        for line in f:
            mb = re.match(r'<!--- begin test (\w+)', line)
            me = re.match(r'end test -->', line)
            if mb:
                tests.append(TestCase(article_name, mb.group(1)))
                collect_test = True
            elif me:
                collect_test = False
            elif re.match(r'^\s*```', line) and collect_test:
                collect_lines = not collect_lines
            elif collect_test and collect_lines:
                tests[-1].add_line(line)

    tests = [test for test in tests if test.lines]
    print('Found {} test cases:'.format(len(tests)))
    return tests


if __name__ == '__main__':
    tests = extract_tests('../src/data_structures/sparse-table.md')
    for test in tests:
        print(test.test_name)
        test.write()
