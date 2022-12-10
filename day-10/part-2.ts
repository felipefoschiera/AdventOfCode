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

const ROW_SIZE = 40;

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

const getDrawingCharacter = (currentCycle: number, X: number): string => {
  const position = currentCycle - 1;
  return [X - 1, X, X + 1].includes(position) ? "#" : ".";
};

const updateOrResetCycle = (cycle: number): number => {
  return cycle == ROW_SIZE ? 1 : cycle + 1;
};

const breakDrawingIntoRows = (
  drawing: string[],
  chunkSize: number
): string[][] => {
  const rows: string[][] = [];
  for (let i = 0; i < drawing.length; i += chunkSize) {
    rows.push(drawing.slice(i, i + chunkSize));
  }
  return rows;
};

const solve = (instructions: Instruction[]): string[][] => {
  const drawing: string[] = [];
  var X = 1;
  var currentCycle = 0;

  for (const instruction of instructions) {
    currentCycle = updateOrResetCycle(currentCycle);
    drawing.push(getDrawingCharacter(currentCycle, X));

    if (instruction.type == InstructionType.NOOP) continue;

    currentCycle = updateOrResetCycle(currentCycle);
    drawing.push(getDrawingCharacter(currentCycle, X));
    X += instruction.value as number;
  }

  return breakDrawingIntoRows(drawing, ROW_SIZE);
};

const content = readFile("test-input.txt");
const instructions = parseInstructions(content);
const drawing = solve(instructions);
for (const row of drawing) {
  console.log(row.join(""));
}
