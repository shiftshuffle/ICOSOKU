from lib.dna import Generation
from lib.config_load import Value
import time
import os
import tqdm

base_dir = "./solutions"
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

filename = f"{base_dir}/A_{Value.A}-B_{Value.B}-C_{Value.C}-D_{Value.D}-E_{Value.E}-F_{Value.F}-G_{Value.G}-H_{Value.H}-I_{Value.I}-J_{Value.J}-K_{Value.K}-L_{Value.L}.txt"


def success(min_individual, start_time):
    print(min_individual)
    print(f"found in {time.time() - start_time} seconds")
    with open(filename, 'a') as f:
        f.write(str(min_individual))
        f.write("\n")
        f.write(f"found in {time.time() - start_time} seconds")
        f.write("\n")
        f.write(f"{'-' * 100}")
        f.write("\n")


start_time = time.time()
max_epochs = Value.max_epochs
epoch = Generation.populate(Value.population_number)

#print(epoch.population[0].gene)
#print(epoch.population[0].phenotype)

 with tqdm.tqdm(total=max_epochs, position=1) as pbar:
     for i in range(max_epochs):
         pbar.set_description_str(f'Current min score: {epoch.min_score}')
         if epoch.min_score == 0:
             success(epoch.min_individual, start_time)
             break
         else:
             epoch = epoch.update()
             pbar.update(1)
