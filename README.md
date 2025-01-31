# 🌠 Fractals Generator

![Fractale générée](Ethereal_Mandala_6107.png)

---

## **Présentation du Projet**

Ce programme génère des représentations visuelles de l'ensemble de Mandelbrot, une structure mathématique emblématique des fractales. À partir d'une équation simple (`zₙ₊₁ = zₙ² + c`), il affiche des motifs géométriques complexes en haute résolution (8K).

---

## **Fonctionnement Technique**

### Algorithme Clé
```python
def compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    # Initialisation du plan complexe
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    c = x + y[:, None] * 1j  # Grille de nombres complexes
    z = np.zeros_like(c)
    divergence_map = np.zeros(c.shape, dtype=np.uint16)
    mask = np.ones(c.shape, dtype=bool)

    for _ in range(max_iter):
        z[mask] = z[mask]**2 + c[mask]  # Application de la formule
        mask = np.abs(z) < 4.0          # Condition de divergence
        divergence_map += mask          # Enregistrement des itérations
    
    return divergence_map
