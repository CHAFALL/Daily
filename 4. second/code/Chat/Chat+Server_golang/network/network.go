package network

import (
	"log"
	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
)

type Network struct{
	engin *gin.Engine
}

func NewServer() *Network {
	n := &Network{
		engin: gin.New()}

		n.engin.Use(gin.Logger())
		n.engin.Use(gin.Recovery()) // 에러 로그가 뜨더라도 서버가 죽지 않도록
		n.engin.Use(cors.New(cors.Config{
			AllowWebSockets: true,
			AllowOrigins: []string{"*"},
			AllowMethods: []string{"GET", "POST", "PUT"},
			AllowHeaders: []string{"*"},
			AllowCredentials: true,
		}))

		r := NewRoom()
		go r.RunInit() // 고루틴 방식으로 go가 붙은 코드 같은 경우에는 백그라운드에서 동작을 하라는 뜻
		// 예를 들어서 무한 루프가 돌아가는 함수가 있다면 이 함수가 실행이 됨으로써 아래로 못 내려오는데 근데 go를 이용해서 그걸 백그라운드에서 동작을 하게 하면 그 아래로 내려갈 수 있도록 함. 

		n.engin.GET("/room", r.SocketServe)

		return n
}

func (n *Network) StartServer() error {
	log.Println("Starting server")
	
	return n.engin.Run(":8080")
}