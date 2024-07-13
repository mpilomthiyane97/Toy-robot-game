# Toy Robot Game

This is a simple command-line based toy robot game where you can control a robot by issuing various commands. The robot can move forward, backward, turn, sprint, and replay a series of commands.

## Getting Started

### Prerequisites

- Python 3.x



## Running the Game

### To Run

1. Start the game by running the following command in your terminal:
    ```sh
    python robot.py
    ```
2. Follow the input prompts to control the robot and achieve the desired outputs.

### Commands

- `OFF` - Shut down the robot.
- `HELP` - Provide information about commands.
- `FORWARD <steps>` - Move forward by the specified number of steps.
- `BACK <steps>` - Move backward by the specified number of steps.
- `RIGHT` - Turn right by 90 degrees.
- `LEFT` - Turn left by 90 degrees.
- `SPRINT <steps>` - Sprint forward according to a formula.
- `REPLAY` - Replay all the previous commands.
- `REPLAY <n>` - Replay the last `n` commands.
- `REPLAY <n> SILENT` - Replay the last `n` commands silently.
- `REPLAY <n> REVERSED` - Replay the last `n` commands in reverse order.
- `REPLAY <n> REVERSED SILENT` - Replay the last `n` commands in reverse order silently.
- `REPLAY <start>-<end>` - Replay a range of commands from `start` to `end`.

## Testing

### To Run Tests

1. To run all the unittests:
    ```sh
    python3 -m unittest tests/test_main.py
    ```
2. To run a specific step's unittest, e.g. step *1*:
    ```sh
    python3 -m unittest tests.test_main.MyTestCase.test_step1
    ```

## Example Usage

```sh
$ python robot.py
What do you want to name your robot? R2D2
R2D2: Hello kiddo!
R2D2: What must I do next? FORWARD 10
 > R2D2 moved forward by 10 steps.
 > R2D2 now at position (0,10).
R2D2: What must I do next? LEFT
 > R2D2 turned left.
 > R2D2 now at position (0,10).
R2D2: What must I do next? OFF
R2D2: Shutting down..
