# lolesports-idler

## Requirements
* Python 3.7+

## Run
For any events:

```sh
python3 idler.py
```

For Worlds:

```sh
python3 worlds.py
```

Twitch stream will be preferred when using `worlds.py`
as they play automatically upon being loaded. Unlike YouTube,
which may require users to click on the stream first.

## Usage

Enter the local time in 24-hour format without colons (HHMM). The first game of the day usually
doesn't start until about 15 minutes after the scheduled time.

To ensure that the stream will be loaded on lolesports.com, enter the time about 10 minutes
after the scheduled time. For example, if the game is scheduled to start at 1pm, you
may enter `1310`.

## URL schemas

### Schedule

```url
https://lolesports.com/schedule?leagues={league_id,league_id2,...}
```

Examples
* Schedule for MSI: `https://lolesports.com/schedule?leagues=msi`
* Schedule for Worlds and LCS: `https://lolesports.com/schedule?leagues=worlds,lcs`

### Livestream

```url
https://lolesports.com/live/{league_id}/{provider_id}
```

`provider_id` is optional. If empty, the website will choose one for you.

Do note that Twitch streams usually play automatically when opened, whereas YouTube requires you
to click on the video first.

This value depends on the stream provider. For Twitch, it is the channel ID. For YouTube, it is the video/stream ID.

Examples:
* Worlds stream: `https://lolesports.com/live/worlds`
  * The website will pick a stream provider for you, usually YouTube or based on
    previous preference.
* Worlds stream on Twitch `https://lolesports.com/live/worlds/riotgames`
  * International events are streamed on Riot Games' Twitch channel.
* Worlds stream on YouTube: `https://lolesports.com/live/worlds/u4vIEops3EM`
  * The YouTube link to this stream would be: `https://www.youtube.com/watch?v=u4vIEops3EM`
