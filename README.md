#Icosoku genetic solver

a genetic python solver for the [icosoku puzzle]()
the config.yml file contains the information of the pins
following the convention in this [constraint based solver ](https://www.nearly42.org/games/icosoku-solver/)

an Individual.gene might look like this
```python
[(4, 1), (0, 2), (11, 1), (13, 2), (17, 1), (10, 0), (14, 0), (1, 1), (16, 0), (5, 0), (6, 1), (3, 2), (7, 1), (9, 0), (12, 1), (19, 2), (2, 2), (8, 2), (15, 0), (18, 1)]
```

for the first tuple (4,1) this means go to Value.triangles and get the index 4 triange tile
and then rotate it 1

the corresponding Individual.phenotype then should look like
```python
[(0, 0, 0), (3, 1, 2), (3, 3, 0), (0, 1, 2), (2, 0, 2), (1, 1, 1), (3, 3, 3), (0, 2, 1), (1, 0, 2), (1, 3, 2), (0, 0, 1), (0, 1, 1), (2, 2, 2), (2, 1, 0), (2, 3, 1), (2, 0, 1), (2, 0, 0), (2, 1, 3), (2, 0, 1), (0, 0, 3)]
```

from which the score and fitness are calculated
(if you lay out the faces in a predetermined order you could count the errors)

---------


this project uses tqdm and yaml

```bash
python3 -m venv icoenv
source icoenv/bin/activate
pip install -r requirements.txt
```