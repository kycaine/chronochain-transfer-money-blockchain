# Project Structure
```text
chronochain/
├── api/            
│   ├── router.go
│   ├── transaction_handler.go
│   ├── node_handler.go
│   └── reward_handler.go
│
├── src/           
│   ├── models/               
│   │   ├── block.go          
│   │   ├── transaction.go    
│   │   ├── node.go           
│   │   └── reward.go         
│   │
│   ├── services/             
│   │   ├── blockchain_service.go
│   │   ├── transaction_service.go
│   │   ├── node_service.go
│   │   └── reward_service.go
│   │
│   ├── rewards/              
│   │   ├── pool.go
│   │   └── distribution.go
│   │
│   ├── config/               
│   │   └── config.go
│   │
│   └── utils/                
│       └── logger.go
│
├── tests/                    
│   ├── block_test.go
│   ├── transaction_test.go
│   ├── node_test.go
│   └── reward_test.go
│
├── cmd/
│   ├── api/                  
│   │   └── main.go
│   └── cli/                 
│       └── main.go
│
├── go.mod
└── go.sum

```

