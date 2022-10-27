import datetime


def loger_maker(file_name):

    def loger(decor_func):
        """Decorator function. Log date and time into log file"""

        def decorator(*args, **kwargs):
            data = (
                f'Function: {decor_func.__name__}, '
                f'run at {str(datetime.datetime.now())}\n'
            )
            result = decor_func(*args, **kwargs)
            with open(file_name, 'a') as file:
                file.write(data)
            return result
        return decorator
    return loger


@loger_maker("log.txt")
def test_function(a, b):
    print('this is test function print')
    return a, b

def main():
    """Main function"""

    print(test_function('ac', 'bc'))


if __name__ == '__main__':
    main()
