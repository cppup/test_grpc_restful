
- ./gen/XX 目录需要手工创建，protoc不自动创建；

```sh
python ./service/server.py   # 启动服务，端口 9090
python ./server/client.py  # 测试请求是否成功

go run ./proxy.go  # 启动 RESTful 代理
```
