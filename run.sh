# Este arquivo é responsável por executar o docker-compose.
# Defina os valores das variáveis que vão ser atribuidas ao docker-compose.
# Para criar as imagens e iniciar os containers, descomente a linha 11 e comente a linha 12.

export TAG_OPERATIONAL="tag_operational-2"
export CONTAINER_OPERATIONAL="container_operational-2"

export TAG_FINANCIAL="tag_financial-2"
export CONTAINER_FINANCIAL="container_financial-2"

#docker-compose up
docker-compose create