const express = require("express");
const http = require("http");
const cors = require("cors");
const Websocket = require("ws");
const { SocketLogger } = require("./logs/winston");
const { NewRoom } = require("./types/Room");

// const app = express();

// app.use(
//   cors({
//     origin: "*",
//   })
// );

// app.use(express.json());
// app.use(express.urlencoded({ extended: false }));

const server = http.createServer();
const wss = new Websocket.Server({ server });

const room = NewRoom();

// ws : 웹소켓 객체, req : 쿠키 값이나 추가적인 정보값이 담겨있음
wss.on("connection", (ws, req) => {
  // Cookie에서 user 정보 가져오기

  // console.log(cookie);
  const cookie = req.headers.cookie;
  const [_, user] = cookie.split("=");

  // console.log(user);
  room.join(ws);

  ws.on("message", (msg) => {
    // message가 들어오면 해당 메시지를 다른 client에도 브로드 캐스팅

    // console.log("msg", msg);

    const jsonMsg = JSON.parse(msg);
    jsonMsg.Name = user;

    room.forwardMessage(jsonMsg);
  });

  ws.on("close", () => {
    // client 접속이 끊기면, client 제거
    // console.log("close");
    room.leave(ws);
  });
});

const PORT = process.env.PORT || 8080; // env 경로가 없을 시 디폴트로 8080
server.listen(PORT, () => {
  SocketLogger.info(`Server Started on Port = ${PORT}`);
});
