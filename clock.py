"""Простые часы для терминала: выводит текущее время каждую секунду.

Запуск:
    python clock.py          # непрерывно, остановить: Ctrl+C
    python clock.py --once   # вывести время один раз и выйти
"""

import argparse
import time
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser(description="Вывод текущего времени в терминале")
    parser.add_argument("--once", action="store_true", help="вывести время один раз и выйти")
    args = parser.parse_args()

    if args.once:
        print(datetime.now().strftime("%H:%M:%S"))
        return

    try:
        while True:
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            # \r возвращает курсор в начало строки, поэтому время обновляется на месте
            print(f"\rТекущее время: {now}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nВыход.")


if __name__ == "__main__":
    main()
