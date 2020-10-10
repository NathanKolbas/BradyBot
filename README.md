# BradyBot

## About
The BradyBot was developed by Nathan Kolbas and is currently in use in our software engineering Discord server. It is mainly used for jokes and memes but can become much more. It was originally built with node.js but migrated over to python before release. 

## Features
The BradyBot's main feature is the ability to @ any user in the Discord which will then take their profile image and overlay it onto an Among Us gif. The overlaid image is also moving each frame. More features to be added in the future such as reading a random Brady quote or adding a new one.

## Getting started
#### Installing
To install the required dependencies, simply run the command `pip install -r requirements.txt`.

#### Setup
Create a `config.json` file in the root directory of the project. This will story secrets used by the bot.  Example `config.json` file:
```json
{
    "BOT_TOKEN": "bot_token",
    "GIS_DEV_API_KEY": "gis_api",
    "GIS_PROJECT_CX": "cx_project"
}
```
The `BOT_TOKEN` is your Discord API key. Both `GIS_DEV_API_KEY` and `GIS_PROJECT_CX` are for Google image searching. Documentation for how to setup image search keys can be found [here](https://github.com/arrrlo/Google-Images-Search).

## Documentation
After adding the BradyBot to your Discord server, you can run the following commands:
  - `BradyBot execute @UserName`
    - Overlays the user profile icon, or image search, in an Among Us gif. The student being executed after one of Brady's clever questions  
    ![example gif](Examples/example.gif)
  - `BradyBot kd|kills|executions|kill-count`
    - Tells you how many people Brady has executed
  - `BradyBot quote` (TODO)
    - Reads a random quote from the BradyDatabase
    - Optionally you can specify the line of the quote (e.g.`BradyBot quote 1`)
  - `BradyBot quote-all`
    - Shows all the quotes
  - `BradyBot add quote quote_text`
    - Add a quote to the BradyDatabase
  - `BradyBot remove-quote quote_line`
    - Removes a quote by the line. Requires Administrator permission to do so.
  - `BradyBot help`
    - Help and commands for the BradyBot

## Contributing
Pull request are more than welcome. Feel free to contribute or fork the project for your own needs.
