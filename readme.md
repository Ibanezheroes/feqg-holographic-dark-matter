# Holographic ER=EPR Tensor Networks & Galactic Kinematics

### Discrete Numerical Simulator & Empirical Verification of Fractal Entanglement Quantum Gravity (FEQG)

This repository provides an open-source, discrete numerical simulation engine evaluating **Jaume Giné's (2026)** *Fractal Entanglement Quantum Gravity (FEQG)* framework against galactic kinematics from the **SPARC** (Spitzer Photometry & Accurate Rotation Curves) database.

It addresses an explicit open frontier highlighted in Giné (2026): translating the continuous, analytical formulations of informational quantum gravity and non-local entanglement into discrete, falsifiable graph-theoretic models.

---

## 🔬 Theoretical Framework: FEQG & Holographic Entanglement

Modern particle dark matter searches (cryogenic direct detection and collider probes) continue to produce null bounds, while small-scale astrophysical tensions (core-cusp, missing satellites) persist under standard $\Lambda\text{CDM}$. FEQG proposes that classical spacetime and dark sector phenomenology emerge from the entanglement architecture of a universal quantum state.

1. **Information-Theoretic Metric (Giné 2026):**  
   Spatial separation $d_{ij}$ is derived directly from mutual information $I_{ij}$:
   $$d_{ij} = -l_0 \ln\left(\frac{I_{ij}}{I_0}\right)$$
   strongly entangled subsystems establish immediate geometric proximity, while weakly correlated modes recede into the distance.

2. **Informational Stress Tensor & Emergent Field Equation:**  
   The macroscopic field equation incorporates matter alongside entanglement and fractal corrections:
   $$G_{\mu\nu} = 8\pi G \left( T_{\mu\nu} + \alpha E_{\mu\nu} + \beta F_{\mu\nu} \right)$$
   where the informational stress tensor $E_{\mu\nu} \sim \nabla_\mu \nabla_\nu S_{\mathrm{ent}} - g_{\mu\nu}\Box S_{\mathrm{ent}}$ sources curvature without non-baryonic particle relics.

3. **Discrete Ryu–Takayanagi (RT) Cuts on Hyperbolic Lattices:**  
   Discretizing continuous 2D spatial manifolds into hyperbolic tensor graphs, the holographic entanglement entropy of a boundary disk subregion $A$ is solved via minimal cut surfaces $\gamma_A$:
   $$S(A) = \min_{\gamma_A} \sum_{e \in \gamma_A} \ln(\chi_e) = \frac{\mathrm{Area}(\gamma_A)}{4 G \hbar}$$

4. **ER=EPR Defect Superposition:**  
   Superimposing non-local chordal wormhole defects (Planckian ER bridges) with spatial probability $P(r_i, r_j) \propto |r_i - r_j|^{-\gamma}$ generates an informational backreaction that yields an effective orbital velocity:
   $$v_c^2(r) = r \frac{\partial \Phi_{\mathrm{eff}}}{\partial r} = v_{\mathrm{bary}}^2(r) + v_{\mathrm{ER}}^2(r)$$
   In the deep low-acceleration regime ($a_{\mathrm{bary}} \ll a_0$), this boundary cut naturally reproduces flat velocity plateaus and the Baryonic Tully–Fisher Relation ($v_c^4 \approx G M_{\mathrm{bary}} a_0$).

---

## 💻 Simulation Pipeline Architecture

The computational engine (`feqg_sparc_pipeline.py`) executes a 5-stage numerical pipeline:

```
+-------------------------------------------------------------+
| 1. Hyperbolic Lattice Generation (NetworkX, SciPy Sparse)  |
|    Poincaré disk tessellation discretizing spatial slices   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 2. Baryonic Seeding & Mass Potential Injection             |
|    SPARC gas + disk + bulge profiles & stellar M/L (Upsilon)|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 3. ER Defect Superposition (Giné Metric Scaling)           |
|    Power-law chordal edges weighted via d_ij = -l_0 ln(I/I0)|
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 4. Max-Flow / Min-Cut Solver (Push-Relabel Algorithm)       |
|    Solves extremal cuts gamma_A to compute S_ent(r)         |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
| 5. Kinematic Differentiation & Goodness-of-Fit Evaluation   |
|    g_eff = -grad Phi_eff -> circular velocity v_c(r) & chi2 |
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
| **MOND** | Modified Inertia / Gravitation | 2 ($\Upsilon_\star, a_0$) | 3.6 – 4.1 | Resolved | Empirical acceleration scale |
| **FEQG Tensor Net (This Work)**| **Informational Defects ($E_{\mu\nu}$)** | **2 ($\Upsilon_\star, a_{0,\mathrm{eff}}$)** | **3.97** | **Resolved** | **First-principles bulk min-cut** |

### Key Benchmark Galaxy Fits

* **NGC 3198 (Classic Spiral):** $\chi_\nu^2 = 2.69$
* **NGC 6503 (Compact Spiral):** $\chi_\nu^2 = 2.89$
* **DDO 154 (Gas-Rich Dwarf LSB):** $\chi_\nu^2 = 4.94$
* **NGC 2403 (Intermediate Spiral):** $\chi_\nu^2 = 7.31$
* **UGC 00128 (Extreme LSB):** $\chi_\nu^2 = 55.66$
* **NGC 2841 (High-Velocity Disk):** $\chi_\nu^2 = 63.61$

### Statistical Diagnostics

1. **Scaling Invariance ($v_\infty \text{ vs. } v_{\max}$):** The emergent asymptotic velocity accurately traces observed maximum velocities along the $1:1$ identity line across an order of magnitude in dynamic scale ($25 \text{ to } 350\text{ km/s}$).
2. **Kinematic Residuals:** The residual distribution ($\Delta v = v_{\mathrm{obs}} - v_{\mathrm{mod}}$) evaluated over all 3,375 measurements is unbiased and centered at $\Delta v = 0\text{ km/s}$.
3. **Goodness-of-Fit Distribution:** Yields a catalog median of $\tilde{\chi}_\nu^2 = 3.97$, with over half the catalog satisfying $\chi_\nu^2 \le 3.97$.

---

## 📁 Repository Contents

```
├── README.md                           # Technical report and pipeline documentation
├── requirements.txt                    # Python runtime dependencies
├── feqg_sparc_pipeline.py              # Self-contained tensor network simulator & plotting suite
├── sparc_full_catalog_results.csv      # Processed batch kinematic fits for 171 SPARC galaxies
├── docs/
│   └── Gine_2026_FEQG.pdf              # Foundation paper (J. Giné, arXiv:2607.26035)
└── figures/
    ├── sparc_benchmark_fits.png        # 6-galaxy benchmark rotation curve fits
    └── sparc_full_catalog_diagnostics.png # Global 3-panel statistical validation
```

---

## 🚀 Reproduction & Usage

### 1. Installation

Ensure Python 3.9+ is installed, clone this repository, and install dependencies:

```bash
git clone https://github.com/Ibanezheroes/feqg-holographic-dark-matter.git
cd feqg-holographic-dark-matter
pip install -r requirements.txt
```

### 2. Run the Numerical Simulation

To execute the graph min-cut solver, compute the kinematic profiles, and regenerate the benchmark figures:

```bash
python feqg_sparc_pipeline.py
```

Generated plots:
* `sparc_benchmark_fits.png`: Individual rotation curves for NGC 3198, NGC 2403, NGC 2841, DDO 154, UGC 00128, and NGC 6503.
* `sparc_full_catalog_diagnostics.png`: 3-panel statistical validation (Scaling relation, residual distribution, and $\chi_\nu^2$ distribution).

---

## 📖 References

1. **J. Giné**, *Quantum Gravity from Fractal Entanglement Geometry*, arXiv:2607.26035 [gr-qc] (2026).
2. **E. P. Verlinde**, *Emergent Gravity and the Dark Universe*, SciPost Phys. 2, 016 (2017), arXiv:1611.02269 [hep-th].
3. **S. Ryu and T. Takayanagi**, *Holographic Derivation of Entanglement Entropy from AdS/CFT*, Phys. Rev. Lett. 96, 181602 (2006).
4. **J. Maldacena and L. Susskind**, *Cool horizons for entangled black holes*, Fortschr. Phys. 61, 781-811 (2013).
5. **F. Lelli, S. S. McGaugh, and J. M. Schombert**, *SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves*, Astron. J. 152, 157 (2016).

---

## ⚖️ License

Distributed under the MIT License. Contributions, bug reports, and extensions to 3D networks or lensing benchmarks are welcome via Pull Requests.