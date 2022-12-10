import * as fs from "node:fs";

const readFile = (filePath: string): string[] => {
  const content = fs.readFileSync(filePath, "utf8");
  const lines = content.split("\n").map((line: string) => line.trim());
  return lines;
};

enum InstructionType {
  ADDX,
  NOOP,
}

interface Instruction {
  type: InstructionType;
  value?: number;
}

const parseInstructions = (lines: string[]): Instruction[] => {
  return lines.map((line) => {
    const [instruction, value] = line.split(" ");
    if (instruction == "addx") {
      return {
        type: InstructionType.ADDX,
        value: Number.parseInt(value),
      };
    }
    return {
      type: InstructionType.NOOP,
    };
  });
};

const solve = (instructions: Instruction[]) => {
  const cycleValue = new Map<number, number>();
  var X = 1;
  var currentCycle = 0;

  for (const instruction of instructions) {
    if (instruction.type == InstructionType.NOOP) {
      currentCycle++;
      cycleValue.set(currentCycle, X);
      continue;
    }

    currentCycle++;
    cycleValue.set(currentCycle, X);
    currentCycle++;
    cycleValue.set(currentCycle, X);
    X += instruction.value as number;
  }
  return cycleValue;
};

const sumPowerInPositions = (
  values: Map<number, number>,
  positions: number[]
): number => {
  return positions
    .map((pos) => pos * (values.get(pos) as number))
    .reduce((a, b) => a + b, 0);
};

const content = readFile("test-input.txt");
const instructions = parseInstructions(content);
const cycleValues = solve(instructions);
const selectedPowers = sumPowerInPositions(
  cycleValues,
  [20, 60, 100, 140, 180, 220]
);
console.log(selectedPowers);
