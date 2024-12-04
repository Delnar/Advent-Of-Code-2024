internal class Program {
	private static readonly string[] puzzleInput = File.ReadAllLines("./PuzzleInput.txt");

	private static void Main(string[] args) {
		//Part1();
		Part2();
	}

	private static void Part1() {
		List<int> leftList = new();
		List<int> rightList = new();

		foreach (string input in puzzleInput) {
			string[] split = input.Split("   ");

			leftList.Add(int.Parse(split[0]));
			rightList.Add(int.Parse(split[1]));
		}

		leftList.Sort();
		rightList.Sort();

		int totalDistance = 0;
		for (int i = 0; i < leftList.Count(); i++) {
			int distance = Math.Abs(leftList[i] - rightList[i]);

			totalDistance += distance;
		}

		Console.WriteLine(totalDistance);
	}

	private static void Part2() {
		List<int> leftList = new();
		List<int> rightList = new();

		foreach (string input in puzzleInput) {
			string[] split = input.Split("   ");

			leftList.Add(int.Parse(split[0]));
			rightList.Add(int.Parse(split[1]));
		}

		leftList.Sort();
		rightList.Sort();

		int totalSimilarity = 0;
		for (int i = 0; i < leftList.Count(); i++) {
			int number = leftList[i];
			int numCount = 0;
			for (int j = 0; j < rightList.Count(); j++) {
				if (number == rightList[j]) {
					numCount++;
				}
			}

			totalSimilarity += number * numCount;
		}

		Console.WriteLine(totalSimilarity);
	}
}