# CollisionDetector
Um programa para detecção de colisão em linhas usando OpenGL
## Dependencias

No Windows:

```sh
make win
```

No Unix:
```
make unix
```

## Execução

```sh
python main.py < n > < xDiv > < yDiv >

- n: Tamanho do universo da matriz da subdivisão regular
- xDiv: Divisões no eixo X sobre o universo da subdivisão regular
- yDiv: Divisões no eixo Y sobre o universo da subdivisão regular
Esses parametros devem ser inseridos independente da solução escolhida pois a definição dessa será feita durante a execução (vid sessão abaixo)
```

## Runtime

Modo padrão é Ingênua, este calcula a colisão LINHAxLINHA:

- Pressione 'a' para usar o modo AABB
- Pressione 's' para usar o modo Subdivisão Regular
- Pressione 'n' para returnar ao modo Ingênuo
- Pressione 'spacebar' para gerar um novo data set (irá manter modo de detecção selecionado)
