import datetime


def loger_maker(file_name):

    def loger(decor_func):
        """Decorator function. Log date and time into log file"""

        def decorator():
            data = (
                f'Function: {decor_func.__name__}, '
                f'run at {str(datetime.datetime.now())}\n'
            )
            decor_func()
            with open(file_name, 'a') as file:
                file.write(data)

        return decorator
    return loger


@loger_maker("log.txt")
def test_function():
    print('this is test function print')


def main():
    """Main function"""

    test_function()


if __name__ == '__main__':
    main()
