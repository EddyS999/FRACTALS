#Author : EDDY DAMEN

import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib.colors import PowerNorm
from tqdm import tqdm

"""
Feel free to use it, improve it like you want 
"""

def compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Compute the Mandelbrot set using an optimized approach with NumPy arrays,
    while displaying a progress bar for iteration count.
    """
    x = np.linspace(xmin, xmax, width, dtype=np.float32)
    y = np.linspace(ymin, ymax, height, dtype=np.float32)
    
    c = x + y[:, None] * 1j
    
    z = np.zeros_like(c, dtype=np.complex64)
    
    mandel = np.zeros(c.shape, dtype=np.uint16)
    
    mask = np.ones(c.shape, dtype=bool)
    
    #z = z² + c
    for i in tqdm(range(max_iter), desc="Computing Mandelbrot"):
        z[mask] = z[mask]**2 + c[mask]
        mask = np.abs(z) < 4.0
        mandel += mask
    
    return mandel

fractal_adjectives = [
    "Celestial", "Chaotic", "Ethereal", "Quantum", "Cosmic",
    "Hypnotic", "Infinite", "Luminous", "Mystic", "Nebular"
]
fractal_nouns = [
    "Vortex", "Mandala", "Abyss", "Tessellation", "Infinity",
    "Spiral", "Echo", "Nexus", "Matrix", "Continuum"
]

def generate_fractal_name():
    """generate a nama for each fractals"""
    adj = random.choice(fractal_adjectives)
    noun = random.choice(fractal_nouns)
    num = random.randint(1000, 9999)
    return f"{adj}_{noun}_{num}"

# 8K param
WIDTH, HEIGHT = 7680, 4320
DPI = 300

def pick_luminous_cmap():
    """
    Return a colormap known for bright, luminous gradients.
    """
    luminous_cmaps = ["inferno", "plasma", "magma", "cividis", 
                      "turbo", "viridis", "hot", "afmhot"]
    return plt.get_cmap(random.choice(luminous_cmaps))

def generate_random_mandelbrot(width=WIDTH, height=HEIGHT, dpi=DPI, max_tries=5):
    """
    Generate and save a Mandelbrot fractal image with luminous colormaps.
    Retries up to `max_tries` times if the fractal is too uniform.
    """
    for attempt in range(max_tries):
        cmap = pick_luminous_cmap()
        
        zoom = random.uniform(1, 2000)
        max_iter = int(min(5000, 200 + zoom * 2))
        
        max_iter = 150  
        
        
        interesting_regions = [
            (-0.75,  0.1,   0.1),   # Main cardioid region
            (-1.77,  0,     0.01),  # Seahorse valley
            (0.3,    0.6,   0.004), # Elephant valley
            (-0.16,  1.04,  0.01)   # Triple spiral
        ]
        if random.random() > 0.2:
            cx, cy, spread = random.choice(interesting_regions)
            cx += random.uniform(-spread, spread)
            cy += random.uniform(-spread, spread)
        else:
            cx = random.uniform(-2.0, 1.0)
            cy = random.uniform(-1.5, 1.5)

        
        aspect_ratio = width / height
        region_size = 3.0 / zoom
        
        if random.random() > 0.5:
            x_size = region_size * aspect_ratio
            y_size = region_size
        else:
            x_size = region_size
            y_size = region_size / aspect_ratio
        
        xmin = cx - x_size/2
        xmax = cx + x_size/2
        ymin = cy - y_size/2
        ymax = cy + y_size/2
        
        mandel = compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
        
        #Sometimes, The image is uniform.
        #The porpose here, is to try until it works.
        data_min, data_max = mandel.min(), mandel.max()
        if data_min == data_max:
            print(f"[Attempt {attempt+1}] Fractal is uniform (all {data_min}). Retrying...")
            continue
        
        
        fig = plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)
        plt.axis('off')
        
        vmin, vmax = float(data_min), float(data_max)
        
        gamma_choices = [0.3, 0.5, 0.7, 0.9, 1.0]
        gamma = random.choice(gamma_choices)
        
        plt.imshow(
            mandel,
            cmap=cmap,
            norm=PowerNorm(gamma, vmin=vmin, vmax=vmax),
            origin='lower',
            extent=(xmin, xmax, ymin, ymax)
        )
        
        fractal_name = generate_fractal_name()
        plt.savefig(f"{fractal_name}.png", bbox_inches='tight', pad_inches=0, dpi=dpi)
        plt.close()
        
        print(f"[Attempt {attempt+1}] Fractal saved as {fractal_name}.png")
        return  #We quit right after the fractal is correctly generated 
    
    print("All attempts resulted in uniform fractals. Try again later!")

if __name__ == "__main__":
    generate_random_mandelbrot()
