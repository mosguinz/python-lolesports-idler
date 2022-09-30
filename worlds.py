import idler

if __name__ == "__main__":
    target_time = idler.prompt_time()
    # Special-case to prefer using Twitch stream as they automatically play.
    target_url = idler.BASE_URL.format(league="worlds/riotgames")
    idler.run_loop(target_url=target_url, target_time=target_time)
