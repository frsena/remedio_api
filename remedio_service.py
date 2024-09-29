
from flask_openapi3 import Tag
from sqlalchemy import and_

from model import Session, Remedio
from app import app
from schemas import *

remedio_tag = Tag(name="Remedio", description="Listar todos os remedios")


@app.get('/remedio', tags=[remedio_tag],
         responses={"200": RemedioSchema, "404": ErrorSchema})
def busca_id(query: PesquisaRemedioId):
    """ Busca o remedio pelo codigo
    """
    id = query.id
    session = Session()
    med = session.query(Remedio).filter(Remedio.id == id).first()

    if not med:
        error_msg = "Não foi encontrado nenhum remedio."
        return {"mesage": error_msg}, 404
    else :
        return remedio_view(med)


@app.get('/remedios', tags=[remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def busca_remedios():
    """ Retorna todos os remedios cadastrados
    """
    session = Session()
    remedios = session.query(Remedio).all()

    if not remedios:
        # se não há produtos cadastrados
        return [], 200
    else:
        return remedios_view(remedios), 200


@app.get('/pesquisa', tags=[remedio_tag],
         responses={"200": ListagemRemedioSchema, "404": ErrorSchema})
def pesquisa_remedio(query: PesquisaRemedio):
    """ pesquisa o remedio pelo codigo e pelo nome, caso não passe nenhum parametro retorna a lista toda
    """
    session = Session()
    filters = []
    print(query)
    if query.id:
        filters.append(Remedio.id == query.id)
    if query.nome:
        filters.append(Remedio.nome.ilike(f"%{query.nome}%"))
       
    remedio = session.query(Remedio).filter(and_(*filters)).all()

    if not remedio:
        error_msg = "Não foi encontrado nenhum medicamento."
        return {"mesage": error_msg}, 404
    else :
        return remedios_view(remedio), 200



@app.post('/remedio', tags=[remedio_tag],
         responses={"200": RemedioSchema, "400": ErrorSchema})
def adicionar(form: RemedioIncluirSchema):
    """ adiciona um remedio novo
    """
    print(form)
    remedio = Remedio(form.nome) 
    try:
        session = Session()
        session.add(remedio)
        session.commit()

        return remedio_view(remedio)
    
    except Exception as e:
        print(e)
        # caso um erro fora do previsto
        error_msg = "Não foi possível salvar novo remedio."
        return {"mesage": error_msg}, 400 
    


@app.put('/atualizar', tags=[remedio_tag],
         responses={"200": RemedioSchema, "400": ErrorSchema})
def atualizar(form: RemedioSchema):
    """ atualizar um medicamento cadastrado
    """
    id = form.id
    session = Session()
    remedio = session.query(Remedio).filter(Remedio.id == id).first()
    try:
    
        if not remedio:
            error_msg = "Não foi possível atualizar o medicamento."
            return {"mesage": error_msg}, 400
        
        print(remedio.id)
        remedio.nome = form.nome
        print(remedio.nome)
        session.add(remedio)
        session.commit()
        print("atualizar")
        return remedio_view(remedio)
        
    except Exception as e:
        # caso um erro fora do previsto
        error_msg = "Não foi possível atualizar o medicamento."
        return {"mesage": error_msg}, 400 

@app.delete('/deletar', tags=[remedio_tag],
         responses={"200": ErrorSchema, "404": ErrorSchema})
def deletar(query: PesquisaRemedioId):
    """ deletar um remedio cadastrado
    """
    id = query.id
    print(query)
    session = Session()
    count = session.query(Remedio).filter(Remedio.id == id).delete()
    session.commit()

    if count:
        msg = "Remedio foi excluido com sucesso."
        return {"mesage": msg}, 200
    else :
        error_msg = "Não foi encontrado nenhum remedio."
        return {"mesage": error_msg}, 404
    

