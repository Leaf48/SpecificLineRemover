import sys
from time import sleep

# choose -r remove or -rl remove line
CMD = None
if len(sys.argv) > 1:
    if sys.argv[1] == "-r" or sys.argv[1] == "-rl":
        CMD = sys.argv[1]
    else:
        print("Please choose -r (remove) or -rl (remove line)")
        sleep(10)
        sys.exit()
else:
    print("Please choose -r (remove) or -rl (remove line)")
    sleep(10)
    sys.exit()

SOURCE_PATH = None
if len(sys.argv) > 2:
    SOURCE_PATH = sys.argv[2]
else:
    print("Please type your source file path!")
    sleep(10)
    sys.exit()

PARAMETER_PATH = None
if len(sys.argv) > 3:
    PARAMETER_PATH = sys.argv[3]
else:
    print("Please type your parameter file path!")
    sleep(10)
    sys.exit()


def executor(mode, src_path, param_path):
    # remove char
    if mode == "-r":
        params = []
        with open(param_path, "r") as r:
            for i in r:
                params.append(i.strip())

        src = []
        with open(src_path, "r") as r:
            for i in r:
                src.append(i.strip())

        result = []
        temp = None
        for n, i in enumerate(src):
            temp = i
            for p in params:
                if p in i:
                    temp = temp.replace(p, "")
            if temp == "":
                continue
            result.append(temp)

        with open("./output_r.txt", "a") as w:
            for i in sorted(result):
                print(i, file=w)

        print("Finished removing words!")

    elif mode == "-rl":
        params = []
        with open(param_path, "r") as r:
            for i in r:
                params.append(i.strip())

        src = []
        with open(src_path, "r") as r:
            for i in r:
                src.append(i.strip())

        result = []

        def filtering(line):
            if line == "":
                return True
            for p in params:
                if p in line:
                    return True

        for i in src:
            temp = i
            if not filtering(temp):
                result.append(temp)

        with open("./output_rl.txt", "a") as w:
            beautyResult = []
            for i in sorted(result):
                if i not in beautyResult:
                    beautyResult.append(i)
            for i in beautyResult:
                print(i, file=w)

        print("Finished removing lines!")


if __name__ == '__main__':
    executor(mode=CMD, src_path=SOURCE_PATH, param_path=PARAMETER_PATH)
