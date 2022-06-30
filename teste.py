variavel = {"id": 11, 
            "velocidade_rolo": 3.87, 
            "velocidade_esteira": 16.08, 
            "timestamp": "2022-05-21T01:45:33.000Z", 
            "detalhes": [
                {"id": 667, "velocidade_rolo": 2.2, "velocidade_esteira": 7.25, "esteira_id": 11}, 
                {"id": 668, "velocidade_rolo": 20.72, "velocidade_esteira": 10.65, "esteira_id": 11},
                {"id": 669, "velocidade_rolo": 18.64, "velocidade_esteira": 12.35, "esteira_id": 11}
            ],
            "id": 11, 
            "velocidade_rolo": 3.88, 
            "velocidade_esteira": 15.08, 
            "timestamp": "2022-05-21T01:45:40.000Z", 
            "detalhes": [
                {"id": 670, "velocidade_rolo": 2.2, "velocidade_esteira": 7.25, "esteira_id": 11}, 
                {"id": 671, "velocidade_rolo": 20.72, "velocidade_esteira": 10.65, "esteira_id": 11},
                {"id": 672, "velocidade_rolo": 18.64, "velocidade_esteira": 12.35, "esteira_id": 11}
            ]
           }

print(variavel)
print(type(variavel))
print("velocidade de esteira: ",variavel['detalhes'][1]['velocidade_esteira'])
detalhe = variavel["detalhes"]
print("velocidade do rolo   : ",detalhe[1]['velocidade_rolo'])
print("Tamanho da variavel =",len(variavel))