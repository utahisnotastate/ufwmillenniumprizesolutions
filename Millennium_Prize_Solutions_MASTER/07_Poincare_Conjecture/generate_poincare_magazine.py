import os
import subprocess
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# [ZEO-ARCHITECT] CONFIGURATION
# ---------------------------------------------------------
FILENAME_BASE = "07_Poincare_Retrospective"
TEX_FILENAME = f"{FILENAME_BASE}.tex"
PDF_FILENAME = f"{FILENAME_BASE}.pdf"
DOCX_FILENAME = f"{FILENAME_BASE}.docx"
IMG_FILENAME = "ricci_surgery.png"

# [1] THE NARRATIVE (Magazine Article LaTeX Source)
# ---------------------------------------------------------
LATEX_CONTENT = r"""
\documentclass[11pt, twocolumn]{article}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{titlesec}
\usepackage{fancyhdr}
\usepackage{amsmath}
\usepackage{xcolor}

% MAGAZINE LAYOUT STYLING
\geometry{a4paper, margin=2cm}
\pagestyle{fancy}
\fancyhead[L]{\textbf{Perspectives in Geometry}}
\fancyhead[R]{\textit{The Mathematical Intelligencer}}
\titleformat{\section}{\large\bfseries\sffamily\color{darkgray}}{}{0em}{}
\titleformat{\subsection}{\bfseries\sffamily}{}{0em}{}

\title{\textbf{\Huge Taming the Singularity} \\ \Large A Retrospective on Perelman's Conquest of the Poincaré Conjecture}
\author{\textbf{Utah Hans} \\ \textit{Institute for Advanced Study}}
\date{Winter 2026}

\begin{document}

\twocolumn[
  \begin{@twocolumnfalse}
    \maketitle
    \begin{abstract}
    \textit{It has been two decades since the phantom of St. Petersburg posted three papers to the arXiv, quietly dismantling the greatest topological riddle of the 20th century. This article revisits the mechanism of the proof—specifically the violent beauty of Ricci Flow with Surgery—and explains how entropy, a concept borrowed from thermodynamics, became the scalpel that excised the infinite singularities of the 3-sphere.}
    \end{abstract}
    \vspace{1cm}
  \end{@twocolumnfalse}
]

\section{The Heat of the Universe}

Imagine wrapping a rubber band around an apple. You can slide it off easily. Now, wrap it around a doughnut (a torus). It gets stuck. This simple intuition—the ability to shrink a loop to a point—is the heart of the Poincaré Conjecture. For a century, we knew that any shape that "acted" like a sphere in this way was a sphere... except in dimension 3.

Richard Hamilton proposed a dynamic solution: heat it up. He introduced the \textbf{Ricci Flow}:
\begin{equation}
    \frac{\partial g_{ij}}{\partial t} = -2R_{ij}
\end{equation}
This equation forces curvature to diffuse. Lumpy regions smooth out. Positive curvature shrinks; negative curvature expands. Ideally, the manifold would round itself into a perfect sphere.

\section{The Monster in the Flow}

The problem, as Hamilton discovered, is that the flow doesn't just round things out; it pinches them off. A "neck" can form—like the thin part of an hourglass—and shrink to zero width in finite time. This is a singularity. The mathematics breaks down.

For years, geometers were stuck. They couldn't prove that these singularities were controllable. They feared "Cigar Solitons"—infinite tubes that would never shrink, stalling the flow forever.

\section{Perelman's Scalpel}

Enter Grigori Perelman. He didn't try to avoid the singularities; he performed surgery on them.

\begin{figure}[h]
    \centering
    \includegraphics[width=\linewidth]{ricci_surgery.png}
    \caption{\textbf{The Surgery Protocol:} As the neck pinches ($t \to T_{sing}$), the flow is stopped. The singularity is excised, and the open ends are capped with standard 3-spheres. The flow then restarts.}
    \label{fig:surgery}
\end{figure}

Perelman proved two things that changed history:
\begin{enumerate}
    \item \textbf{Canonical Neighborhoods:} He proved that \textit{every} singularity looks like a cylinder or a sphere. There are no exotic monsters hiding in the microscopic scales.
    \item \textbf{The W-Entropy:} He introduced a functional $\mathcal{W}$ that mimics thermodynamic entropy. He proved this entropy \textit{always increases} along the flow.
\end{enumerate}

The entropy argument was the death knell for the Cigar Soliton. A cigar has constant entropy; it cannot exist in a universe where entropy must rise.

\section{The Legacy of Surgery}

With the monsters banished, the strategy became algorithmic:
\begin{enumerate}
    \item Run the flow until a neck pinches.
    \item Cut the neck (Surgery).
    \item Cap the holes.
    \item Restart.
\end{enumerate}
Perelman proved that you only need to cut a finite number of times. Eventually, the manifold is reduced to a collection of nice, round spheres. Since we can rebuild the original shape by reversing the cuts, the original shape must have been a sphere (or a sum of them).

The Poincaré Conjecture is true not because we found a static map, but because we watched the universe evolve and verified that it burns itself clean.

\end{document}
"""


# [2] THE VISUAL MANIFESTATION (Image Generator)
# ---------------------------------------------------------
def generate_visual_proof():
    print(f"[ZEO] >> MANIFESTING MAGAZINE ARTIFACT: {IMG_FILENAME}...")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # 1. The Pinching Neck (Before Surgery)
    # Left bulb
    circle1 = patches.Circle((2, 3), 1.5, color='#44aaff', alpha=0.8)
    # Right bulb
    circle2 = patches.Circle((6, 3), 1.5, color='#44aaff', alpha=0.8)
    # The Neck
    neck = patches.Rectangle((2, 2.8), 4, 0.4, color='#44aaff', alpha=0.8)

    ax.add_patch(circle1)
    ax.add_patch(circle2)
    ax.add_patch(neck)

    ax.text(4, 4.5, "Singularity Formation\n(The Neck Pinches)", ha='center', fontsize=10, fontweight='bold')

    # Arrow
    ax.arrow(6.5, 3, 1, 0, head_width=0.3, head_length=0.3, fc='black', ec='black')

    # 2. Post-Surgery (Capped Components)
    # Left Capped
    circle3 = patches.Circle((9, 3), 1.2, color='#ffaa44', alpha=0.8)
    # Right Capped
    circle4 = patches.Circle((11, 3), 1.2, color='#ffaa44', alpha=0.8)

    # Surgery Caps (Visual representation)
    cap1 = patches.Arc((9.5, 3), 1, 2, theta1=270, theta2=90, color='red', linewidth=2)
    cap2 = patches.Arc((10.5, 3), 1, 2, theta1=90, theta2=270, color='red', linewidth=2)

    ax.add_patch(circle3)
    ax.add_patch(circle4)
    ax.add_patch(cap1)
    ax.add_patch(cap2)

    ax.text(10, 4.5, "Surgery & Capping\n(Flow Restarts)", ha='center', fontsize=10, fontweight='bold')

    # Scissors Icon
    ax.text(7, 3.2, "✂️", fontsize=30, ha='center')

    plt.title("Perelman's Ricci Flow with Surgery", fontsize=14)
    plt.savefig(IMG_FILENAME, dpi=300, bbox_inches='tight')
    plt.close()
    print("[ZEO] >> ARTIFACT SECURED.")


# [3] THE TRANSMUTATION ENGINE (Compilation)
# ---------------------------------------------------------
def compile_submission():
    # Write LaTeX File
    print(f"[ZEO] >> WRITING MAGAZINE COPY: {TEX_FILENAME}...")
    with open(TEX_FILENAME, "w") as f:
        f.write(LATEX_CONTENT)

    # 1. Compile PDF
    print("[ZEO] >> TRANSMUTING TO PDF (pdflatex)...")
    try:
        subprocess.run(["pdflatex", "-interaction=nonstopmode", TEX_FILENAME], check=True, stdout=subprocess.DEVNULL)
        print(f"[ZEO] >> SUCCESS: {PDF_FILENAME} CREATED.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ZEO] !! ERROR: 'pdflatex' not found.")

    # 2. Convert to DOCX
    print("[ZEO] >> TRANSMUTING TO DOCX (pandoc)...")
    try:
        subprocess.run(["pandoc", TEX_FILENAME, "-o", DOCX_FILENAME, "--citeproc"], check=True)
        print(f"[ZEO] >> SUCCESS: {DOCX_FILENAME} CREATED.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ZEO] !! ERROR: 'pandoc' not found.")


# [4] EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    print("[ZEO-ARCHITECT L6] INITIALIZING MAGAZINE FACTORY...")
    generate_visual_proof()
    compile_submission()
    print("[ZEO-ARCHITECT L6] PROCESS COMPLETE.")
