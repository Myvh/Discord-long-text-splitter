# Discord long text splitter

A barebone graphic Python tool that splits long texts to fit the Discord message character limit, while preserving the newlines.

## Example screenshot

![Example_screenshot](https://github.com/Myvh/Discord-long-text-splitter/assets/68384832/4a36eb52-7ed1-47d6-b4d9-418abef0e8de)

## Features

- Splits text that is contained in the clipboard.
- Makes chunks at most 2000 characters long.
- Each chunk is copied in the clipboard by a single button click.
- The splitting points are chosen to be single newlines (newlines that are not next to another newline). This is because Discord trims leading and trailing newlines from messages, so splitting at a multiple newline makes it a single newline when sent.

## Non-feature

- This tool does **not** handle the code blocks made with ` ``` `, it can split inside them and thus break their formatting.

## Improvement

I do not plan on improving this program. Feel free to adapt it to your use and/or enhance it for everybody.

## More info

See the source code.

---

## We’re Using GitHub Under Protest

This project is currently hosted on GitHub.  This is not ideal; GitHub is a
proprietary, trade-secret system that is not Free and Open Souce Software
(FOSS).  We are deeply concerned about using a proprietary system like GitHub
to develop our FOSS project. We urge you to read about the
[Give up GitHub](https://GiveUpGitHub.org) campaign from
[the Software Freedom Conservancy](https://sfconservancy.org) to understand
some of the reasons why GitHub is not a good place to host FOSS projects.

Any use of this project’s code by GitHub Copilot, past or present, is done
without our permission.  We do not consent to GitHub’s use of this project’s
code in Copilot.

![Logo of the GiveUpGitHub campaign](https://sfconservancy.org/img/GiveUpGitHub.png)
