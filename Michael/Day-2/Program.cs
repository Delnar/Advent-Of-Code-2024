// File 🐐
using System.Globalization;

var inputFilePath = "input.txt";
var lines = File.ReadAllLines(inputFilePath);

// Numbers
List<int> numbers1 = new List<int>();
List<int> numbers2 = new List<int>();

//key = uniqueLeftNumber, value = count
Dictionary<int, int> Similarities = new Dictionary<int, int>();


// Populate the number lists
foreach (var line in lines)
{
    var parts = line.Split("   ");
    numbers1.Add(int.Parse(parts[0]));
    numbers2.Add(int.Parse(parts[1]));
}

// Sort the number Lists
numbers1.Sort();
numbers2.Sort();


// Store Unique Left list numbers (numbers1)
var uniqueLeftNumbers = numbers1.Distinct().ToList();

// Populate our Similarities Dictionary
foreach (int num1 in uniqueLeftNumbers)
{
    int count = 0; // count # of times num1 appears in numbers2 list

    foreach (int num2 in numbers2)
    {
        if (num1 == num2)
        {
            count++;
        }
    }

    Similarities.Add(num1, count); // key= # from left list, value= its count
}

// Calculate Similarity Score 🐐
/* =  Each number in the left list X it's count */
var similarityScore = 0;
foreach (var num in numbers1)
{
    foreach (var entry in Similarities)
    {
        if (num == entry.Key)
        {
            similarityScore += entry.Key * entry.Value;
        }
    }
}

// Print the sum 🐐
Console.WriteLine(similarityScore);