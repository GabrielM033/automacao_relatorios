# Arquivo responsável por enviar as imagens criadas para o Docker Hub.
# Use o mesmo nome dado a tag quando construiu as imagens no arquivo: run.sh.

export TAG_OPERATIONAL="tag_operational-1"
export TAG_FINANCIAL="tag_financial-1"


docker tag $TAG_OPERATIONAL gabrielmoreira033/reports-automation:$TAG_OPERATIONAL
docker push gabrielmoreira033/reports-automation:$TAG_OPERATIONAL

docker tag $TAG_FINANCIAL gabrielmoreira033/reports-automation:$TAG_FINANCIAL
docker push gabrielmoreira033/reports-automation:$TAG_FINANCIAL