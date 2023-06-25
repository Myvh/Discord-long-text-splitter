# Discord long text splitter

A barebone graphic Python tool that splits long texts to fit the Discord message character limit, while preserving the text layout.

## Example screenshot

![Example_screenshot](https://github.com/Myvh/Discord-long-text-splitter/assets/68384832/4a36eb52-7ed1-47d6-b4d9-418abef0e8de)

## Features

- Splits text that is contained in the clipboard.
- Makes chunks at most 2000 characters long.
- Each chunk is copied in the clipboard by a single button click.
- The splitting points are chosen to be single newlines (newlines that are not next to another newline). This is because Discord trims leading and trailing newlines from messages, so splitting at a multiple newline makes it a single newline when sent.

## Improvement

I do not plan on improving this program. Feel free to adapt it to your use and/or enhance it for everybody.

## More info

See the comments in the source code.
