import os


class PythonLineCounter:
    def __init__(self, folder):
        self.folder = folder

    def count_files(self):
        return len(self.get_files())

    def get_files(self):
        return list(self.__internal_get_files(self.folder))

    def __internal_get_files(self, folder):
        for f in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, f)):
                sub_folder = os.path.join(folder, f)
                for sf in self.__internal_get_files(sub_folder):
                    yield sf
            elif f == ".DS_Store":
                pass
            else:
                yield os.path.join(folder, f)

    def count_lines(self, file):
        if file is None:
            raise TypeError

        if file.strip().endswith(".cs"):
            raise InvalidFileTypeError(file, ".cs")

        count = 0
        with open(file) as fin:
            all_lines = fin.readlines()
            if len(all_lines) > 10000:
                raise FileTooLargeError(file, len(all_lines))

            for line in all_lines:
                if self.count_as_line(line):
                    count += 1

        return count

    def count_all_lines(self):
        count = 0
        for file in self.get_files():
            count += self.count_lines(file)

        return count

    def count_as_line(self, line):
        if line is None:
            return False

        if len(line.strip()) == 0:
            return False

        if line.strip().startswith("#"):
            return False

        return True


class InvalidFileTypeError(Exception):
    def __init__(self, file, ext):
        self.file = file
        self.ext = ext

    def __str__(self):
        return "The file extension {0} of {1} is not allowed.".format(self.ext, self.file)


class FileTooLargeError(Exception):
    def __init__(self, file, numOfLines):
        self.file = file
        self.numOfLines = numOfLines

    def __str__(self):
        return "Too many lines ({0:,}) in file {1}.".format(self.numOfLines, self.file)