import numpy as np

# Toprak ve bitki özelliklerinin tanımlanması
area = 20  # Bahçenin alanı (metrekare)
soil_type = "sandy"  # Toprak türü
plant_type = "tomato"  # Bitki türü

# Hedef fonksiyonun tanımlanması
def objective_function(x):
    # x[0] - su kaynağı
    # x[1] - sulama miktarı
    # x[2] - sulama sıklığı
    # x[3] - sulama süresi
    # x[4] - sulama bölgesi
    # x[5] - sulama yöntemi

    # Hedef fonksiyonu - Su tüketimini minimize ederek bitki büyümesini maksimize etmek
    water_consumption = x[1] * x[2] * x[3] * x[4] * x[5]
    plant_growth = x[1] * x[3] * x[4] * x[5]
    objective = -(plant_growth / water_consumption)
    return objective

# PSO algoritmasının tanımlanması
def pso(objective_function, bounds, num_particles, maxiter, c1, c2):
    # Partiküllerin başlangıç ​​pozisyonlarının belirlenmesi
    dimensions = len(bounds)
    x_min, x_max = np.asarray(bounds).T
    x_0 = np.random.rand(num_particles, dimensions)
    x_0 = x_min + x_0 * (x_max - x_min)

    # Başlangıç hızlarının belirlenmesi
    v_min = -abs(x_max - x_min)
    v_max = abs(x_max - x_min)
    v_0 = np.random.uniform(low=v_min, high=v_max, size=(num_particles, dimensions))

    # En iyi konumların ve uygunluk değerlerinin kaydedilmesi
    best_position = x_0.copy()
    best_fitness = [objective_function(x) for x in x_0]

def pso(objective_function, bounds, num_particles, maxiter, c1, c2):
    # En iyi konumların ve uygunluk değerlerinin kaydedilmesi
    dimensions = len(bounds)
    x_min, x_max = np.asarray(bounds).T
    x_0 = np.random.rand(num_particles, dimensions)
    x_0 = x_min + x_0 * (x_max - x_min)

    v_min = -abs(x_max - x_min)
    v_max = abs(x_max - x_min)
    v_0 = np.random.uniform(low=v_min, high=v_max, size=(num_particles, dimensions))

    best_position = x_0.copy()
    best_fitness = [objective_function(x) for x in x_0]

    global_best_position = best_position.copy()
    global_best_fitness = min(best_fitness)

    for i in range(maxiter):
        for j in range(num_particles):
            # Partikülün yeni hızı
            v_0 = v_0 + c1 * np.random.rand(dimensions) * (best_position - x_0) + c2 * np.random.rand(dimensions) * (global_best_position - x_0)

            # Partikülün yeni konumu
            x_0[j] = x_0[j] + v_0[j]

            # Sınırların dışına çıkmaması sağlanır
            x_0[j] = np.clip(x_0[j], x_min, x_max)

            # Partikülün uygunluk değeri
            fitness = objective_function(x_0[j])

            # En iyi konumların ve uygunluk değerlerinin güncellenmesi
            if fitness < best_fitness[j]:
                best_fitness[j] = fitness
                best_position[j] = x_0[j]

                if fitness < global_best_fitness:
                    global_best_fitness = fitness
                    global_best_position = x_0[j]

    return global_best_position, global_best_fitness

bounds = [(0, 100), (0, 50), (1, 7), (1, 24), (1, 10), (0, 1)]
num_particles = 50
maxiter = 100
c1 = 2
c2 = 2
global_best_position, global_best_fitness = pso(objective_function, bounds, num_particles, maxiter, c1, c2)
print("En iyi pozisyon: ", global_best_position)
print("En iyi uygunluk değeri: ", global_best_fitness)



