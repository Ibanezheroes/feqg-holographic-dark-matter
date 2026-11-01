# Holographic ER=EPR Tensor Networks & Galactic Kinematics

### Discrete Numerical Simulator & Empirical Verification of Fractal Entanglement Quantum Gravity (FEQG)

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![arXiv](https://img.shields.io/badge/arXiv-2607.26035-b31b1b.svg)](https://arxiv.org/abs/2607.26035)

This repository provides an open-source, discrete numerical simulation engine testing the **Fractal Entanglement Quantum Gravity (FEQG)** framework formulated by **Jaume Giné (2026)** against high-precision empirical galactic rotation curves from the **SPARC (Spitzer Photometry & Accurate Rotation Curves)** database.

It addresses an explicit open frontier highlighted in Giné (2026): translating the continuous, analytical formulations of informational quantum gravity and non-local entanglement into discrete, falsifiable graph-theoretic models.

---

## 🔬 Theoretical Foundations

In *"Quantum Gravity from Fractal Entanglement Geometry"* ([arXiv:2607.26035](https://arxiv.org/abs/2607.26035)), Giné posits that classical spacetime, quantum mechanics, and gravitation emerge from the entanglement architecture of a universal quantum state:

1. **Relational Distance Metric:** Spatial metric separation $d_{ij}$ is derived directly from bipartite mutual information $I_{ij}$:
   $$d_{ij} = -l_0 \ln\left(\frac{I_{ij}}{I_0}\right)$$
   Strongly entangled subsystems establish immediate geometric proximity, while weakly correlated modes recede into macroscopic distance.

2. **Master Field Equation & Informational Stress Tensor:** Macroscopic gravitational dynamics incorporate matter alongside entanglement curvature and fractal dimensional corrections:
   $$G_{\mu\nu} = 8\pi G \left( T_{\mu\nu} + \alpha E_{\mu\nu} + \beta F_{\mu\nu} \right)$$
   where the informational stress tensor $E_{\mu\nu} \sim \nabla_\mu \nabla_\nu S_{\mathrm{ent}} - g_{\mu\nu}\Box S_{\mathrm{ent}}$ sources emergent gravitational backreaction without non-baryonic particle relics.

3. **Discrete Ryu–Takayanagi (RT) Formula:** Discretizing 2D spatial manifolds into hyperbolic tensor graphs, the holographic entanglement entropy of a boundary disk subregion $A$ is solved via minimal cut surfaces $\gamma_A$:
   $$S(A) = \min_{\gamma_A} \sum_{e \in \gamma_A} \ln(\chi_e) = \frac{\mathrm{Area}(\gamma_A)}{4 G \hbar}$$

4. **ER=EPR Bridge Defect Superposition:** Non-local chordal wormhole defects (Planckian ER bridges) with spatial probability $P(r_i, r_j) \propto |r_i - r_j|^{-\gamma}$ yield an emergent circular velocity:
   $$v_c^2(r) = r \frac{\partial \Phi_{\mathrm{eff}}}{\partial r} = v_{\mathrm{bary}}^2(r) + v_{\mathrm{ER}}^2(r)$$
   In the deep low-acceleration regime ($a_{\mathrm{bary}} \ll a_0$), this boundary cut naturally reproduces flat velocity plateaus and the Baryonic Tully–Fisher Relation ($v_c^4 \approx G M_{\mathrm{bary}} a_0$).

---

## 💻 Simulation Pipeline Architecture

The computational engine (`feqg_sparc_pipeline.py`) executes a 5-stage numerical pipeline:

```
+-------------------------------------------------------------+
| 1. Hyperbolic Lattice Generation (NetworkX, SciPy Sparse)   |
|    Poincaré disk tessellation discretizing spatial slices   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 2. Baryonic Seeding & Mass Potential Injection              |
|    SPARC gas + disk + bulge profiles & stellar M/L (Υ_★)    |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 3. ER Defect Superposition (Giné Metric Scaling)            |
|    Power-law chordal edges weighted via d_ij = -l_0 ln(I/I0)|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 4. Max-Flow / Min-Cut Solver (Push-Relabel Algorithm)        |
|    Solves extremal cuts γ_A to compute S_ent(r)             |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 5. Kinematic Differentiation & Goodness-of-Fit Evaluation    |
|    g_eff = -grad Φ_eff -> circular velocity v_c(r) & χ_ν^2  |
+-------------------------------------------------------------+
```

---

## 📊 Empirical Results & SPARC Catalog Benchmark

The model was tested against high-precision rotation curves from the SPARC database ($N = 171$ qualifying galaxies, $N_{\mathrm{points}} = 3375$ discrete kinematic measurements).

### Comparative Framework Assessment

| Theoretical Framework | Dark Sector Mechanism | Free Parameters | Median $\chi_\nu^2$ | Cusp-Core Problem | Physical Origin |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Baryons Only** | None (Newtonian) | 1 ($\Upsilon_\star$) | > 45.0 | N/A | Fails outer flat plateau |
| **$\Lambda\text{CDM}$ (NFW)** | Cold Dark Matter Particle | 3 ($\Upsilon_\star, M_{200}, c_{200}$) | 2.8 – 3.5 | Severe ($\rho \propto r^{-1}$) | Empirical halo fitting function |
| **MOND** | Modified Inertia / Gravity | 2 ($\Upsilon_\star, a_0$) | 3.6 – 4.1 | Resolved | Empirical acceleration scale |
| **FEQG Tensor Net (This Work)** | **Informational Defects ($E_{\mu\nu}$)** | **2 ($\Upsilon_\star, a_{0,\mathrm{eff}}$)** | **3.97** | **Resolved** | **First-principles bulk min-cut** |

> *Note on astrophysical notation:* **$\Upsilon_\star$** (*Upsilon star*) denotes the stellar mass-to-light ratio ($M_\star / L_\star$ in solar units $M_\odot / L_\odot$), converting observed 3.6 $\mu$m Spitzer photometry into baryonic stellar mass.

### Key Benchmark Galaxy Fits

* **NGC 3198 (Classic Spiral):** $\chi_\nu^2 = 2.69$
* **NGC 6503 (Compact Spiral):** $\chi_\nu^2 = 2.89$
* **DDO 154 (Gas-Rich Dwarf LSB):** $\chi_\nu^2 = 4.94$
* **NGC 2403 (Intermediate Spiral):** $\chi_\nu^2 = 7.31$
* **UGC 00128 (Extreme LSB):** $\chi_\nu^2 = 55.66$
* **NGC 2841 (High-Velocity Disk):** $\chi_\nu^2 = 63.61$

### Statistical Diagnostics

1. **Scaling Invariance ($v_\infty \text{ vs. } v_{\max}$):** The emergent asymptotic velocity accurately traces observed maximum velocities along the 1:1 identity line across more than a decade in dynamic scale ($25 \text{ to } 350\text{ km/s}$).
2. **Kinematic Residuals:** The residual distribution ($\Delta v = v_{\mathrm{obs}} - v_{\mathrm{mod}}$) evaluated over all 3,375 measurements is centered on zero bias ($\Delta v = 0\text{ km/s}$).
3. **Goodness-of-Fit Distribution:** Yields a catalog median of $\tilde{\chi}_\nu^2 = 3.97$, with over half the catalog satisfying $\chi_\nu^2 \le 3.97$.

---

## 📁 Repository Contents

```text
├── README.md                           # Technical report and pipeline documentation
├── feqg_sparc_pipeline.py              # Discrete tensor network simulator & diagnostic suite
├── sparc_full_catalog_results.csv      # Processed batch kinematic fits for 171 SPARC galaxies
├── sparc_benchmark_fits.png            # 6-galaxy benchmark rotation curve fits
└── sparc_full_catalog_diagnostics.png  # Global 3-panel statistical validation suite
```

---

## 🚀 Reproduction & Usage

### 1. Installation
Install the required scientific packages:
```bash
pip install numpy scipy pandas matplotlib
```

### 2. Run the Numerical Simulation
To solve the discrete min-cuts, compute the kinematic curves, and regenerate the benchmark figures:
```bash
python feqg_sparc_pipeline.py
```

Generated plots:
* `sparc_benchmark_fits.png`: Individual rotation curves for NGC 3198, NGC 2403, NGC 2841, DDO 154, UGC 00128, and NGC 6503.
* `sparc_full_catalog_diagnostics.png`: 3-panel statistical validation (Scaling relation, residual distribution, and $\chi_\nu^2$ distribution).

---

## 📖 Theoretical Reference

* **J. Giné (2026)**, *Quantum Gravity from Fractal Entanglement Geometry*, [arXiv:2607.26035 [gr-qc]](https://arxiv.org/abs/2607.26035).

---

## ⚖️ License

Distributed under the MIT License.