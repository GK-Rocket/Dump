#include <iostream>
#include <chrono>

// Function to be benchmarked
void myFunction()
{
    // Perform some time-consuming task
    for (int i = 0; i < 100000000; ++i)
    {
        // Do some computation
    }
}

int main()
{
    // Start the timer
    auto startTime = std::chrono::high_resolution_clock::now();

    // Call the function to be benchmarked
    myFunction();

    // Stop the timer and calculate the duration
    auto endTime = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(endTime - startTime).count();

    // Print the duration
    std::cout << "Execution time: " << duration << " milliseconds" << std::endl;

    return 0;
}
