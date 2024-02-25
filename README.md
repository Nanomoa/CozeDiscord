<div align="center">

# CozeDiscord

A way to use ChatGpt4 for free by simulating communication behavior with CozeBot through a proxy Discord user.
---

</div>

## Description

CozeDiscord, a project that allows you to use `chatgpt4` for free. [Coze](https://coze.com/) is a project that allows us to use `chatgpt4` models for free. After creating a new bot in Coze, you can publish it to [Discord](https://discord.com/). At this point, we can then use the [discord.py](https://github.com/Rapptz/discord.py) repository to implement a `DiscordBot` that can create channels, send messages, and receive replies. We can then use this bot to send messages to the `CozeBot` and get replies from it, in order to use `chatgpt4` for free!

## Functionality

- [x] Create a new channel in the server
- [x] Send a message to `CozeBot` on the specified channel.
- [x] Support AI drawing
- [ ] Support for NextChat 
- [ ] Other (under development)

## Api Document

- **Create a new channel**
  > /api/channel/create
  
  _Request Methods_：`POST`

  _Parameters_:
  - Content-Type: application/json
  - Body:
    ```json
    {
      "channel_name": "test_channel"
    }
    ```

  _Example_:
  ```
  ~/CozeDiscord$ curl -X POST -H "Content-Type: application/json" -H "token: nanomoa" -d '{"channel_name": "test_channel"}' http://127.0.0.1:5000/api/channel/create
  {"code":1,"data":{"channel_id":1200000000000000053,"channel_name":"test_channel"},"message":"Create channel success."}
  ```

- **Delete channel**
  > /api/channel/delete
  
  _Request Methods_：`POST`

  _Parameters_:
  - Content-Type: application/json
  - Body:
    ```json
    {
      "channel_id": 1200000000000023
    }
    ```

  _Example_:
  ```
  ~/CozeDiscord$ curl -X POST -H "Content-Type: application/json" -H "token: nanomoa" -d '{"channel_id": 1200000000000023}' http://127.0.0.1:5000/api/channel/delete
  {"code":1,"message":"Delete channel success."}
  ```
  
- **Send a message and get a reply**
  > /api/chat/send
  
  _Request Methods_: `POST`

  _Parameters_:
  - Content-Type: application/json
  - Body:
    ```json
    {
      "channel_id": 1200000000000000086
      "message": "test"
    }
    ```

      _Example_:
  ```
  ~/CozeDiscord$ curl -X POST -H "Content-Type: application/json" -H "token: nanomoa" -d '{"channel_id":1200000000000000086,"message":"test"}' http://127.0.0.1:5000/api/chat/send
  {"code":1,"data":{"message":"Hello! How can I assist you today? If you need to test something or have any questions, feel free to ask."},"message":"Send message success."}
  ```

## Usage

1. Go to the Discord Developer Platform
2. Create a new app and copy the token.
3. Go to Coze
4. Create a new bot and install the `DALLE 3` plugin on it.
5. Publish the bot to Discord and add it to your server
6. Create a new Discord app and give it administrator rights.
7. Add it to your server
8. then configure the project's `config.yaml` file
9. Install all the libraries and run the project
10. After it finishes running you will see the command line output `Logged in as {your bot's name}`.

## People who starred this github repository!
[![Stargazers repo roster for @Nanomoa/CozeDiscord](https://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=Nanomoa&repo=CozeDiscord)](https://github.com/Nanomoa/CozeDiscord)

## Express gratitude (esp. in public)

**[Coze](https://coze.com/)**: Next-generation AI chatbot building platform.

**[Discord](https://discord.com/)**: A community for gaming, learning, music and more.

**[discord.py](https://github.com/Rapptz/discord.py)**: An API wrapper for Discord written in Python.
