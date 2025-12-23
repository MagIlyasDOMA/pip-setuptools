import argparse, os


def main():
    parser = argparse.ArgumentParser(description='package-compiler')
    parser.add_argument('--no-sdist', '-s', action='store_false', dest='sdist')
    parser.add_argument('--no-wheel', '-w', action='store_false', dest='wheel')

    args = parser.parse_args()

    if not os.path.exists('setup.py'):
        raise FileNotFoundError('setup.py not found')
    command = 'python setup.py'
    if args.sdist:
        command += ' sdist'
    if args.wheel:
        command += ' bdist_wheel'

    os.system(command)


if __name__ == '__main__':
    main()
