import datetime
import time
import webbrowser

from leagues import LEAGUES

BASE_URL = "https://lolesports.com/live/{league}"


def prompt_league():
    for i, league in enumerate(LEAGUES, 1):
        print(f"{i}. {league}")

    while True:
        league = input("Select a number above or enter the league ID: ").strip()
        try:
            idx = int(league)
            return league[idx - 1]
        except ValueError:
            if league in LEAGUES:
                return league
        except IndexError:
            pass


def prompt_time(league_id: str = None):
    if league_id:
        print(f"Check schedule at: https://lolesports.com/schedule?leagues={league_id}")
    return input("Enter local time (HHMM) to open tab: ").strip()


def now():
    return datetime.datetime.now().strftime("%H%M")


def open_link(url: str):
    webbrowser.open(url)


def run_loop(target_url: str, target_time: str):
    print("\n=========================================================")
    print(f"Waiting till {target_time}. Refreshing every 10 seconds...")
    print(f"Link: {target_url}")

    while now() <= target_time:
        time.sleep(10)

    open_link(target_url)
    print(f"It is now {now()}. Opening {target_url}")

    input("Link didn't open? Press Enter to try again, or Ctrl+C to cancel.")
    open_link(target_url)


if __name__ == "__main__":
    target_league = prompt_league()
    target_time = prompt_time()
    target_url = BASE_URL.format(league=target_league)
    run_loop(target_url=target_url, target_time=target_time)
