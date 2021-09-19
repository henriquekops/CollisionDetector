# CollisionDetector
A program for line collision detection using OpenGL

## Dependencies

On Windows:

```sh
make win
```

On Unix:
```
make unix
```

## Run

```sh
python main.py
```

## Runtime

Default mode is NAIVE, it will calculate LINESxLINES collisions:

- Press 'a' to use AABB mode
- Press 's' to use Regular Subdivision mode
- Press 'n' to return to NAIVE mode
- Press 'spacebar' to generate a new data set (will keep chosen detection mode)
