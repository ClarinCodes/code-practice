import time


def get_data():
    while True:
        try:
            hours = abs(int(input("Enter Hour(s): ")))
            minutes = abs(int(input("Enter Minute(s): ")))
            seconds = abs(int(input("Enter Second(s): ")))
            return hours * 3600 + minutes * 60 + seconds
        except ValueError:
            print("\n !!! Enter only numbers !!!")
        except KeyboardInterrupt:
            print("\n !!! Back to main menu !!!")
            return None


def countdown():
    total_sec = get_data()

    if total_sec is None:
        return

    if total_sec > 0:
        try:
            for x in range(total_sec, 0, -1):
                seconds = x % 60
                minutes = (x // 60) % 60
                hours = x // 3600

                print(f"{hours:02}:{minutes:02}:{seconds:02}")
                time.sleep(1)

            print("TIME'S UP! \n")
        except KeyboardInterrupt:
            print("\n !!! TIMER Stopped !!! \n")


def main():
    while True:
        print("====== Main Menu ======")
        print("1. Countdown")
        print("2. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("\n !!! Enter only valid option !!!")
            continue
        except KeyboardInterrupt:
            print("\nexited")
            break

        if choice == 1:
            countdown()
        elif choice == 2:
            print("exited")
            break


if __name__ == "__main__":
    main()
