import grpc
import contatos_pb2
import contatos_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = contatos_pb2_grpc.ContatoServiceStub(channel)

    # Adicionar um contato
    contato = contatos_pb2.Contato(
        nome="Henrique Rosa",
        telefones=[
            contatos_pb2.Telefone(numero="51998765432", tipo=contatos_pb2.MOVEL),
            contatos_pb2.Telefone(numero="5133245678", tipo=contatos_pb2.FIXO)
        ],
        categoria=contatos_pb2.PESSOAL
    )
    response = stub.AdicionarContato(contatos_pb2.ContatoRequest(contato=contato))
    print(response.mensagem)

    # Consultar contato
    consulta = stub.ConsultarContato(contatos_pb2.ConsultaRequest(nome="Henrique Rosa"))
    print(f"Consulta: {consulta.contato.nome}, Telefones: {[t.numero for t in consulta.contato.telefones]}")

    # Listar todos os contatos
    lista = stub.ListarContatos(contatos_pb2.Empty())
    print("Lista de contatos:")
    for c in lista.contatos:
        print(f"- {c.nome} ({contatos_pb2.CategoriaContato.Name(c.categoria)})")

if __name__ == '__main__':
    run()
