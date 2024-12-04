using System.Runtime.CompilerServices;

internal class Program {
	private static readonly string[] puzzleInput = File.ReadAllLines("./PuzzleInput.txt");

	private static void Main(string[] args) {
		//Part1();
		Part2();
	}

	private static bool AreLevelsSafe(string[] levels, out string errMsg) {
		int previous = -1;
		int seesaw = 0;

		errMsg = "";
		for (int j = 0; j < levels.Length; j++) {
			int level = int.Parse(levels[j]);

			if (previous == -1) {
				previous = level;
				continue;
			} else {
				int rawDist = level - previous;
				int distance = Math.Abs(rawDist);
				if (rawDist != 0)
					seesaw += rawDist / distance;
				//Console.WriteLine(rawDist);

				if (distance < 1 || distance > 3) {
					errMsg = $"Distance Fail {distance}";
					return false;
				}

				previous = level;
			}
		}

		if (Math.Abs(seesaw) == levels.Length - 1) {
			//we safe
		} else {
			errMsg = $"seesaw Fail {seesaw}";
			return false;
		}

		return true;
	}

	private static void Part1() {
		int safeCount = 0;
		for (int i = 0; i < puzzleInput.Count(); i++) {
			string line = puzzleInput[i];
			string[] levels = line.Split(' ');

			string errMsg = "";
			bool isSafe = true;

			isSafe = AreLevelsSafe(levels, out errMsg);

			Console.WriteLine($"{isSafe} || {line} || {errMsg}");

			if (isSafe) {
				safeCount += 1;
			}
		}

		Console.WriteLine(safeCount);
	}

	private static void Part2() {
		int safeCount = 0;
		for (int i = 0; i < puzzleInput.Count(); i++) {
			string line = puzzleInput[i];
			string[] levels = line.Split(' ');

			string errMsg = "";
			bool isSafe = true;

			isSafe = AreLevelsSafe(levels, out errMsg);

			Console.WriteLine($"{isSafe} || {line} || {errMsg}");

			if (isSafe) {
				safeCount += 1;
				continue;
			}

			//Not safe; let the insanity commence...
			for (int j = 0; j < levels.Length; j++) {
				//we need to exclude this one
				List<string> levels2 = levels.ToList();
				levels2.RemoveAt(j);

				isSafe = AreLevelsSafe(levels2.ToArray(), out errMsg);

				levels2.Insert(j, "  ");

				Console.WriteLine($">> {isSafe} {string.Join(' ', levels2)} || {errMsg}");

				//If any of these come back as safe, then we are safe...? Yeah.
				if (isSafe) {
					safeCount += 1;
					break;
				}
			}
		}

		Console.WriteLine(safeCount);
	}
}