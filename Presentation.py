import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
print(sys.executable)
# Initialize 16:9 widescreen presentation
prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

# Academic Astro Color Palette
C_NAVY_BG   = RGBColor(7, 21, 36)      # #071524 Deep Midnight
C_CARD_BG   = RGBColor(14, 38, 64)     # #0E2640 Elevated Card Container
C_TEXT_W    = RGBColor(241, 245, 249)  # Slate 100
C_TEXT_SUB  = RGBColor(148, 163, 184)  # Slate 400
C_CYAN      = RGBColor(56, 189, 248)   # Sky Accent
C_GOLD      = RGBColor(229, 169, 60)   # Gold Accent

def set_slide_background(slide):
    """Draw a dark background across the entire slide."""
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_NAVY_BG
    bg.line.color.rgb = C_NAVY_BG
    return bg

def add_header(slide, title, category="MASTER'S THESIS PROSPECTUS DEFENSE"):
    """Adds a standardized top banner."""
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(1.1))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p_cat = tf.paragraphs[0]
    p_cat.text = category.upper()
    p_cat.font.size = Pt(10)
    p_cat.font.bold = True
    p_cat.font.color.rgb = C_CYAN
    
    p_title = tf.add_paragraph()
    p_title.text = title
    p_title.font.size = Pt(22)
    p_title.font.bold = True
    p_title.font.color.rgb = C_TEXT_W

def create_card(slide, left, top, width, height, fill_color=C_CARD_BG):
    """Creates an elevated container card."""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = fill_color
    card.line.color.rgb = RGBColor(26, 61, 98)
    card.line.width = Pt(1)
    return card

# ==============================================================================
# SLIDE 1: TITLE SLIDE
# ==============================================================================
s1 = prs.slides.add_slide(blank_layout)
set_slide_background(s1)

tb1 = s1.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.3), Inches(3.2))
tf1 = tb1.text_frame
tf1.word_wrap = True

p_sub0 = tf1.paragraphs[0]
p_sub0.text = "THEORETICAL & COMPUTATIONAL ASTROPHYSICS"
p_sub0.font.size = Pt(12)
p_sub0.font.bold = True
p_sub0.font.color.rgb = C_CYAN
p_sub0.space_after = Pt(14)

p_title = tf1.add_paragraph()
p_title.text = "Emergent Spacetime and the Dark Sector"
p_title.font.size = Pt(36)
p_title.font.bold = True
p_title.font.color.rgb = C_TEXT_W
p_title.space_after = Pt(10)

p_sub = tf1.add_paragraph()
p_sub.text = "Computational Testing of the ER=EPR Conjecture in Holographic Tensor Networks"
p_sub.font.size = Pt(18)
p_sub.font.color.rgb = C_GOLD

# Author info card
card_meta = create_card(s1, Inches(1.0), Inches(5.2), Inches(11.3), Inches(1.2))
tb_meta = s1.shapes.add_textbox(Inches(1.2), Inches(5.35), Inches(10.9), Inches(0.9))
tf_m = tb_meta.text_frame
p_m1 = tf_m.paragraphs[0]
p_m1.text = "Candidate: Master of Science Candidate      |      Scope: 40 Weeks (60 ECTS)"
p_m1.font.size = Pt(12)
p_m1.font.bold = True
p_m1.font.color.rgb = C_TEXT_W

p_m2 = tf_m.add_paragraph()
p_m2.text = "Supervisor: Theoretical Physics Group      |      Submission: October 2026"
p_m2.font.size = Pt(11)
p_m2.font.color.rgb = C_TEXT_SUB

# ==============================================================================
# SLIDE 2: THE SCIENTIFIC CRISIS (MISSING MASS)
# ==============================================================================
s2 = prs.slides.add_slide(blank_layout)
set_slide_background(s2)
add_header(s2, "The Astrophysical Missing Mass Dilemma")

c1 = create_card(s2, Inches(0.8), Inches(1.8), Inches(3.6), Inches(5.0))
tb = s2.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(3.2), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Keplerian Breakdown"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(10)

bullets1 = [
    "Galactic disks exhibit flat outer circular velocity curves (v_c ≈ const).",
    "Standard Newtonian mechanics predicts a sharp Keplerian drop-off: v_c ∝ r^(-1/2).",
    "The discrepancy points to either non-baryonic matter or modified gravitational laws."
]
for b in bullets1:
    p = tf.add_paragraph()
    p.text = "• " + b
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(10)

c2 = create_card(s2, Inches(4.8), Inches(1.8), Inches(3.6), Inches(5.0))
tb = s2.shapes.add_textbox(Inches(5.0), Inches(2.0), Inches(3.2), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Particle Relic Search Crisis"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(10)

bullets2 = [
    "ΛCDM successfully fits the CMB and large-scale cosmic structure.",
    "Decades of direct cryogenic searches (LZ, XENONnT) have produced null bounds.",
    "Particle accelerator trials (LHC) reveal zero evidence for supersymmetry or light WIMPs.",
    "Small-scale tensions persist: core-cusp and too-big-to-fail problems."
]
for b in bullets2:
    p = tf.add_paragraph()
    p.text = "• " + b
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(8)

c3 = create_card(s2, Inches(8.8), Inches(1.8), Inches(3.7), Inches(5.0))
tb = s2.shapes.add_textbox(Inches(9.0), Inches(2.0), Inches(3.3), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "The Informational Paradigm"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_TEXT_W
p.space_after = Pt(10)

bullets3 = [
    "Core Thesis: Dark matter is not a particulate relic.",
    "Gravitational anomalies emerge from non-local quantum entanglement defects.",
    "Utilizes spacetime emergence via the ER=EPR holographic bridge conjecture."
]
for b in bullets3:
    p = tf.add_paragraph()
    p.text = "• " + b
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(10)

# ==============================================================================
# SLIDE 3: THEORETICAL FRAMEWORK (ER=EPR & FEQG)
# ==============================================================================
s3 = prs.slides.add_slide(blank_layout)
set_slide_background(s3)
add_header(s3, "Theoretical Foundations: Spacetime from Entanglement")

card_l = create_card(s3, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
tb = s3.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Holographic Entanglement"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(8)

bullets_t1 = [
    "Ryu-Takayanagi Formula: S(A) = Area(γ_A) / (4 G ħ) maps boundary entropy to bulk area.",
    "First Law of Entanglement Thermodynamics: δ S_ent = δ <H_mod>.",
    "Jacobson / Faulkner et al.: Spatial entropy variations map directly to linearized Einstein field equations: G_μν = 8πG <T_μν^eff>."
]
for b in bullets_t1:
    p = tf.add_paragraph()
    p.text = "• " + b
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(8)

card_r = create_card(s3, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb = s3.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Fractal Entanglement Quantum Gravity (FEQG)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(8)

bullets_t2 = [
    "Gin\'e's Relational Metric: d_ij = -l_0 ln(I_ij / I_0) directly weights the network graph.",
    "Generalized Field Equation: G_μν = 8πG (T_μν + α E_μν + β F_μν).",
    "Informational Stress Tensor: E_μν ~ ∇_μ ∇_ν S_ent induces an effective weak-field potential.",
    "Resultant Potential: V(r) ~ 1/r^(1+ε) mimics dark matter without particle relics."
]
for b in bullets_t2:
    p = tf.add_paragraph()
    p.text = "• " + b
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(8)

# ==============================================================================
# SLIDE 4: THE RESEARCH GAP (ANALYTICAL VS COMPUTATIONAL)
# ==============================================================================
s4 = prs.slides.add_slide(blank_layout)
set_slide_background(s4)
add_header(s4, "The Research Gap: Moving from Theory to Computation")

# Left: Existing Theory
c_left = create_card(s4, Inches(0.8), Inches(1.8), Inches(5.6), Inches(4.8))
tb = s4.shapes.add_textbox(Inches(1.1), Inches(2.1), Inches(5.0), Inches(4.2))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Status of Prior Literature"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_TEXT_SUB
p.space_after = Pt(12)

points_l = [
    "Purely continuous, analytical pencil-and-paper derivations.",
    "Verlinde (2016) & Gin\'e (2026) postulated emergent elastic gravity[cite: 3].",
    "Gin\'e explicitly noted that computational simulation tools were missing.",
    "No discrete tensor network realization has been tested against galaxy catalogs."
]
for pt in points_l:
    p = tf.add_paragraph()
    p.text = "✗  " + pt
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(10)

# Right: Thesis Contribution
c_right = create_card(s4, Inches(6.9), Inches(1.8), Inches(5.6), Inches(4.8))
tb = s4.shapes.add_textbox(Inches(7.2), Inches(2.1), Inches(5.0), Inches(4.2))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "The Thesis Deliverable"
p.font.size = Pt(18)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(12)

points_r = [
    "Build a discrete 2D Poincaré hyperbolic tensor network.",
    "Inject non-local ER defect ensembles weighted by mutual information.",
    "Execute graph-theoretic Push-Relabel min-cut algorithms (discrete RT).",
    "Directly fit derived circular velocities to 175 SPARC galaxies and MaNGA 2D maps."
]
for pt in points_r:
    p = tf.add_paragraph()
    p.text = "✓  " + pt
    p.font.size = Pt(12.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(10)

# ==============================================================================
# SLIDE 5: COMPUTATIONAL ARCHITECTURE & MIN-CUT SOLVER
# ==============================================================================
s5 = prs.slides.add_slide(blank_layout)
set_slide_background(s5)
add_header(s5, "Computational Pipeline & Algorithmic Modules", "NUMERICAL REALIZATION")

stages = [
    ("Stage 1: Lattice Gen", "2D Poincaré hyperbolic disk tessellation via NetworkX / igraph.", C_CYAN),
    ("Stage 2: Baryon & ER Seeding", "Central mass injection + non-local chordal ER bridges (Gin\'e metric).", C_TEXT_W),
    ("Stage 3: Min-Cut Solver", "Push-Relabel algorithm to determine minimal surface area Area(γ_A).", C_GOLD),
    ("Stage 4: Metric Inversion", "Numerical differentiation: v_c^2(r) = r (dΦ_eff / dr).", C_TEXT_W),
    ("Stage 5: Benchmarking", "Non-linear least squares (Lmfit) against SPARC, MaNGA, and MACHO data.", C_CYAN)
]

for idx, (stg, desc, col) in enumerate(stages):
    top_pos = Inches(1.8 + idx * 1.0)
    card = create_card(s5, Inches(0.8), top_pos, Inches(11.7), Inches(0.85))
    tb = s5.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.08), Inches(11.3), Inches(0.7))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = stg
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = col
    
    p2 = tf.add_paragraph()
    p2.text = desc
    p2.font.size = Pt(11)
    p2.font.color.rgb = C_TEXT_SUB

# ==============================================================================
# SLIDE 6: EMPIRICAL BENCHMARKS (SPARC, MaNGA, MACHO)
# ==============================================================================
s6 = prs.slides.add_slide(blank_layout)
set_slide_background(s6)
add_header(s6, "Empirical Validation & Observational Data", "TESTING & FALSIFICATION")

bmarks = [
    ("1. SPARC 1D Rotation Curves", 
     "• 175 disk galaxies with high-precision Spitzer photometry.\n"
     "• Ingests gas and stellar disk profiles (M_gas + M_disk).\n"
     "• Tests classic massive spirals (NGC 3198, NGC 2841) alongside dark-matter-dominated LSB dwarfs.",
     Inches(0.8)),
    ("2. SDSS-IV MaNGA 2D Fields", 
     "• Integral Field Spectroscopy (IFS) kinematic maps.\n"
     "• Validates whether 2D tensor network preserves observed axisymmetry and velocity shear.\n"
     "• Tests non-circular motions and bar dynamics.",
     Inches(4.8)),
    ("3. LMC / MACHO Microlensing", 
     "• Gravitational microlensing observational constraints (heic0116).\n"
     "• Ensures that non-local entanglement defects do not violate empirical compact halo object limits.\n"
     "• Cross-checks smooth vs granular deflection.",
     Inches(8.8))
]

for title, content, left_pos in bmarks:
    create_card(s6, left_pos, Inches(1.8), Inches(3.7), Inches(5.0))
    tb = s6.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.0), Inches(3.3), Inches(4.5))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = C_GOLD
    p.space_after = Pt(12)
    
    for line in content.split("\n"):
        p = tf.add_paragraph()
        p.text = line
        p.font.size = Pt(11.5)
        p.font.color.rgb = C_TEXT_W
        p.space_after = Pt(8)

# ==============================================================================
# SLIDE 7: INTEGRATED GRAPHICS SPOTLIGHT
# ==============================================================================
s7 = prs.slides.add_slide(blank_layout)
set_slide_background(s7)
add_header(s7, "Visual Realization: Lattice, Halo, and Workflow", "FIGURE PORTFOLIO")

img_files = ["figure1.png", "figure2.png", "figure3.png"]
captions = [
    "Fig 1: ER=EPR Geometric Substrate",
    "Fig 2: Empirical Target Rotation Curves",
    "Fig 3: Python Tensor Network Pipeline"
]

for idx, (img_name, cap) in enumerate(zip(img_files, captions)):
    x_pos = Inches(0.8 + idx * 4.0)
    create_card(s7, x_pos, Inches(1.8), Inches(3.7), Inches(5.0))
    
    if os.path.exists(img_name):
        s7.shapes.add_picture(img_name, x_pos + Inches(0.15), Inches(2.0), Inches(3.4), Inches(3.2))
    else:
        # Placeholder box if image is not present
        box = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, x_pos + Inches(0.2), Inches(2.2), Inches(3.3), Inches(2.8))
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(20, 50, 85)
        tf_b = box.text_frame
        tf_b.text = f"[{img_name}]\nPlace in directory to display"
    
    tb = s7.shapes.add_textbox(x_pos + Inches(0.2), Inches(5.4), Inches(3.3), Inches(1.2))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = cap
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = C_CYAN

# ==============================================================================
# SLIDE 8: BOUNDARY CONDITIONS & FUTURE OUTLOOK (BULLET CLUSTER & 2029)
# ==============================================================================
s8 = prs.slides.add_slide(blank_layout)
set_slide_background(s8)
add_header(s8, "Theoretical Boundaries & The 2029 Horizon", "CRITICAL RIGOR")

card_bc = create_card(s8, Inches(0.8), Inches(1.8), Inches(5.6), Inches(5.0))
tb = s8.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(5.2), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Boundary: The Bullet Cluster (1E 0657-558)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(10)

bc_points = [
    "Verlinde explicitly noted: static equations hold only in equilibrium systems (spherical/disk symmetry).",
    "Dynamic mergers exhibit spatial offsets between collisional gas (X-ray) and lensing peaks.",
    "Thesis Scope: Rigorously bounded to virialized galaxies (SPARC/MaNGA).",
    "Non-equilibrium relaxation and dynamic time-lags are scoped for PhD extension."
]
for pt in bc_points:
    p = tf.add_paragraph()
    p.text = "• " + pt
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(8)

card_fut = create_card(s8, Inches(6.8), Inches(1.8), Inches(5.7), Inches(5.0))
tb = s8.shapes.add_textbox(Inches(7.0), Inches(2.0), Inches(5.3), Inches(4.5))
tf = tb.text_frame
tf.word_wrap = True

p = tf.paragraphs[0]
p.text = "Observational Horizon (2028-2029)"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(10)

fut_points = [
    "ESA Euclid Space Telescope: Comprehensive dark halo mass mapping.",
    "Vera C. Rubin Observatory (LSST): Weak-lensing shear profiles for millions of galaxies.",
    "Nancy Grace Roman Space Telescope: High-resolution 2D convergence maps.",
    "Strategic Alignment: The thesis pipeline is completed now to ingest these upcoming datasets."
]
for pt in fut_points:
    p = tf.add_paragraph()
    p.text = "• " + pt
    p.font.size = Pt(11.5)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(8)

# ==============================================================================
# SLIDE 9: 40-WEEK RESEARCH TIMELINE
# ==============================================================================
s9 = prs.slides.add_slide(blank_layout)
set_slide_background(s9)
add_header(s9, "40-Week Master Timeline & Milestones", "EXECUTION ROADMAP")

phases = [
    ("Phase 1: Analytical Modeling", "Weeks 1–10", "Derive E_μν and <T_μν^eff>; verify w=0 dust equation of state; complete Ch. 1 & 2.", C_TEXT_W),
    ("Phase 2: Codebase Construction", "Weeks 11–22", "Implement 2D Poincaré hyperbolic graph and Push-Relabel min-cut engine; draft Ch. 3.", C_CYAN),
    ("Phase 3: Simulation & Fitting", "Weeks 23–32", "Seed non-local ER bridges; fit curves against SPARC database; draft Ch. 4 & 5.", C_GOLD),
    ("Phase 4: Synthesis & Defense", "Weeks 33–40", "Comparative χ^2 analysis vs NFW/MOND; finalize thesis manuscript; thesis defense.", C_TEXT_W)
]

for idx, (title, wks, desc, col) in enumerate(phases):
    top_pos = Inches(1.8 + idx * 1.25)
    create_card(s9, Inches(0.8), top_pos, Inches(11.7), Inches(1.1))
    
    tb = s9.shapes.add_textbox(Inches(1.0), top_pos + Inches(0.12), Inches(3.2), Inches(0.8))
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = col
    
    p_w = tf.add_paragraph()
    p_w.text = wks
    p_w.font.size = Pt(11)
    p_w.font.color.rgb = C_CYAN
    
    tb_d = s9.shapes.add_textbox(Inches(4.5), top_pos + Inches(0.2), Inches(7.7), Inches(0.7))
    tf_d = tb_d.text_frame
    tf_d.word_wrap = True
    p_d = tf_d.paragraphs[0]
    p_d.text = desc
    p_d.font.size = Pt(12)
    p_d.font.color.rgb = C_TEXT_W

# ==============================================================================
# SLIDE 10: CONCLUSION & SEVEN-CHAPTER SYLLABUS
# ==============================================================================
s10 = prs.slides.add_slide(blank_layout)
set_slide_background(s10)
add_header(s10, "Summary: Structure of the Dissertation", "SYLLABUS & CONCLUSION")

chapters = [
    "Ch 1: The Missing Mass Dilemma & Galactic Dynamics",
    "Ch 2: The Quantum Geometry of Spacetime (ER=EPR)",
    "Ch 3: Holographic & Fractal Entanglement Thermodynamics",
    "Ch 4: The Entanglement Defect Model of Dark Matter",
    "Ch 5: Discrete Numerical Engine & Algorithmic Architecture",
    "Ch 6: Simulation Runs, SPARC Benchmarking, and Fitting",
    "Ch 7: Discussion, Astrophysical Implications & Outlook"
]

c_syl = create_card(s10, Inches(0.8), Inches(1.8), Inches(6.8), Inches(5.0))
tb = s10.shapes.add_textbox(Inches(1.0), Inches(2.0), Inches(6.4), Inches(4.6))
tf = tb.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "Seven-Chapter Master Syllabus"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_CYAN
p.space_after = Pt(8)

for ch in chapters:
    p = tf.add_paragraph()
    p.text = "• " + ch
    p.font.size = Pt(11)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(4)

c_concl = create_card(s10, Inches(8.0), Inches(1.8), Inches(4.5), Inches(5.0))
tb_c = s10.shapes.add_textbox(Inches(8.2), Inches(2.0), Inches(4.1), Inches(4.6))
tf_c = tb_c.text_frame
tf_c.word_wrap = True
p = tf_c.paragraphs[0]
p.text = "Core Takeaway"
p.font.size = Pt(16)
p.font.bold = True
p.font.color.rgb = C_GOLD
p.space_after = Pt(10)

takeaways = [
    "Bridging the Gap: Takes analytical ER=EPR and FEQG proposals into a falsifiable numerical laboratory.",
    "High Deliverable Value: Combines graph-theoretic min-cuts with real astrophysical observational data.",
    "Future-Proof: Builds the testing engine ahead of the 2028–2029 Euclid and Rubin survey releases."
]
for t in takeaways:
    p = tf_c.add_paragraph()
    p.text = "✔ " + t
    p.font.size = Pt(12)
    p.font.color.rgb = C_TEXT_W
    p.space_after = Pt(10)

# Save
prs.save("thesis_presentation.pptx")
print("Successfully generated thesis_presentation.pptx!")