package network

import (
	. "chat_server_golang/types"
	"log"
	"time"
	"net/http"
	"github.com/gin-gonic/gin"
	"github.com/gorilla/websocket"
)

var Upgrader = &websocket.Upgrader{ReadBufferSize: SocketBufferSize, WriteBufferSize: MessageBufferSize, CheckOrigin: func(r *http.Request) bool {return true}}


type Room struct {
	Forward chan *message // 수신되는 메시지를 보관하는 값
	// 들어오는 메시지를 다른 클라이언트들에게 전송을 합니다.

	Join chan *client // Socket이 연결되는 경우에 적용
	Leave chan *client // Socket이 끊어지는 경우에 대해서 적용

	Clients map[*client]bool // 현재 방에 있는 Client 정보를 저장
}

type message struct {
	Name    string
	Message string
	Time    int64
}

type client struct {
	Send   chan *message
	Room   *Room
	Name   string
	Socket *websocket.Conn
}

func NewRoom() *Room {
	return &Room{
		Forward: make(chan *message),
		Join: make(chan *client),
		Leave: make(chan *client),
		Clients: make(map[*client]bool),
	}
}

func (c *client) Read() {
	// 클라이언트가 들어오는 메시지를 읽는 함수
	defer c.Socket.Close()
	for {
		var msg *message
		err := c.Socket.ReadJSON(&msg)
		if err != nil {
			// 에러로그 뜨는 것 방지 (클로즈가 되었는데도 채널이 들어와서 처리를 해줘야 된다거나 그런 오류)
			// 클로즈가 된 에러이면...
			if !websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway) {
				break
			} else {
				panic(err)
			}
		} else {
			log.Println("READ : ", msg, "client", c.Name)
			log.Println()
			msg.Time = time.Now().Unix()
			msg.Name = c.Name

			c.Room.Forward <- msg
		}
	}
}

func (c *client) Write() {
	// 클라이언트가 메시지를 전송하는 함수
	defer c.Socket.Close()

	for msg := range c.Send {
		log.Println("WRITE : ", msg, "client", c.Name)
		log.Println()
		err:= c.Socket.WriteJSON(msg)
		if err != nil {
			panic(err)
		}
	}
}

func (r *Room) RunInit(){
	// Room에 있는 모든 채널값들을 받는 역할
	for {
		select {
		case client:= <- r.Join:
			r.Clients[client] = true
		case client:= <- r.Leave:
			r.Clients[client] = false
			close(client.Send)
			delete(r.Clients, client)
		case msg:= <- r.Forward:
			for client := range r.Clients {
				client.Send <- msg
			}
		}
	}
}

// 웹소켓 패키지에서 제공해주는 업그레이더를 사용해서 HTTP 통신을 소켓 통신으로 변환해줌.
func (r *Room) SocketServe(c *gin.Context) {
	socket, err := Upgrader.Upgrade(c.Writer, c.Request, nil)
	if err != nil {
		panic(err)
	}

	// 프론트에서 보내주는 쿠키를 가져옴
	userCookie, err := c.Request.Cookie("auth")
	if err!= nil {
		panic(err)
	}

	// userCookie.Value를 통해서 유저에 대한 네이밍 가져올 것

	client := &client{
		Socket: socket,
		Send: make(chan *message, MessageBufferSize),
		Room: r,
		Name: userCookie.Value,
	}

	r.Join <- client

	defer func() {r.Leave <- client} () // 함수가 벗어나는 걸 진행하기 직전에 이 defer가 동작

	go client.Write()

	client.Read()

	log.Println("여기가 마지막 로직")
}