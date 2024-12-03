// File
var inputFilePath = "input.txt";
var lines = File.ReadAllLines(inputFilePath);

// Numbers
List<int> numbers1 = new List<int>();
List<int> numbers2 = new List<int>();
List<int> differences = new List<int>();


// Populate the lists
foreach (var line in lines)
{
    var parts = line.Split("   ");
    numbers1.Add(int.Parse(parts[0]));
    numbers2.Add(int.Parse(parts[1]));
}

// Sort the Lists
numbers1.Sort();
numbers2.Sort();


// Populate the differences
for (int i = 0; i <= numbers1.Count - 1; i++)
{
    differences.Add(Math.Abs(numbers1[i] - numbers2[i]));
}


// Get the sum of all the differences.
var differencesSum = differences.Sum();

// Print the sum
Console.WriteLine(differencesSum);