import matplotlib.pyplot as plt
import numpy as np


MAX_DISTANCE = 1e10
GRID_SIZE = 128
N_SEEDS = 8


def jump_flood(grid, seeds):
    step = int(max(grid.shape) / 2)

    while step >= 1:
        # Random iterative scheme to simulate parallel GPU computations
        indexes = list(np.ndindex(grid.shape[0], grid.shape[1]))
        np.random.shuffle(indexes)
        for i, j in indexes:
            best_dist = grid[i, j, 1]

            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ii = i + di*step
                    jj = j + dj*step

                    # Neighbor out of bounds
                    if not (0 <= ii < grid.shape[0]) or not (0 <= jj < grid.shape[1]):
                        continue

                    # Neighbor has not been set
                    if grid[ii, jj, 1] == MAX_DISTANCE:
                        continue

                    # Compute the distance with the seed saved by neighbor
                    seed_idx = grid[ii, jj, 0]
                    seed_i, seed_j = seeds[seed_idx]
                    dist = (i - seed_i)**2 + (j - seed_j)**2
                    if dist < best_dist:
                        grid[i, j] = [seed_idx, dist]
                        best_dist = dist

        step = int(step / 2)

    return grid


if __name__ == '__main__':
    # Create grid containing at each position:
    # - seed index of nearest seed
    # - distance to nearest seed
    grid = np.zeros((GRID_SIZE, GRID_SIZE, 2), dtype=int)
    grid[..., 1] = MAX_DISTANCE

    # Draw random seeds
    seeds = np.random.randint(0, GRID_SIZE, (N_SEEDS, 2))
    for i, (x, y) in enumerate(seeds):
        grid[x, y] = [i, 0]

    grid = jump_flood(grid, seeds)

    # Display seed index
    grid[seeds[:,0], seeds[:,1], 0] = -1
    plt.imshow(grid[..., 0])
    plt.show()
