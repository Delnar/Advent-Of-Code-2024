//     Each report is a line consisting of numbers called levels, and these are separated by spaces
//     So, a report only counts as 'safe' if both of the following are true:
//     1. The levels are either all increasing or all decreasing.
//     2. Any two adjacent levels differ by at least one and at most three.

// Sample: 7 6 4 2 1

/* File Stuff */
using System.Diagnostics;
using System.Numerics;
using System.Text.Json.Serialization;

var inputFilePath = "./input.txt";
var lines = File.ReadAllLines(inputFilePath); // each line is a report

/* Rules is rules */
const int MinDifference = 1;
const int MaxDifference = 3;
int safeReports = 0;
int errorCount = 0;

// Check if the levels are increasing
bool increasing(List<int> levels)
{
    for (int i = 1; i < levels.Count; i++)
    {
        if (levels[i] < levels[i - 1])
        {
            return false;
        }
    }
    return true;
}

// Check if the levels are decreasing
bool decreasing(List<int> levels)
{
    for (int i = 1; i < levels.Count; i++)
    {
        if (levels[i] > levels[i - 1])
        {
            return false;
        }
    }
    return true;
}

// Check if the difference between two levels is valid
bool validDifference(int a, int b)
{
    int difference = Math.Abs(b - a);

    if (difference >= MinDifference && difference <= MaxDifference)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void resetErrorCount()
{
    errorCount = 0;
}


string[] test =
{
    "7 6 4 2 1",
    "1 2 7 8 9",
    "9 7 6 2 1",
    "1 3 2 4 5",
    "8 6 4 4 1",
    "1 3 6 7 9"
};

void Part1()
{
    // Iterate over each line (record)
    // Change lines to test to test the sample data
    foreach (var line in lines)
    {
        List<int> levels = line.Split(" ").Select(int.Parse).ToList();

        if (increasing(levels) || decreasing(levels))
        {
            bool allValid = true;
            for (int i = 1; i < levels.Count; i++)
            {
                if (!validDifference(levels[i], levels[i - 1]))
                {
                    allValid = false;
                    break;
                }
            }
            if (allValid)
            {
                safeReports++;
            }
        }
    }
}


void Part2()
{
    foreach (var line in lines)
    {
        List<int> levels = line.Split(" ").Select(int.Parse).ToList();

        if (IsSafe(levels))
        {
            safeReports++;
            continue;
        }

        // Try removing each level and check if the report becomes safe
        bool reportIsSafe = false;
        for (int i = 0; i < levels.Count; i++)
        {
            // Create a new list without the current level
            List<int> modifiedLevels = new List<int>(levels);
            modifiedLevels.RemoveAt(i);

            if (IsSafe(modifiedLevels))
            {
                reportIsSafe = true;
                break; // No need to check further
            }
        }

        if (reportIsSafe)
        {
            safeReports++;
        }
    }
}

// Check if a list of levels satisfies the rules
bool IsSafe(List<int> levels)
{
    // Check if the levels are all increasing or all decreasing
    bool isIncreasing = increasing(levels);
    bool isDecreasing = decreasing(levels);

    if (!isIncreasing && !isDecreasing) return false;

    // Check if all differences are valid
    for (int i = 1; i < levels.Count; i++)
    {
        if (!validDifference(levels[i], levels[i - 1]))
        {
            return false;
        }
    }

    return true;
}


//Part1();
Part2();
Console.WriteLine(safeReports);
