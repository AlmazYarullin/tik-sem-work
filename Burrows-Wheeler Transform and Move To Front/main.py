from bwt import transform_bwt
from move_to_front import MoveToFront


def main():
    mtf = MoveToFront()
    message = input("Enter your message: ")
    message_bwt = transform_bwt(message)
    print('Output:', mtf.encode(message_bwt[0]), message_bwt[1], sep='\n')


if __name__ == '__main__':
    main()
