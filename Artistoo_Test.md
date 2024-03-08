**What is Artistoo?**

Artistoo (Artificial Tissue Toolbox) is a framework that lets you build
interactive, explorable simulation models of cells and tissues in the
web browsers. In few words, it is a software tool used for simulating
biological tissue. This package is particularly useful in computational
biology and bioinformatics, where understanding cell behaviors in a
virtual environment is essential.

The platform is available under the MIT open-source license and was
created by Inge M.N.Wortel and Johannes Textor. It implements the
Cellular Potts Model (CPM), a versatile framework for simulating various
biological processes at the tissue scale. Additionally, it can also
handle simpler Cellular Automaton (CA) models. Simulations can be shared
via URLs or HTML files without requiring software installation. It
features an interactive interface, allowing users to modify parameters
in real-time through HTML sliders and input fields.

Artistoo is entirely JavaScript-based, allowing for high-performance web
simulations without the need for software installation. Users can
interact with the simulations through web pages with customizable HTML
elements, making it user-friendly for non-programmers.

**What are CPM and CA models?**

-   CPM (Cellular Potts Model): Developed in 1980s, CPM is used for
    simulating the collective behavior of cellular structures. It's
    particularly effective for modeling the morphology (the study of the
    forms of things) and dynamics of tissues, cell sorting, and cell
    movement. CPM represents cells as extended objects in a lattice,
    allowing the simulation of various cell shapes and interactions.
    This tool models cells and tissues as collections of pixels on a 2D
    or 3D, where each pixel has an "identity" linking it to a specific
    cell or to the empty background.

-   CA (Cellular Automation): Originating in the 1940s by John Neumann,
    CA is a simpler model where space is divided into discrete cells,
    each of which can be in one of a finite number of states. The state
    of each cell changes over time based on a set of rules that depend
    on the states of neighboring cells. CA is used for modeling a wide
    range of phenomena, including biological growth and behavior, fluid
    dynamics, and pattern formation.

**CPM Limitations:**

Criticisms have included their lack of scalability, as well as
difficulties in linking CPM parameters to measurable, real-world
quantities.

Although CPMs are relatively efficient models, tissue-scale simulations
still require substantial computational resources. For this reason, many
frameworks rely on the C++ programming language for computation steps,
which requires them to be built for and installed on the user's native
operating system.

Mature Modelling frameworks with CPM Examples based on C++ Programming:

-   CompuCell3D.

-   Morpheus.

-   Tissue Simulation Toolkit.

-   CHASTE.

**Artistoo is based on JavaScript entirely:**

As mentioned before, this tool is built entirely in JavaScript. Although
interpreted languages like JavaScript have classically been deemed too
inefficient for running simulations, the creators found that this no
longer holds: investments by major tech companies have tremendously
improved JavaScript engines over the past years, to the point that our
CPM now has no major performance disadvantage compared to existing C++
frameworks.

The JavaScript implementation of Artistoo opens new possibilities for
rapid and low barrier sharing of CPM simulations with students,
collaborators, and readers or reviewers of a paper.

Unlike existing frameworks, Artistoo allows building simulations that
run in the web browser without the need to install any software.
Artistoo models run on any platform providing a standards-compliant web
browser -- be it a desktop computer, a tablet, or a mobile phone. These
simulations can be published on any web server or saved locally and do
not rely on any back-end servers being available. They can be made
explorable, enabling viewers to interact with the simulation and see the
effect of changing model parameters in real time.

Artistoo is a JavaScript library implemented as an ECMAScript 6 module,
which can be loaded into an HTML page or accessed from within a Node.js
command line application. Artistoo is an open-source library released
under the MIT license and is freely available on GitHub
at <https://github.com/ingewortel/artistoo>.

**Artistoo Users, Challenges, and Design Philosophy:**

Computational modelling research involves two important, but distinct
categories of researchers that tend to have different types of
expertise.

-   Builders: The scientists designing the models and performing the
    research; these are typically computational biologists with at least
    some basic programming skills. 

-   Viewers: members of the broader research community who should be
    able to access and understand these models once they are built; this
    group may also include biologists and students without programming
    expertise.

A major challenge in the design of modelling software is to cater to
both these groups at the same time. Tools revolving around a front-end
graphical user interface (GUI) are ideal for viewers (no programming
required) but tend to lose some of the flexibility desired by builders
(anything not yet implemented in the GUI typically becomes harder to do,
and it becomes more difficult to automate simulations and
post-processing). Vice versa, a more flexible coding-based tool is
comfortable.

**Builders and Developers:**

-   Model builders create these web applications using the Artistoo
    framework. They can do this at different levels of complexity:
    Artistoo users build models via simple changes to configuration
    objects (requiring very little knowledge of Artistoo or
    programming), or by incorporating the many available methods in a
    few simple lines of code; this requires no in-depth knowledge of the
    framework 'under the hood' architecture while still providing high
    flexibility.

-   Finally, Artistoo developers have the ultimate freedom to add custom
    plugins to the existing framework where needed. Only this group
    requires in-depth knowledge of the framework and slightly more
    advanced JavaScript skills.

Documentation helps both these groups to get started with the framework.

**Artistoo Approachability:**

As we know, methods implemented in this framework allow users to
simulate, visualize, and analyze a wide range of CPM Models. The
Artistoo GitHub repository (within documentation) contains example code
for models of various biological processes such as: simulation of
tissues, cell migration, and cell interactions.

First-time users can download these HTML pages and modify parameters
without needing to learn the implementation details of the framework, or
to have programmed in JavaScript before. Alternatively, the Simulation
class provides default methods for setting up and visualizing
simulations, allowing users to get started with the library without
having to set up this "boilerplate" code themselves.

Advanced users can instead build simulations from scratch and customize
them using the many available options and methods. Once they become
accustomed with the framework, they can also develop and plug in their
own code modules.

**Creators thought on Artistoo:**

They now hope to open this powerful avenue of model sharing for CPM
research, allowing users to build online web pages and "explorables"
that combine interactive simulations with model explanations. The
framework's performance (like that of existing frameworks in C++) is
sufficient to allow for interactive CPM simulations. They have been
developing the library for more than 5 years, also using it for robust
simulation work in our research.

They do not envision Artistoo to replace existing modelling software;
rather, it can complement software directed at computational biologists
and developers by letting users build explorable and sharable versions
of a simulation. To the best of their knowledge, Artistoo is the first
CPM simulation framework supporting interactive simulations in the web
browser that can be shared via a simple URL, without requiring installed
software or back-end servers. They hope that this will unlock avenues of
sharing and communicating (CPM) simulations to much larger audiences.

**Open Science Movement is Constantly Changing:**

CompuCell3D, Tellurium, and PhysiCell: Host an online version on NanoHub
(which users can access without installing software locally). These
frameworks have also shown how such online models can be made
interactive by using (variations of) Jupyter notebooks.

Right now, Artistoo does not (yet) support all features of existing
frameworks (Morpheus, CHASTE, CompuCell3D, Tissue Simulation Toolkit),
such as solvers for reaction--diffusion equations or SBML-encoded
intracellular signaling or writing output in formats like VTK and HDF5.
Nevertheless, Artistoo simulations are highly customizable, and a wide
range of CPM models can already be constructed using the framework in
its current state. The software's modular structure also makes it easy
for future developers to extend it with custom code.

**Different Ways of Representing Space in Computational Simulations:**

-   On Lattice: In this approach, space is divided into a grid (like a
    chessboard). Each cell or particle occupies a specific position on
    this grid. It\'s like having a fixed framework where each element
    has a designated spot. This method is typically simpler and
    computationally less demanding.

-   Off Lattice: Here, there\'s no fixed grid. Cells or particles can
    move freely in a continuous space, without being restricted to
    specific grid positions. This approach allows for more realistic and
    flexible movements but can be more complex and computationally
    intensive.

**Some examples of Modeling Approaches (Easily Explain):**

-   CPM (Cellular Potts Model): A computational model used to simulate
    how cells grow and interact with each other. It\'s like having cells
    on a grid, where each cell can spread or move based on certain
    rules.

-   CA (Cellular Automaton): A model where space is divided into cells
    in a grid. Each cell changes its state (like on/off) based on the
    state of neighboring cells, following simple rules. It\'s often used
    for simulating patterns or simple biological processes.

-   ODEs (Ordinary Differential Equations): Mathematical equations used
    to describe how things change over time. They\'re used in
    simulations to model continuous processes like chemical reactions or
    population dynamics.

-   Finite Elements: A method for solving complex equations by breaking
    down a large problem (like stress in a material) into smaller,
    simpler parts (finite elements), and then solving these parts.

-   Particle-Based: In this type of modeling, individual elements,
    referred to as particles, interact with each other following
    physical laws. This approach allows for simulating systems where the
    position and interaction of each particle are important, such as in
    fluid dynamics or molecular dynamics. Each particle can move freely
    in space (off lattice), and their interactions can simulate a
    variety of phenomena, from the behavior of atoms and molecules to
    the movement of cells in a biological system.

-   Agent Based: A model where individual entities (agents) like cells
    or animals are simulated. Each agent behaves independently according
    to set rules, allowing for complex systems and interactions to be
    studied.
