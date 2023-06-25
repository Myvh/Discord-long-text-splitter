## Info

# Made by Myvh on 2023 June.

# This little program splits the given text into chunks at most `maxLength` long, with the added condition that the splitting points have to be single newlines (newlines that are not next to another newline).
# This is because Discord trims leading and trailing newlines from messages, so splitting at a multiple newline makes it a single newline when sent.

## Text splitting

def rightTrim(text, toBeTrimmed):
    while text.endswith(toBeTrimmed):
        text = text[:-len(toBeTrimmed)]
    return text

def splittingIndex(text, maxLength, newline):
    if len(text) <= maxLength:
        return(len(text))
    remainingText = text[:maxLength+2*len(newline)]
    while True:
        possibleIndex = remainingText.rindex(newline)
        remainingText = remainingText[:possibleIndex]
        if remainingText.endswith(newline):
            remainingText = rightTrim(remainingText, newline)
        elif possibleIndex <= maxLength:
            return possibleIndex

def split(text, maxLength, newline):
    splittedText = []
    while text != "":
        currentSplittingIndex = splittingIndex(text, maxLength, newline)
        splittedText.append(text[:currentSplittingIndex])
        text = text[currentSplittingIndex+len(newline):]
    return splittedText

## Graphical interface

import tkinter
import tkinter.font

# Constants

messageMaxLength = 2000
newlineSeparator = "\n"

previewLength = 50
textLengthDisplayDigits = 5
chunkIndexDisplayDigits = 2
chunkLengthDisplayDigits = 4
copyChunkButtonCounterDisplayDigits = 2

windowWidth = 1450
separatorLine = "—"*10
fontFamily = "Liberation Mono"
fontSize = 15

# General setting

window = tkinter.Tk()
window.title("Discord long text splitter")

tkinter.font.nametofont("TkDefaultFont").configure(family=fontFamily, size=fontSize)

def restoreWindowWidth():
    window.update() # needed for `winfo_height` not to return an outdated value
    window.geometry("{}x{}".format(windowWidth, window.winfo_height()))

# Splitting and copying

textLengthLabel = tkinter.Label()
numberOfChunksLabel = tkinter.Label()

splittedText = []
noCopyChunkButtonLabel = tkinter.Label(text="[Nothing to copy yet]")
copyChunkButtons = [noCopyChunkButtonLabel]
copyChunkButtonCounters = []

def clearCopyChunkButtons():
    for CCB in copyChunkButtons:
        CCB.destroy()
    copyChunkButtons.clear()
    copyChunkButtonCounters.clear()

def preview(text):
    flattenedText = text.replace("\n", " | ").replace("\t", "  ")
    result = "“" + flattenedText[:previewLength]
    if len(flattenedText) > previewLength:
        result += "…"
    result += "”"
    result = result.ljust(previewLength+3)
    return result

def replaceClipboard(text):
    window.clipboard_clear()
    window.clipboard_append(text)

def copyChunkButtonText(chunkIndex):
    return "#" + str(chunkIndex).zfill(chunkIndexDisplayDigits) + "   —   Length: " + str(len(splittedText[chunkIndex])).zfill(chunkLengthDisplayDigits) + "   —   Preview: " + preview(splittedText[chunkIndex]) + "   —   Copied: " + str(copyChunkButtonCounters[chunkIndex]).zfill(copyChunkButtonCounterDisplayDigits) + " time·s"

def handleCopyChunkButton(chunkIndex):
    global copyChunkButtonCounters
    copyChunkButtonCounters[chunkIndex] += 1
    copyChunkButtons[chunkIndex]["text"] = copyChunkButtonText(chunkIndex)
    replaceClipboard(splittedText[chunkIndex])

def updateInfoLabels(textLength, numberOfChunks):
    textLengthLabel["text"] = " "*5 + "Text length: {} character·s".format(str(textLength).zfill(textLengthDisplayDigits))
    numberOfChunksLabel["text"] = "Number of chunks: {}".format(str(numberOfChunks).zfill(chunkIndexDisplayDigits)) + " "*15

def handleSplit():
    clipboardText = window.clipboard_get()
    global splittedText, copyChunkButtonCounters
    clearCopyChunkButtons()
    window.geometry("")
    splittedText = split(clipboardText, messageMaxLength, newlineSeparator)
    copyChunkButtonCounters = [0] * len(splittedText)
    updateInfoLabels(len(clipboardText), len(splittedText))
    for chunkIndex in range(len(splittedText)):
        newCopyChunkButton = tkinter.Button(text=copyChunkButtonText(chunkIndex))
        newCopyChunkButton["command"] = lambda storedChunkIndex=chunkIndex : handleCopyChunkButton(storedChunkIndex) # argument default value trick that prevents these lambda functions from all using the last value of `chunkIndex`
        newCopyChunkButton.pack()
        copyChunkButtons.append(newCopyChunkButton)
    restoreWindowWidth()

splitButton = tkinter.Button(text="Split text from clipboard", command=handleSplit)

updateInfoLabels("-"*textLengthDisplayDigits, "-"*chunkIndexDisplayDigits)

copyChunkLabel = tkinter.Label(text="Copy chunks to clipboard:")

# Display

def packSeparatorLine():
    tkinter.Label(text=separatorLine).pack()

window.geometry("")

splitButton.pack()
packSeparatorLine()
textLengthLabel.pack()
numberOfChunksLabel.pack()
packSeparatorLine()
copyChunkLabel.pack()
noCopyChunkButtonLabel.pack()

restoreWindowWidth()

window.mainloop()
