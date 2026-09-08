# LinkedIn Featured tiles

Source for the Open Graph images at `/img/og/`. Each short URL (`/corporate`, `/holiday`, `/build`, `/meet`) is a one-file page that carries its tile as `og:image` and forwards to the destination with UTMs.

Rebuild: `python3 tiles/build.py` (needs Google Chrome; renders `tile*.html` at 2x, then writes the 1200x627 JPGs into `out/`). Copy `out/*.jpg` to `img/og/`. Copy is intentional so a rebuild never overwrites a live tile by accident.
