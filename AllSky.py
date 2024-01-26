import streamlit as st
from pathlib import Path
import asyncio
from datetime import datetime, timezone

PLACEHOLDER_URL = "https://www.gaithersburgdental.com/wp-content/uploads/2016/10/orionthemes-placeholder-image.png"

async def watch(image_pl):
    dir_path = "watch_dir"
    previous = None
    while True:
        images = list(Path(dir_path).glob("*.jpg"))
        if images:
            latest = max(images, key=lambda file: file.stat().st_mtime)
        else:
            image_pl.image(PLACEHOLDER_URL, use_column_width=True) #,
            latest = None
        if latest != previous:
            image_pl.image(str(latest), use_column_width=True,  caption='%s' % datetime.fromtimestamp(latest.stat().st_mtime, tz=timezone.utc))
            previous = latest
        _ = await asyncio.sleep(1)


image_pl = st.empty()

asyncio.run(watch(image_pl))
