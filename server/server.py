import grpc
from concurrent import futures
import time
import contatos_pb2
import contatos_pb2_grpc

# Armazenamento simples em memória
contatos_db = {}

class ContatoServiceServicer(contatos_pb2_grpc.ContatoServiceServicer):
    def AdicionarContato(self, request, context):
        nome = request.contato.nome
        contatos_db[nome] = request.contato
        return contatos_pb2.ContatoResponse(contato=request.contato, mensagem="Contato adicionado com sucesso!")

    def ConsultarContato(self, request, context):
        contato = contatos_db.get(request.nome)
        if contato:
            return contatos_pb2.ContatoResponse(contato=contato, mensagem="Contato encontrado.")
        else:
            return contatos_pb2.ContatoResponse(mensagem="Contato não encontrado.")

    def ListarContatos(self, request, context):
        return contatos_pb2.ListaContatosResponse(contatos=list(contatos_db.values()))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    contatos_pb2_grpc.add_ContatoServiceServicer_to_server(ContatoServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051.")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
