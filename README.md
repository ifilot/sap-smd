# Modular 8-bit "Simple as Possible" TTL-Logics Computer

![Work in Progress](https://img.shields.io/badge/status-work_in_progress-orange)
![CERN-OHL](https://img.shields.io/badge/license-CERN--OHL-blue)

This project showcases the design and construction of a modular 8-bit computer
built with TTL logic units. The core principle behind the project is to create a
**"Simple as Possible"** system, focusing on simplicity, modularity, and
compactness.

## Key Features

- **TTL Logic-Based Design**: The computer is built using traditional TTL
  (Transistor-Transistor Logic) components, adhering to a fundamental, hands-on
  approach to computing.
- **Modular Architecture**: Designed for modularity, each functional unit (ALU,
  registers, memory, control logic, etc.) is implemented as a separate module,
  allowing for easy debugging, customization, and scalability.
- **Compact Form Factor**: By predominantly using **SMD (Surface-Mount Device)**
  components, the overall size of the computer is significantly reduced compared
  to traditional through-hole designs, making it more efficient and portable.
- **Educational Value**: Serves as an excellent learning resource for
  understanding the basic principles of digital logic, computer architecture,
  and how these concepts come together to form a functional computing system.
- **Customization Potential**: The modular approach allows users to experiment
  with different configurations and expand the system to suit specific needs or
  projects.

## Goals of the Project

The project aims to:
1. **Simplify Complexity**: Break down the workings of a computer into
   comprehensible modules without unnecessary abstraction.
2. **Promote Learning**: Provide an accessible platform for enthusiasts,
   educators, and students to explore computer design.
3. **Encourage Miniaturization**: Demonstrate how SMD components can be used
   effectively in hobbyist and educational projects to save space while
   maintaining functionality.

## Design Overview

The computer consists of several interconnected modules:
- **Arithmetic Logic Unit (ALU)**: Handles basic arithmetic and logical
  operations.
- **Instruction Decoder**: Handles control lines based on machine code 
  instructions.
- **Registers**: Temporary storage for data and instructions during operation.
- **Control Logic**: Directs the flow of data and controls the execution of
  instructions.
- **Memory**: Stores programs and data, using a simple addressing scheme.
- **Output**: Facilitates communication with the user.

Each module is implemented with a combination of SMD-type TTL ICs, emphasizing
straightforward design while keeping the size compact.

## Why SMD Components?

SMD components offer several advantages:
- **Space Efficiency**: Significantly smaller than through-hole components,
  enabling more compact designs.
- **Modern Availability**: Easier to source and more reflective of contemporary
  electronics practices.
- **Scalability**: Allows for a more complex system without requiring excessive
  physical space.

## Who Is This For?

This project is ideal for:
- **Hobbyists and Makers** interested in retrocomputing and hardware design.
- **Students and Educators** looking for hands-on experience with digital logic
  and computing fundamentals.
- **Researchers and Enthusiasts** exploring minimalist computing and modular
  design approaches.

## Getting Started

1. **Clone the Repository**: Download the files and schematics from this
   repository.
2. **Review the Documentation**: Detailed explanations and schematics for each
   module are available in the `docs` directory.
3. **Assemble and Test**: Follow the provided instructions to assemble and test
   the modules step-by-step.
4. **Customize**: Modify or expand the design to suit your needs or explore
   specific areas of interest.

## Contributing

Contributions to this project are welcome! If you have ideas for improvements,
additional features, or alternative designs, feel free to fork the repository
and submit a pull request.