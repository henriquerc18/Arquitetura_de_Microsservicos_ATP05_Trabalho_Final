## Instruções
### Atualizar pacotes Python (caso tenha instalado, previamente), baixar biblioteca e clonar gRPC
- python -m pip install --upgrade pip  
- python -m pip install grpcio grpcio-tools  
- git clone -b v1.72.0 --depth 1 --shallow-submodules https://github.com/grpc/grpc

### Definir estrutura de pastas
agenda-contatos/protos/contatos.proto  
agenda-contatos/server/server.py  
agenda-contatos/client/client.py  
agenda-contatos/requirements.txt  

### OBS: após o upload dos arquivos dentro da pasta "agenda-contatos", não foi possível visualizar as pastas internas e seus arquivos no repositório, por isso, coloquei-os direto na pasta raiz.
/protos/contatos.proto  
/server/server.py  
/client/client.py  
requirements.txt  

### Gerar os arquivos gRPC Python nas pastas /server e /client:
- python -m grpc_tools.protoc -I=protos --python_out=server --grpc_python_out=server protos/contatos.proto
- python -m grpc_tools.protoc -I=protos --python_out=client --grpc_python_out=client protos/contatos.proto

### Rodar o servidor
- python server/server.py

### Em outro terminal, rodar o cliente:
- python client/client.py


